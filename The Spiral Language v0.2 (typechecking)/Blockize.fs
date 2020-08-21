﻿module Spiral.Blockize
open Hopac
open Hopac.Infixes
open Hopac.Extensions

open Spiral.Config
open Spiral.Tokenize

type FileOpenRes = VSCError []
type FileChangeRes = VSCError []
type FileTokenAllRes = VSCTokenArray

type Req =
    | Put of string * IVar<FileOpenRes>
    | Modify of SpiEdit * IVar<FileChangeRes>
    | GetRange of VSCRange * IVar<VSCTokenArray>

open Spiral.BlockParsing
type Block = {block: LineToken [] []; offset: int; parsed: Result<TopStatement, (Range * ParserErrors) list>}

let block_init is_top_down (block : LineToken [] []) offset =
    let comments, tokens = 
        block |> Array.mapi (fun line x ->
            let comment, len = match Array.tryLast x with Some (r, TokComment c) -> Some (r, c), x.Length-1 | _ -> None, x.Length
            let tokens = Array.init len (fun i ->
                let r, x = x.[i] 
                ({ line=line; character=r.from }, { line=line; character=r.nearTo }), x
                )
            comment, tokens
            )
        |> Array.unzip

    let env : BlockParsing.Env = 
        {comments = comments; tokens = Array.concat tokens; i = ref 0; 
        is_top_down = is_top_down; default_int=Int32T; default_float=Float64T}
    {block=block; offset=offset; parsed=BlockParsing.parse env}

/// Reads the comments up to a statement, and then reads the statement body. Leaves any errors for the parsing stage.
let block_at is_top_down (lines : LineToken [] ResizeArray) i =
    let ar = ResizeArray()
    let rec loop_initial i =
        if i < lines.Count then
            let x = lines.[i]
            ar.Add x
            if 0 < x.Length then
                let r,t = x.[0]
                if r.from = 0 then
                    match t with
                    | TokComment _ -> loop_initial (i+1)
                    | _ -> loop_body (i+1)
                else loop_initial (i+1) // This branch will be an error in the parsing stage unless the token is a comment.
            else loop_initial (i+1)
    and loop_body i =
        if i < lines.Count then
            let x = lines.[i]
            if 0 < x.Length then
                let r,_ = x.[0]
                if r.from <> 0 then ar.Add x; loop_body (i+1)
            else ar.Add x; loop_body (i+1)
    loop_initial i
    block_init is_top_down (ar.ToArray()) i

let rec block_all is_top_down (lines : _ ResizeArray) i = 
    if i < lines.Count then 
        let x = block_at is_top_down lines i
        x :: block_all is_top_down lines (i+x.block.Length) else []

let block_separate is_top_down (lines : LineToken [] ResizeArray) (blocks : Block list) (edit : SpiEdit) =
    // Lines added minus lines removed.
    let line_adjustment = edit.lines.Length - (edit.nearTo - edit.from)
    // The dirty block boundary needs to be more conservative when a separator is added in the first position of block.
    let dirty_from = let x = lines.[edit.from] in edit.from - (if Array.length x = 0 || 0 < (fst x.[0]).from then 1 else 0)
    let is_dirty x = (dirty_from <= x.offset && x.offset < edit.nearTo) || (x.offset <= dirty_from && dirty_from < x.offset + Array.length x.block)
    let rec loop blocks i =
        if i < lines.Count then
            match blocks with
            | x :: xs ->
                // If the block is dirty, forget it.
                if is_dirty x then loop xs i else 
                    // If the block is past the removal range, adjust its line offset.
                    let x = {x with offset=if edit.nearTo <= x.offset then x.offset + line_adjustment else x.offset}
                    // The block can't be dirty here. Hence if the offsets are the same, so are the blocks. Take it.
                    if x.offset = i then x :: loop xs (i + Array.length x.block)
                    // Else if the block has been skipped over, forget it.
                    elif x.offset < i then loop xs i
                    // Else the block has been dirty filtered, recalculate it.
                    else let x = block_at is_top_down lines i in x :: loop blocks (i + Array.length x.block)
            | [] -> block_all is_top_down lines i
        else []
    loop blocks 0

type Bundle = (int * TopStatement) [] // offset * statement
let block_bundle (l : Block list) : Bundle [] * VSCError [] =
    let (+.) a b = BlockParsingError.add_line_to_range a b
    let bundle = ResizeArray()
    let errors = ResizeArray()
    let temp = ResizeArray()
    let move_temp () = if 0 < temp.Count then bundle.Add(temp.ToArray()); temp.Clear()
    let rec init (l : Block list) =
        match l with
        | x :: x' ->
            match x.parsed with
            | Ok (TopAnd(r,_)) -> errors.Add("Invalid `and` statement.", x.offset +. r); init x'
            | Ok (TopRecInl _ as a) -> temp.Add(x.offset,a); recinl x'
            | Ok (TopNominal _ | TopUnion _ as a) -> temp.Add(x.offset,a); rectype x'
            | Ok a -> temp.Add(x.offset, a); move_temp(); init x'
            | Error er -> BlockParsingError.show_block_parsing_error x.offset er |> errors.AddRange; init x'
        | [] -> move_temp()
    and recinl (l : Block list) =
        match l with
        | x :: x' ->
            match x.parsed with
            | Ok (TopAnd(_, TopRecInl _ & a)) -> temp.Add(x.offset,a); recinl x'
            | Ok (TopAnd(r, _)) -> errors.Add("inl/let recursive statements can only be followed by `and` inl/let statements.", x.offset +. r); recinl x'
            | Ok _ -> move_temp(); init l
            | Error er -> BlockParsingError.show_block_parsing_error x.offset er |> errors.AddRange; recinl x'
        | [] -> move_temp()
    and rectype (l : Block list) =
        match l with
        | x :: x' ->
            match x.parsed with
            | Ok (TopAnd(_, (TopNominal _ | TopUnion _) & a)) -> temp.Add(x.offset,a); rectype x'
            | Ok (TopAnd(r, _)) -> errors.Add("`union` or `nominal` can only be followed by `and union` or `and nominal.", x.offset +. r); rectype x'
            | Ok _ -> move_temp(); init l
            | Error er -> BlockParsingError.show_block_parsing_error x.offset er |> errors.AddRange; rectype x'
        | [] -> move_temp()
    init l
    bundle.ToArray(), errors.ToArray()

let server (uri : string) = Job.delay <| fun () ->
    let is_top_down = System.IO.Path.GetExtension(uri) = ".spi"
    let lines : LineToken [] ResizeArray = ResizeArray([[||]])
    let mutable errors_tokenization = [||]
    let mutable blocks : Block list = []

    let replace edit =
        errors_tokenization <- Tokenize.replace lines errors_tokenization edit // Mutates the lines array
        blocks <- block_separate is_top_down lines blocks edit
        let bundles, errors_parsing = block_bundle blocks
        Array.append errors_tokenization errors_parsing

    let req = Ch()
    let loop =
        Ch.take req >>= function
            | Put(text,res) -> replace {|from=0; nearTo=lines.Count; lines=Utils.lines text|} |> IVar.fill res
            | Modify(edits,res) -> replace edits |> IVar.fill res
            | GetRange((a,b),res) -> // It is assumed that a.character = 0 and b.character = length of the line
                let from, near_to = a.line, b.line+1
                vscode_tokens from (lines.GetRange(from,near_to-from).ToArray()) |> IVar.fill res
    Job.foreverServer loop >>-. req
