﻿module Spiral.Server

open System
open System.IO
open System.Collections.Generic
open FSharpx.Collections

open Spiral.Config
open Spiral.Tokenize
open Spiral.TypecheckingUtils
open Spiral.Blockize

open Hopac
open Hopac.Infixes
open Hopac.Extensions
open Hopac.Stream

type TokReq =
    | Put of string
    | Modify of SpiEdit
    | GetRange of VSCRange * (VSCTokenArray -> unit)
type TokRes = {blocks : Block list; errors : VSCError []}
type ParserRes = {bundles : Bundle list; parser_errors : VSCError []; tokenizer_errors : VSCError []}

let tokenizer req =
    let lines : LineToken [] ResizeArray = ResizeArray([[||]])
    let mutable errors_tokenization = [||]
    let mutable blocks : Block list = []

    let res_text = Src.create()
    let replace edit =
        errors_tokenization <- Tokenize.replace lines errors_tokenization edit // Mutates the lines array
        blocks <- block_separate lines blocks edit
        Src.value res_text {blocks=blocks; errors=errors_tokenization}

    req |> Stream.consumeJob (function 
        | Put text -> replace {|from=0; nearTo=lines.Count; lines=Utils.lines text|}
        | Modify edit -> replace edit
        | GetRange((a,b),res) ->
            let from, near_to = min (lines.Count-1) a.line, min lines.Count (b.line+1)
            vscode_tokens from (lines.GetRange(from,near_to-from |> max 0).ToArray()) |> res
            Job.unit()
        )
    Src.tap res_text

let parser is_top_down req =
    let dict = System.Collections.Generic.Dictionary(HashIdentity.Reference)
    req |> Stream.keepPreceding1 |> Stream.mapFun (fun (a : TokRes) ->
        let b = 
            List.map (fun x -> {
                parsed = Utils.memoize dict (block_init is_top_down) x.block
                offset = x.offset
                }) a.blocks
        dict.Clear(); List.iter2 (fun a b -> dict.Add(a.block,b.parsed)) a.blocks b
        let bundles, parser_errors = block_bundle b
        {bundles = bundles; parser_errors = parser_errors; tokenizer_errors = a.errors}
        )
    
type TypecheckerRes = (Bundle * Infer.InferResult) PersistentVector * bool
let typechecker (req : ParserRes Stream) : TypecheckerRes Stream =
    let req = Stream.values req
    let res = Src.create()
    let r = Src.tap res
    let rec waiting a = req ^=> fun b ->
        let rec loop s i b = 
            match PersistentVector.tryNth i a, b with
            | Some(bundle,_ as r), bundle' :: b' when bundle = bundle' -> loop (PersistentVector.conj r s) (i+1) b'
            | _ -> s, b
        loop PersistentVector.empty 0 b.bundles |> processing
    and processing = function
        | a, [] -> Alt.prepare (Src.value res (a,true) >>- fun () -> waiting a)
        | a, b :: b' -> waiting a <|> Alt.prepare (Src.value res (a, false) >>- fun () -> 
            let env = 
                match PersistentVector.tryLast a with
                | Some(_,b : Infer.InferResult) -> b.blockwise_top_env
                | None -> Infer.default_env
            let a' = PersistentVector.conj (b,Infer.infer env (bundle b)) a
            processing (a', b')
            )
    Hopac.server (waiting PersistentVector.empty)
    r

let hover (req : (VSCPos * (string option -> unit)) Stream) (req_tc : TypecheckerRes Stream) =
    let req, req_tc = Stream.values req, Stream.values req_tc
    let rec processing ((x,_ as r) : TypecheckerRes) = waiting <|> (req ^=> fun (pos,ret) ->
        let rec block_from i = 
            if 0 <= i then 
                let a,b = x.[i]
                if (List.head a).offset <= pos.line then b.hovers else block_from (i-1)
            else [||]
        block_from (x.Length-1) |> Array.tryPick (fun ((a,b),r) ->
            if pos.line = a.line && (a.character <= pos.character && pos.character < b.character) then Some r else None
            ) |> ret
        processing r
        )
    and waiting = req_tc ^=> processing
    Hopac.server waiting

type ProjectReq =
    | ProjOpen of string
    | ProjChange of string
    | ProjLinks of ({|uri : string; range : VSCRange|} [] -> unit)

