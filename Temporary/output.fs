module SpiralExample.Main
let cuda_kernels = """

extern "C" {
    
}
"""

type Tuple0 =
    struct
    val mem_0: int64
    val mem_1: int64
    new(arg_mem_0, arg_mem_1) = {mem_0 = arg_mem_0; mem_1 = arg_mem_1}
    end
Tuple0(3L, 4L)
