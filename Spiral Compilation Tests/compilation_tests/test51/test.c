#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
typedef enum {REFC_DECR, REFC_INCR, REFC_SUPPR} REFC_FLAG;
typedef struct UH0 UH0;
void UHRefc0(UH0 * x, REFC_FLAG q);
typedef struct UH1 UH1;
void UHRefc1(UH1 * x, REFC_FLAG q);
typedef struct {
    int tag;
    union {
        struct {
            int32_t v0;
        } case0; // A
        struct {
            double v0;
        } case1; // B
    };
} US0;
struct UH0 {
    int refc;
    int tag;
    union {
        struct {
            int32_t v0;
            UH0 * v1;
        } case0; // Cons
    };
};
struct UH1 {
    int refc;
    int tag;
    union {
        struct {
            double v0;
            UH1 * v1;
        } case0; // Cons
    };
};
static inline void USRefcBody0(US0 x, REFC_FLAG q){
    switch (x.tag) {
    }
}
void USRefc0(US0 * x, REFC_FLAG q){
    USRefcBody0(*x, q);
}
US0 US0_0(int32_t v0) { // A
    US0 x;
    x.tag = 0;
    x.case0.v0 = v0;
    USRefcBody0(x, REFC_INCR);
    return x;
}
US0 US0_1(double v0) { // B
    US0 x;
    x.tag = 1;
    x.case1.v0 = v0;
    USRefcBody0(x, REFC_INCR);
    return x;
}
static inline void UHRefcBody0(UH0 x, REFC_FLAG q){
    switch (x.tag) {
        case 0: {
            UHRefc0(x.case0.v1, q);
            break;
        }
    }
}
void UHRefc0(UH0 * x, REFC_FLAG q){
    if (x != NULL) {
        int refc = (x->refc += q & REFC_INCR ? 1 : -1);
        if (!(q & REFC_SUPPR) && refc == 0) {
            UHRefcBody0(*x, REFC_DECR);
            free(x);
        }
    }
}
UH0 * UH0_0(int32_t v0, UH0 * v1) { // Cons
    UH0 x;
    x.tag = 0;
    x.refc = 1;
    x.case0.v0 = v0; x.case0.v1 = v1;
    UHRefcBody0(x, REFC_INCR);
    return memcpy(malloc(sizeof(UH0)),&x,sizeof(UH0));
}
UH0 * UH0_1() { // Nil
    UH0 x;
    x.tag = 1;
    x.refc = 1;
    UHRefcBody0(x, REFC_INCR);
    return memcpy(malloc(sizeof(UH0)),&x,sizeof(UH0));
}
static inline void UHRefcBody1(UH1 x, REFC_FLAG q){
    switch (x.tag) {
        case 0: {
            UHRefc1(x.case0.v1, q);
            break;
        }
    }
}
void UHRefc1(UH1 * x, REFC_FLAG q){
    if (x != NULL) {
        int refc = (x->refc += q & REFC_INCR ? 1 : -1);
        if (!(q & REFC_SUPPR) && refc == 0) {
            UHRefcBody1(*x, REFC_DECR);
            free(x);
        }
    }
}
UH1 * UH1_0(double v0, UH1 * v1) { // Cons
    UH1 x;
    x.tag = 0;
    x.refc = 1;
    x.case0.v0 = v0; x.case0.v1 = v1;
    UHRefcBody1(x, REFC_INCR);
    return memcpy(malloc(sizeof(UH1)),&x,sizeof(UH1));
}
UH1 * UH1_1() { // Nil
    UH1 x;
    x.tag = 1;
    x.refc = 1;
    UHRefcBody1(x, REFC_INCR);
    return memcpy(malloc(sizeof(UH1)),&x,sizeof(UH1));
}
uint64_t method0(UH0 * v0){
    UHRefc0(v0, REFC_INCR);
    switch (v0->tag) {
        case 0: { // Cons
            int32_t v1 = v0->case0.v0; UH0 * v2 = v0->case0.v1;
            UHRefc0(v2, REFC_INCR);
            UHRefc0(v0, REFC_DECR);
            uint64_t v3;
            v3 = hash(v1);
            uint64_t v4;
            v4 = v3 * 9973ull;
            uint64_t v5;
            v5 = method0(v2);
            UHRefc0(v2, REFC_DECR);
            uint64_t v6;
            v6 = v4 + v5;
            uint64_t v7;
            v7 = 9223372036854775807ull + v6;
            uint64_t v8;
            v8 = v7 * 9973ull;
            uint64_t v9;
            v9 = 0l;
            uint64_t v10;
            v10 = 1ull + v9;
            uint64_t v11;
            v11 = v8 * v10;
            return v11;
            break;
        }
        case 1: { // Nil
            UHRefc0(v0, REFC_DECR);
            uint64_t v12;
            v12 = 1l;
            uint64_t v13;
            v13 = 1ull + v12;
            uint64_t v14;
            v14 = 9223372036854765835ull * v13;
            return v14;
            break;
        }
    }
}
uint64_t method1(UH1 * v0){
    UHRefc1(v0, REFC_INCR);
    switch (v0->tag) {
        case 0: { // Cons
            double v1 = v0->case0.v0; UH1 * v2 = v0->case0.v1;
            UHRefc1(v2, REFC_INCR);
            UHRefc1(v0, REFC_DECR);
            uint64_t v3;
            v3 = hash(v1);
            uint64_t v4;
            v4 = v3 * 9973ull;
            uint64_t v5;
            v5 = method1(v2);
            UHRefc1(v2, REFC_DECR);
            uint64_t v6;
            v6 = v4 + v5;
            uint64_t v7;
            v7 = 9223372036854775807ull + v6;
            uint64_t v8;
            v8 = v7 * 9973ull;
            uint64_t v9;
            v9 = 0l;
            uint64_t v10;
            v10 = 1ull + v9;
            uint64_t v11;
            v11 = v8 * v10;
            return v11;
            break;
        }
        case 1: { // Nil
            UHRefc1(v0, REFC_DECR);
            uint64_t v12;
            v12 = 1l;
            uint64_t v13;
            v13 = 1ull + v12;
            uint64_t v14;
            v14 = 9223372036854765835ull * v13;
            return v14;
            break;
        }
    }
}
int32_t main(){
    uint64_t v1;
    v1 = hash(1l);
    uint64_t v2;
    v2 = 9223372036854775807ull + v1;
    uint64_t v3;
    v3 = v2 * 9973ull;
    uint64_t v4;
    v4 = 0l;
    uint64_t v5;
    v5 = 1ull + v4;
    uint64_t v6;
    v6 = v3 * v5;
    uint64_t v8;
    v8 = hash(3.0);
    uint64_t v9;
    v9 = 9223372036854775807ull + v8;
    uint64_t v10;
    v10 = v9 * 9973ull;
    uint64_t v11;
    v11 = 1l;
    uint64_t v12;
    v12 = 1ull + v11;
    uint64_t v13;
    v13 = v10 * v12;
    int32_t v14;
    v14 = 1l;
    US0 v15;
    v15 = US0_0(v14);
    uint64_t v30;
    switch (v15.tag) {
        case 0: { // A
            int32_t v16 = v15.case0.v0;
            uint64_t v17;
            v17 = hash(v16);
            uint64_t v18;
            v18 = 9223372036854775807ull + v17;
            uint64_t v19;
            v19 = v18 * 9973ull;
            uint64_t v20;
            v20 = 0l;
            uint64_t v21;
            v21 = 1ull + v20;
            uint64_t v22;
            v22 = v19 * v21;
            v30 = v22;
            break;
        }
        case 1: { // B
            double v23 = v15.case1.v0;
            uint64_t v24;
            v24 = hash(v23);
            uint64_t v25;
            v25 = 9223372036854775807ull + v24;
            uint64_t v26;
            v26 = v25 * 9973ull;
            uint64_t v27;
            v27 = 1l;
            uint64_t v28;
            v28 = 1ull + v27;
            uint64_t v29;
            v29 = v26 * v28;
            v30 = v29;
            break;
        }
    }
    USRefc0(&(v15), REFC_DECR);
    double v31;
    v31 = 3.0;
    US0 v32;
    v32 = US0_1(v31);
    uint64_t v47;
    switch (v32.tag) {
        case 0: { // A
            int32_t v33 = v32.case0.v0;
            uint64_t v34;
            v34 = hash(v33);
            uint64_t v35;
            v35 = 9223372036854775807ull + v34;
            uint64_t v36;
            v36 = v35 * 9973ull;
            uint64_t v37;
            v37 = 0l;
            uint64_t v38;
            v38 = 1ull + v37;
            uint64_t v39;
            v39 = v36 * v38;
            v47 = v39;
            break;
        }
        case 1: { // B
            double v40 = v32.case1.v0;
            uint64_t v41;
            v41 = hash(v40);
            uint64_t v42;
            v42 = 9223372036854775807ull + v41;
            uint64_t v43;
            v43 = v42 * 9973ull;
            uint64_t v44;
            v44 = 1l;
            uint64_t v45;
            v45 = 1ull + v44;
            uint64_t v46;
            v46 = v43 * v45;
            v47 = v46;
            break;
        }
    }
    USRefc0(&(v32), REFC_DECR);
    int32_t v48;
    v48 = 3l;
    UH0 * v49;
    v49 = UH0_1();
    UH0 * v50;
    v50 = UH0_0(v48, v49);
    UHRefc0(v49, REFC_DECR);
    double v51;
    v51 = 2.0;
    double v52;
    v52 = 3.0;
    UH1 * v53;
    v53 = UH1_1();
    UH1 * v54;
    v54 = UH1_0(v52, v53);
    UHRefc1(v53, REFC_DECR);
    UH1 * v55;
    v55 = UH1_0(v51, v54);
    UHRefc1(v54, REFC_DECR);
    uint64_t v58;
    v58 = hash(1l);
    uint64_t v59;
    v59 = v58 * 9973ull;
    uint64_t v61;
    v61 = hash(2l);
    uint64_t v62;
    v62 = v61 * 9973ull;
    uint64_t v63;
    v63 = method0(v50);
    UHRefc0(v50, REFC_DECR);
    uint64_t v64;
    v64 = v62 + v63;
    uint64_t v65;
    v65 = 9223372036854775807ull + v64;
    uint64_t v66;
    v66 = v65 * 9973ull;
    uint64_t v67;
    v67 = 0l;
    uint64_t v68;
    v68 = 1ull + v67;
    uint64_t v69;
    v69 = v66 * v68;
    uint64_t v70;
    v70 = v59 + v69;
    uint64_t v71;
    v71 = 9223372036854775807ull + v70;
    uint64_t v72;
    v72 = v71 * 9973ull;
    uint64_t v73;
    v73 = 0l;
    uint64_t v74;
    v74 = 1ull + v73;
    uint64_t v75;
    v75 = v72 * v74;
    uint64_t v77;
    v77 = hash(1.0);
    uint64_t v78;
    v78 = v77 * 9973ull;
    uint64_t v79;
    v79 = method1(v55);
    UHRefc1(v55, REFC_DECR);
    uint64_t v80;
    v80 = v78 + v79;
    uint64_t v81;
    v81 = 9223372036854775807ull + v80;
    uint64_t v82;
    v82 = v81 * 9973ull;
    uint64_t v83;
    v83 = 0l;
    uint64_t v84;
    v84 = 1ull + v83;
    uint64_t v85;
    v85 = v82 * v84;
    return 0l;
}