type SuggestedFix = 
    | None = 0
    | CreateFile = 1
    | CreateDirectory = 2
type ProjectError = {|message : string; range : VSCRange; code : SuggestedFix|}
let project project_dir (req : ProjectReq Stream) =
    let req = Stream.values req
    let res : ProjectError [] Src = Src.create()
    let r = Src.tap res

    let rec file x =
        match config x with
        | Ok x ->
            let errors = ResizeArray()
            let validate_dir dir =
                match dir with
                | Some (r,dir) ->
                    try let x = DirectoryInfo(Path.Combine(project_dir,dir))
                        if x.Exists = false then errors.Add {|message="Directory does not exist."; range=r; code=SuggestedFix.CreateDirectory|}
                        x.FullName
                    with e -> errors.Add {|message=e.Message; range=r; code=SuggestedFix.None|}; project_dir
                | None -> project_dir
            let moduleDir = validate_dir x.moduleDir
            let outDir = validate_dir x.outDir

            let links = ResizeArray()
            let rec validate_file prefix = function
                | File(r,a,is_top_down,is_include) -> 
                    try let x = FileInfo(Path.Combine(prefix,a + (if is_top_down then ".spi" else ".spir")))
                        if x.Exists then links.Add {|uri="file:///" + x.FullName; range=r|}
                        else errors.Add {|message="File does not exist."; range=r; code=SuggestedFix.CreateFile|}
                    with e -> errors.Add {|message=e.Message; range=r; code=SuggestedFix.None|}
                | Directory(r,a,b) -> 
                    try let x = DirectoryInfo(Path.Combine(prefix,a))
                        if x.Exists then Array.iter (validate_file x.FullName) b
                        else errors.Add {|message="Directory does not exist."; range=r; code=SuggestedFix.CreateDirectory|}
                    with e -> errors.Add {|message=e.Message; range=r; code=SuggestedFix.None|}
            if 0 = errors.Count then Array.iter (validate_file moduleDir) x.modules
            Src.value res (errors.ToArray()) >>= fun () -> ready (links.ToArray())
        | Error er -> Src.value res (er |> Array.map (fun (a,b) -> {|message=a; range=b; code=SuggestedFix.None|})) >>= erroneous
    and ready links = req >>= function
        | ProjOpen _ -> ready links
        | ProjChange x -> file x
        | ProjLinks ret -> ret links; ready links
    and erroneous () = req >>= function
        | ProjOpen _ -> erroneous()
        | ProjChange x -> file x
        | ProjLinks ret -> ret [||]; erroneous()
    and opening () = req >>= function
        | ProjOpen x | ProjChange x -> file x
        | ProjLinks ret -> ret [||]; opening()
    Hopac.start (opening())
    r

type ClientReq =
    | ProjectFileOpen of {|uri : string; spiprojText : string|}
    | ProjectFileChange of {|uri : string; spiprojText : string|}
    | ProjectFileLinks of {|uri : string|}
    | FileOpen of {|uri : string; spiText : string|}
    | FileChanged of {|uri : string; spiEdit : SpiEdit|}
    | FileTokenRange of {|uri : string; range : VSCRange|}
    | HoverAt of {|uri : string; pos : VSCPos|}
    | BuildFile of {|uri : string|}

type ClientRes =
    | ProjectErrors of {|uri : string; errors : ProjectError []|}
    | TokenizerErrors of {|uri : string; errors : VSCError []|}
    | ParserErrors of {|uri : string; errors : VSCError []|}
    | TypeErrors of {|uri : string; errors : VSCError list|}

let port = 13805
let uri_server = sprintf "tcp://*:%i" port
let uri_client = sprintf "tcp://localhost:%i" (port+1)

open FSharp.Json
open NetMQ
open NetMQ.Sockets

