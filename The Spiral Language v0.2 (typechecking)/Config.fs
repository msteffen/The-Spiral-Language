﻿// Everything that deals with Spiral project files themselves goes here
module Spiral.Config
open System
open FParsec

type VSCPos = {|line : int; character : int|}
type VSCRange = VSCPos * VSCPos
type VSCError = string * VSCRange

type FileHierarchy =
    | Directory of VSCRange * string * FileHierarchy []
    | File of VSCRange * string * is_top_down : bool * is_include : bool
type ConfigResumableError =
    | DuplicateFiles of VSCRange [] []
    | DuplicateRecordFields of VSCRange [] []
    | MissingNecessaryRecordFields of string [] * VSCRange
type ConfigFatalError =
    | Tabs of VSCRange []
    | ParserError of string * VSCRange
exception ConfigException of ConfigFatalError

let rec spaces_template s = (spaces >>. optional (followedByString "//" >>. skipRestOfLine true >>. spaces_template)) s
let spaces s = spaces_template s

let raise' x = raise (ConfigException x)
let raise_if_not_empty exn l = if Array.isEmpty l = false then raise' (exn l)
let add_to_exception_list' (p: CharStream<ResizeArray<ConfigResumableError>>) = p.State.UserState.Add
let add_to_exception_list (p: CharStream<ResizeArray<ConfigResumableError>>) exn l = if Array.isEmpty l = false then p.State.UserState.Add (exn l)
let column (p : CharStream<_>) = p.Column
let pos (p : CharStream<_>) : VSCPos = {|line=int p.Line - 1; character=int p.Column - 1|}
let pos' p = Reply(pos p)
let range f p = pipe3 pos' f pos' (fun a b c -> ((a, c) : VSCRange), b) p

let is_small_var_char_starting c = isAsciiLower c
let is_var_char c = isAsciiLetter c || c = '_' || c = ''' || isDigit c
let file' p = many1Satisfy2L is_small_var_char_starting is_var_char "lowercase variable name" p
let file p = range (file' .>> spaces) p

let file_hierarchy p =
    let rec file_hierarchy_list p =
        let i = column p
        let expr p = if i = column p then file_or_directory p else Reply(ReplyStatus.Error,expected "file or directory on the same or greater indentation as the first one")
        (many1 expr |>> fun l ->
            let l = l |> List.toArray
            let _ = 
                l |> Array.map (fun (File(a,b,_,_) | Directory(a,b,_)) -> b,a)
                |> Array.groupBy fst
                |> Array.choose (fun (a,b) -> if b.Length > 1 then Some (Array.map snd b) else None)
                |> add_to_exception_list p DuplicateFiles
            l
            ) p

    and file_or_directory p =
        (range file' >>= fun (r,name) p ->
            let x = p.Peek2()
            match x.Char0, x.Char1 with
            | '/',_ -> p.Skip(); (spaces >>. file_hierarchy_list |>> fun files -> Directory(r,name,files)) p
            | '-',_ -> p.Skip(); (spaces >>% File(r,name,true,true)) p
            | '*','-' -> p.Skip(2); (spaces >>% File(r,name,false,true)) p
            | '*',_ -> p.Skip(); (spaces >>% File(r,name,false,false)) p
            | _ -> (spaces >>% File(r,name,true,false)) p
            ) p

    file_hierarchy_list p

let tab_positions (str : string): VSCRange [] =
    let mutable line = -1
    Utils.lines str |> Array.choose (fun x -> 
        line <- line + 1
        let x = {|line=line; character=x.IndexOf("\t")|}
        if x.character <> -1 then Some(x,{|x with character=x.character+1|}) else None
        )

let record_reduce (field: Parser<'schema -> 'schema, _>) s p =
    let record_body p =
        let i = column p
        let indent expr p = if i = column p then expr p else Reply(ReplyStatus.Error,expected "record field on the same indentation as the first one")
        many (indent field) p
    (range record_body |>> fun (r,l) -> r, List.fold (|>) s l) p

let record_field (name, p) = 
    (skipString name >>. skipChar ':' >>. spaces >>. range p)
    |>> (fun (r,f) (s,l) -> f s, (r, name) :: l)

let record fields fields_necessary schema =
    let fields = choice (List.map record_field fields)
    record_reduce fields (schema, []) >>= fun (range,(schema,l)) p ->
        let l = List.toArray l
        let _ =
            let names = Array.map snd l
            Set fields_necessary - Set names
            |> Set.toArray
            |> add_to_exception_list p (fun fields -> MissingNecessaryRecordFields(fields,range))
        let _ =
            Array.groupBy snd l
            |> Array.choose (fun (k, v) -> if v.Length > 1 then Some (Array.map fst v) else None)
            |> add_to_exception_list p DuplicateRecordFields

        Reply(schema)

type Schema = {
    outDir : (VSCRange * string) option
    name : (VSCRange * string) option
    version : (VSCRange * string) option
    moduleDir : (VSCRange * string) option
    modules : FileHierarchy []
    }

type ConfigError = ResumableError of ConfigResumableError [] | FatalError of ConfigFatalError

open System.IO
let config text =
    try 
        let _ = tab_positions text |> raise_if_not_empty Tabs

        let directory p = (range (restOfLine true .>> spaces) |>> fun (r,x) -> Some(r,x.Trim())) p

        let fields = [
            "outDir", directory |>> fun x s -> {s with outDir=x}
            "version", range (restOfLine true .>> spaces) |>> fun (r,x) s -> {s with version=Some (r,x.TrimEnd())}
            "name", file |>> fun x s -> {s with name=Some x}
            "moduleDir", directory |>> fun x s -> {s with moduleDir=x}
            "modules", file_hierarchy |>> fun x s -> {s with modules=x}
            ]
        let necessary = ["modules"]

        let schema: Schema = {
            outDir=None
            name=None
            version=None
            moduleDir=None
            modules=[||]
            }

        match runParserOnString (spaces >>. record fields necessary schema .>> eof) (ResizeArray()) "spiral.config" text with
        | Success(a,userstate,_) -> 
            if userstate.Count > 0 then userstate.ToArray() |> ResumableError |> Result.Error else Result.Ok a
        | Failure(messages,error,_) ->
            let x = {|line=int error.Position.Line - 1; character=int error.Position.Column - 1|}
            ParserError(messages, (x,{|x with character=x.character+1|})) |> FatalError |> Result.Error
    with 
        | :? ConfigException as e -> e.Data0 |> FatalError |> Result.Error

    |> Result.mapError (fun x ->
        let fatal_error = function
            | Tabs l -> l |> Array.map (fun x -> "Tab not allowed.", x)
            | ParserError(x,p) -> [|(Utils.lines x).[3..] |> String.concat "\n", p|]
        let inline duplicate er = Array.collect (fun l -> let er = er (Array.length l) in Array.map (fun x -> er, x) l)
        let resumable_error = function
            | DuplicateFiles l -> duplicate (sprintf "Duplicate name. Count: %i") l
            | DuplicateRecordFields l -> duplicate (sprintf "Duplicate record field. Count: %i") l
            | MissingNecessaryRecordFields (l,p) -> [|sprintf "Record is missing the fields: %s" (String.concat ", " l), p|]
        match x with
        | ResumableError x -> Array.collect resumable_error x
        | FatalError x -> fatal_error x
        )