let [<EntryPoint>] main _ =
    use poller = new NetMQPoller()
    use server = new RouterSocket()
    poller.Add(server)
    server.Options.ReceiveHighWatermark <- System.Int32.MaxValue
    server.Bind(uri_server)
    printfn "Server bound to: %s" uri_server

    use queue_server = new NetMQQueue<NetMQMessage>()
    poller.Add(queue_server)

    use queue_client = new NetMQQueue<ClientRes>()
    poller.Add(queue_client)

    let file = Utils.memoize (Dictionary()) <| fun (uri : string) ->
        let s = {|token = Src.create(); hover = Src.create()|}
        let token = tokenizer (Src.tap s.token)
        let parse = parser (System.IO.Path.GetExtension(uri) = ".spi") token
        let ty = typechecker parse
        hover (Src.tap s.hover) ty

        token |> Stream.consumeFun (fun x -> queue_client.Enqueue(TokenizerErrors {|uri=uri; errors=x.errors|}))
        parse |> Stream.consumeFun (fun x -> queue_client.Enqueue(ParserErrors {|uri=uri; errors=x.parser_errors|}))
        ty |> Stream.consumeFun (fun (x,_) -> 
            let errors = PersistentVector.foldBack (fun (_,x : Infer.InferResult) errors -> List.append errors x.errors) x []
            queue_client.Enqueue(TypeErrors {|errors=errors; uri=uri|})
            )
        s

    let project = Utils.memoize (Dictionary()) <| fun (uri : string) ->
        let s = Src.create()
        project (FileInfo(Uri(uri).LocalPath).Directory.FullName) (Src.tap s)
        |> Stream.consumeFun (fun errors -> queue_client.Enqueue(ProjectErrors {|uri=uri; errors=errors|}))
        s

    let buffer = Dictionary()
    let last_id = ref 0
    use __ = server.ReceiveReady.Subscribe(fun s ->
        let rec loop () = Utils.remove buffer !last_id (body <| NetMQMessage 3) id
        and body (msg : NetMQMessage) (address : NetMQFrame, x) =
            incr last_id
            let push_back (x : obj) = 
                match x with
                | :? Option<string> as x -> 
                    match x with 
                    | None -> msg.Push("null") 
                    | Some x -> msg.Push(sprintf "\"%s\"" x)
                | _ -> msg.Push(Json.serialize x)
                msg.PushEmptyFrame(); msg.Push(address)
            let send_back x = push_back x; server.SendMultipartMessage(msg)
            let send_back_via_queue x = push_back x; queue_server.Enqueue(msg)
            match x with
            | ProjectFileOpen x -> Src.value (project x.uri) (ProjOpen x.spiprojText) |> Hopac.start; send_back null
            | ProjectFileChange x -> Src.value (project x.uri) (ProjChange x.spiprojText) |> Hopac.start; send_back null
            | ProjectFileLinks x -> Src.value (project x.uri) (ProjLinks send_back_via_queue) |> Hopac.start
            | FileOpen x -> Src.value (file x.uri).token (TokReq.Put(x.spiText)) |> Hopac.start; send_back null
            | FileChanged x -> Src.value (file x.uri).token (TokReq.Modify(x.spiEdit)) |> Hopac.start; send_back null
            | FileTokenRange x -> Hopac.start (timeOutMillis 30 >>=. Src.value (file x.uri).token (TokReq.GetRange(x.range,send_back_via_queue)))
            | HoverAt x -> Hopac.start (Src.value (file x.uri).hover (x.pos, send_back_via_queue))
            | BuildFile x ->
                let x = Uri(x.uri).LocalPath
                match IO.Path.GetExtension(x) with
                | ".spi" | ".spir" -> IO.File.WriteAllText(IO.Path.ChangeExtension(x,"fsx"), "// Compiled with Spiral v0.2.")
                | _ -> ()
                send_back null
            loop ()
        let msg = server.ReceiveMultipartMessage(3)
        let address = msg.Pop()
        msg.Pop() |> ignore
        let (id : int), x = Json.deserialize(Text.Encoding.Default.GetString(msg.Pop().Buffer))
        if !last_id = id then body msg (address, x)
        else buffer.Add(id,(address,x))
        )

    use client = new RequestSocket()
    client.Connect(uri_client)

    use __ = queue_client.ReceiveReady.Subscribe(fun x -> 
        x.Queue.Dequeue() |> Json.serialize |> client.SendFrame
        client.ReceiveMultipartMessage() |> ignore
        )

    use __ = queue_server.ReceiveReady.Subscribe(fun x -> x.Queue.Dequeue() |> server.SendMultipartMessage)

    poller.Run()
    0