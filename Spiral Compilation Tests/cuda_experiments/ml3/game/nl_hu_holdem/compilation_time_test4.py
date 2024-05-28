kernel = r"""
template <typename el, int dim> struct static_array { el v[dim]; };
template <typename el, int dim, typename default_int> struct static_array_list { el v[dim]; default_int length; };
#include <curand_kernel.h>
struct US0;
struct US1;
struct Tuple0;
__device__ US0 card_rank_untag_1(long v0);
__device__ US1 card_suit_untag_2(long v0);
__device__ Tuple0 card_untag_0(long v0);
__device__ long card_rank_tag_4(US0 v0);
__device__ long card_suit_tag_5(US1 v0);
__device__ long card_tag_3(US1 v0, US0 v1);
struct US2;
struct US4;
struct Tuple1;
struct US3;
struct US5;
struct US8;
struct US7;
struct US6;
struct US9;
struct Tuple2;
struct Tuple3;
struct Tuple4;
struct Tuple5;
struct Tuple6;
__device__ unsigned long loop_10(unsigned long v0, curandStatePhilox4_32_10_t & v1);
__device__ Tuple6 draw_card_9(curandStatePhilox4_32_10_t & v0, unsigned long long v1);
__device__ Tuple4 draw_cards_8(curandStatePhilox4_32_10_t & v0, unsigned long long v1);
__device__ static_array_list<unsigned char,5l,long> get_community_cards_11(US8 v0, static_array<unsigned char,3l> v1);
struct Tuple7;
__device__ bool player_can_act_13(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5);
__device__ US7 go_next_street_14(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5);
__device__ US7 try_round_12(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5);
struct Tuple8;
__device__ Tuple8 draw_cards_15(curandStatePhilox4_32_10_t & v0, unsigned long long v1);
struct Tuple9;
__device__ Tuple9 draw_cards_16(curandStatePhilox4_32_10_t & v0, unsigned long long v1);
__device__ static_array_list<unsigned char,5l,long> get_community_cards_17(US8 v0, static_array<unsigned char,1l> v1);
struct Tuple10;
__device__ long loop_20(static_array<float,6l> v0, float v1, long v2);
__device__ long sample_discrete__19(static_array<float,6l> v0, curandStatePhilox4_32_10_t & v1);
__device__ US4 sample_discrete_18(static_array<Tuple10,6l> v0, curandStatePhilox4_32_10_t & v1);
struct Tuple11;
struct Tuple12;
struct US10;
struct Tuple13;
struct US11;
struct Tuple14;
struct Tuple15;
struct US12;
struct US13;
struct US14;
struct US15;
struct US16;
__device__ Tuple1 score_21(static_array<unsigned char,7l> v0);
__device__ US7 play_loop_inner_7(unsigned long long & v0, static_array_list<US3,128l,long> & v1, curandStatePhilox4_32_10_t & v2, static_array<US2,2l> v3, US7 v4);
__device__ Tuple2 play_loop_6(US6 v0, static_array<US2,2l> v1, US9 v2, unsigned long long & v3, static_array_list<US3,128l,long> & v4, curandStatePhilox4_32_10_t & v5, US7 v6);
__device__ void write_23(char v0);
__device__ void write_24();
__device__ void write_25(const char * v0);
__device__ void write_29(unsigned long long v0);
__device__ void write_28(unsigned long long v0);
__device__ void write_32();
__device__ void write_34(unsigned char v0);
__device__ void write_33(static_array_list<unsigned char,5l,long> v0);
__device__ void write_35();
__device__ void write_37(long v0);
__device__ void write_36(long v0, long v1);
__device__ void write_38();
__device__ void write_41();
__device__ void write_42();
__device__ void write_43();
__device__ void write_44();
__device__ void write_40(US4 v0);
__device__ void write_39(long v0, US4 v1);
__device__ void write_45();
__device__ void write_47(static_array<unsigned char,2l> v0);
__device__ void write_46(long v0, static_array<unsigned char,2l> v1);
__device__ void write_48();
__device__ void write_60(const char * v0, unsigned char v1);
__device__ void write_59(unsigned char v0, const char * v1, unsigned char v2);
__device__ void write_58(const char * v0, unsigned char v1, unsigned char v2);
__device__ void write_57(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3);
__device__ void write_56(const char * v0, unsigned char v1, unsigned char v2, unsigned char v3);
__device__ void write_55(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3, unsigned char v4);
__device__ void write_54(const char * v0, unsigned char v1, unsigned char v2, unsigned char v3, unsigned char v4);
__device__ void write_53(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3, unsigned char v4, unsigned char v5);
__device__ void write_61(char v0);
__device__ void write_52(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3, unsigned char v4, unsigned char v5, char v6);
__device__ void write_51(static_array<unsigned char,5l> v0, char v1);
__device__ void write_50(static_array<Tuple1,2l> v0);
__device__ void write_49(long v0, static_array<Tuple1,2l> v1, long v2);
__device__ void write_31(US3 v0);
__device__ void write_30(static_array_list<US3,128l,long> v0);
__device__ void write_27(unsigned long long v0, static_array_list<US3,128l,long> v1);
__device__ void write_64();
__device__ void write_65();
__device__ void write_67();
__device__ void write_69(static_array<static_array<unsigned char,2l>,2l> v0);
__device__ void write_70(static_array<long,2l> v0);
__device__ void write_72();
__device__ void write_73(static_array<unsigned char,3l> v0);
__device__ void write_74();
__device__ void write_75();
__device__ void write_76(static_array<unsigned char,5l> v0);
__device__ void write_77();
__device__ void write_78(static_array<unsigned char,4l> v0);
__device__ void write_71(US8 v0);
__device__ void write_68(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5);
__device__ void write_79();
__device__ void write_80();
__device__ void write_81();
__device__ void write_82();
__device__ void write_83();
__device__ void write_84(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5, US4 v6);
__device__ void write_85();
__device__ void write_86();
__device__ void write_66(US7 v0);
__device__ void write_63(US6 v0);
__device__ void write_89();
__device__ void write_90();
__device__ void write_88(US2 v0);
__device__ void write_87(static_array<US2,2l> v0);
__device__ void write_92();
__device__ void write_93();
__device__ void write_94();
__device__ void write_91(US9 v0);
__device__ void write_62(US6 v0, static_array<US2,2l> v1, US9 v2);
__device__ void write_26(unsigned long long v0, static_array_list<US3,128l,long> v1, US6 v2, static_array<US2,2l> v3, US9 v4);
__device__ void write_22(unsigned long long v0, static_array_list<US3,128l,long> v1, US6 v2, static_array<US2,2l> v3, US9 v4);
struct US0 {
    union {
    } v;
    unsigned char tag;
};
struct US1 {
    union {
    } v;
    unsigned char tag;
};
struct Tuple0 {
    US0 v0;
    US1 v1;
    __device__ Tuple0(US0 t0, US1 t1) : v0(t0), v1(t1) {}
    __device__ Tuple0() = default;
};
struct US2 {
    union {
    } v;
    unsigned char tag;
};
struct US4 {
    union {
        struct {
            long v0;
        } case3; // A_Raise
    } v;
    unsigned char tag;
};
struct Tuple1 {
    static_array<unsigned char,5l> v0;
    char v1;
    __device__ Tuple1(static_array<unsigned char,5l> t0, char t1) : v0(t0), v1(t1) {}
    __device__ Tuple1() = default;
};
struct US3 {
    union {
        struct {
            static_array_list<unsigned char,5l,long> v0;
        } case0; // CommunityCardsAre
        struct {
            long v0;
            long v1;
        } case1; // Fold
        struct {
            US4 v1;
            long v0;
        } case2; // PlayerAction
        struct {
            static_array<unsigned char,2l> v1;
            long v0;
        } case3; // PlayerGotCards
        struct {
            static_array<Tuple1,2l> v1;
            long v0;
            long v2;
        } case4; // Showdown
    } v;
    unsigned char tag;
};
struct US5 {
    union {
        struct {
            US4 v0;
        } case0; // ActionSelected
        struct {
            static_array<US2,2l> v0;
        } case1; // PlayerChanged
    } v;
    unsigned char tag;
};
struct US8 {
    union {
        struct {
            static_array<unsigned char,3l> v0;
        } case0; // Flop
        struct {
            static_array<unsigned char,5l> v0;
        } case2; // River
        struct {
            static_array<unsigned char,4l> v0;
        } case3; // Turn
    } v;
    unsigned char tag;
};
struct US7 {
    union {
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case0; // G_Flop
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case1; // G_Fold
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case3; // G_River
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case4; // G_Round
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            US4 v6;
            long v0;
            long v3;
        } case5; // G_Round'
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case6; // G_Showdown
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case7; // G_Turn
    } v;
    unsigned char tag;
};
struct US6 {
    union {
        struct {
            US7 v0;
        } case1; // Some
    } v;
    unsigned char tag;
};
struct US9 {
    union {
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case1; // GameOver
        struct {
            static_array<static_array<unsigned char,2l>,2l> v1;
            static_array<long,2l> v2;
            static_array<long,2l> v4;
            US8 v5;
            long v0;
            long v3;
        } case2; // WaitingForActionFromPlayerId
    } v;
    unsigned char tag;
};
struct Tuple2 {
    US6 v0;
    static_array<US2,2l> v1;
    US9 v2;
    __device__ Tuple2(US6 t0, static_array<US2,2l> t1, US9 t2) : v0(t0), v1(t1), v2(t2) {}
    __device__ Tuple2() = default;
};
struct Tuple3 {
    US7 v1;
    bool v0;
    __device__ Tuple3(bool t0, US7 t1) : v0(t0), v1(t1) {}
    __device__ Tuple3() = default;
};
struct Tuple4 {
    static_array<unsigned char,3l> v0;
    unsigned long long v1;
    __device__ Tuple4(static_array<unsigned char,3l> t0, unsigned long long t1) : v0(t0), v1(t1) {}
    __device__ Tuple4() = default;
};
struct Tuple5 {
    unsigned long long v1;
    long v0;
    __device__ Tuple5(long t0, unsigned long long t1) : v0(t0), v1(t1) {}
    __device__ Tuple5() = default;
};
struct Tuple6 {
    unsigned long long v1;
    unsigned char v0;
    __device__ Tuple6(unsigned char t0, unsigned long long t1) : v0(t0), v1(t1) {}
    __device__ Tuple6() = default;
};
struct Tuple7 {
    long v0;
    long v1;
    __device__ Tuple7(long t0, long t1) : v0(t0), v1(t1) {}
    __device__ Tuple7() = default;
};
struct Tuple8 {
    static_array<unsigned char,2l> v0;
    unsigned long long v1;
    __device__ Tuple8(static_array<unsigned char,2l> t0, unsigned long long t1) : v0(t0), v1(t1) {}
    __device__ Tuple8() = default;
};
struct Tuple9 {
    static_array<unsigned char,1l> v0;
    unsigned long long v1;
    __device__ Tuple9(static_array<unsigned char,1l> t0, unsigned long long t1) : v0(t0), v1(t1) {}
    __device__ Tuple9() = default;
};
struct Tuple10 {
    US4 v0;
    float v1;
    __device__ Tuple10(US4 t0, float t1) : v0(t0), v1(t1) {}
    __device__ Tuple10() = default;
};
struct Tuple11 {
    long v1;
    bool v0;
    __device__ Tuple11(bool t0, long t1) : v0(t0), v1(t1) {}
    __device__ Tuple11() = default;
};
struct Tuple12 {
    long v0;
    long v1;
    long v2;
    __device__ Tuple12(long t0, long t1, long t2) : v0(t0), v1(t1), v2(t2) {}
    __device__ Tuple12() = default;
};
struct US10 {
    union {
    } v;
    unsigned char tag;
};
struct Tuple13 {
    long v0;
    long v1;
    unsigned char v2;
    __device__ Tuple13(long t0, long t1, unsigned char t2) : v0(t0), v1(t1), v2(t2) {}
    __device__ Tuple13() = default;
};
struct US11 {
    union {
        struct {
            static_array<unsigned char,5l> v0;
        } case1; // Some
    } v;
    unsigned char tag;
};
struct Tuple14 {
    US10 v1;
    long v0;
    __device__ Tuple14(long t0, US10 t1) : v0(t0), v1(t1) {}
    __device__ Tuple14() = default;
};
struct Tuple15 {
    long v0;
    long v1;
    long v2;
    unsigned char v3;
    __device__ Tuple15(long t0, long t1, long t2, unsigned char t3) : v0(t0), v1(t1), v2(t2), v3(t3) {}
    __device__ Tuple15() = default;
};
struct US12 {
    union {
        struct {
            static_array<unsigned char,4l> v0;
            static_array<unsigned char,3l> v1;
        } case1; // Some
    } v;
    unsigned char tag;
};
struct US13 {
    union {
        struct {
            static_array<unsigned char,3l> v0;
            static_array<unsigned char,4l> v1;
        } case1; // Some
    } v;
    unsigned char tag;
};
struct US14 {
    union {
        struct {
            static_array<unsigned char,2l> v0;
            static_array<unsigned char,2l> v1;
        } case1; // Some
    } v;
    unsigned char tag;
};
struct US15 {
    union {
        struct {
            static_array<unsigned char,2l> v0;
            static_array<unsigned char,5l> v1;
        } case1; // Some
    } v;
    unsigned char tag;
};
struct US16 {
    union {
        struct {
            static_array<unsigned char,2l> v0;
            static_array<unsigned char,3l> v1;
        } case1; // Some
    } v;
    unsigned char tag;
};
__device__ US0 US0_0() { // Ace
    US0 x;
    x.tag = 0;
    return x;
}
__device__ US0 US0_1() { // Eight
    US0 x;
    x.tag = 1;
    return x;
}
__device__ US0 US0_2() { // Five
    US0 x;
    x.tag = 2;
    return x;
}
__device__ US0 US0_3() { // Four
    US0 x;
    x.tag = 3;
    return x;
}
__device__ US0 US0_4() { // Jack
    US0 x;
    x.tag = 4;
    return x;
}
__device__ US0 US0_5() { // King
    US0 x;
    x.tag = 5;
    return x;
}
__device__ US0 US0_6() { // Nine
    US0 x;
    x.tag = 6;
    return x;
}
__device__ US0 US0_7() { // Queen
    US0 x;
    x.tag = 7;
    return x;
}
__device__ US0 US0_8() { // Seven
    US0 x;
    x.tag = 8;
    return x;
}
__device__ US0 US0_9() { // Six
    US0 x;
    x.tag = 9;
    return x;
}
__device__ US0 US0_10() { // Ten
    US0 x;
    x.tag = 10;
    return x;
}
__device__ US0 US0_11() { // Three
    US0 x;
    x.tag = 11;
    return x;
}
__device__ US0 US0_12() { // Two
    US0 x;
    x.tag = 12;
    return x;
}
__device__ US1 US1_0() { // Clubs
    US1 x;
    x.tag = 0;
    return x;
}
__device__ US1 US1_1() { // Diamonds
    US1 x;
    x.tag = 1;
    return x;
}
__device__ US1 US1_2() { // Hearts
    US1 x;
    x.tag = 2;
    return x;
}
__device__ US1 US1_3() { // Spades
    US1 x;
    x.tag = 3;
    return x;
}
__device__ US0 card_rank_untag_1(long v0){
    bool v1;
    v1 = 12l == v0;
    if (v1){
        return US0_0();
    } else {
        bool v3;
        v3 = 11l == v0;
        if (v3){
            return US0_5();
        } else {
            bool v5;
            v5 = 10l == v0;
            if (v5){
                return US0_7();
            } else {
                bool v7;
                v7 = 9l == v0;
                if (v7){
                    return US0_4();
                } else {
                    bool v9;
                    v9 = 8l == v0;
                    if (v9){
                        return US0_10();
                    } else {
                        bool v11;
                        v11 = 7l == v0;
                        if (v11){
                            return US0_6();
                        } else {
                            bool v13;
                            v13 = 6l == v0;
                            if (v13){
                                return US0_1();
                            } else {
                                bool v15;
                                v15 = 5l == v0;
                                if (v15){
                                    return US0_8();
                                } else {
                                    bool v17;
                                    v17 = 4l == v0;
                                    if (v17){
                                        return US0_9();
                                    } else {
                                        bool v19;
                                        v19 = 3l == v0;
                                        if (v19){
                                            return US0_2();
                                        } else {
                                            bool v21;
                                            v21 = 2l == v0;
                                            if (v21){
                                                return US0_3();
                                            } else {
                                                bool v23;
                                                v23 = 1l == v0;
                                                if (v23){
                                                    return US0_11();
                                                } else {
                                                    bool v25;
                                                    v25 = 0l == v0;
                                                    if (v25){
                                                        return US0_12();
                                                    } else {
                                                        printf("%s\n", "Invalid tag in card_rank_untag");
                                                        asm("exit;");
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
__device__ US1 card_suit_untag_2(long v0){
    bool v1;
    v1 = 3l == v0;
    if (v1){
        return US1_2();
    } else {
        bool v3;
        v3 = 2l == v0;
        if (v3){
            return US1_3();
        } else {
            bool v5;
            v5 = 1l == v0;
            if (v5){
                return US1_0();
            } else {
                bool v7;
                v7 = 0l == v0;
                if (v7){
                    return US1_1();
                } else {
                    printf("%s\n", "Invalid tag in card_suit_untag");
                    asm("exit;");
                }
            }
        }
    }
}
__device__ Tuple0 card_untag_0(long v0){
    long v1;
    v1 = v0 / 4l;
    US0 v2;
    v2 = card_rank_untag_1(v1);
    long v3;
    v3 = v0 % 4l;
    US1 v4;
    v4 = card_suit_untag_2(v3);
    return Tuple0(v2, v4);
}
__device__ long card_rank_tag_4(US0 v0){
    switch (v0.tag) {
        case 0: { // Ace
            return 12l;
            break;
        }
        case 1: { // Eight
            return 6l;
            break;
        }
        case 2: { // Five
            return 3l;
            break;
        }
        case 3: { // Four
            return 2l;
            break;
        }
        case 4: { // Jack
            return 9l;
            break;
        }
        case 5: { // King
            return 11l;
            break;
        }
        case 6: { // Nine
            return 7l;
            break;
        }
        case 7: { // Queen
            return 10l;
            break;
        }
        case 8: { // Seven
            return 5l;
            break;
        }
        case 9: { // Six
            return 4l;
            break;
        }
        case 10: { // Ten
            return 8l;
            break;
        }
        case 11: { // Three
            return 1l;
            break;
        }
        case 12: { // Two
            return 0l;
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ long card_suit_tag_5(US1 v0){
    switch (v0.tag) {
        case 0: { // Clubs
            return 1l;
            break;
        }
        case 1: { // Diamonds
            return 0l;
            break;
        }
        case 2: { // Hearts
            return 3l;
            break;
        }
        case 3: { // Spades
            return 2l;
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ long card_tag_3(US1 v0, US0 v1){
    long v2;
    v2 = card_rank_tag_4(v1);
    long v3;
    v3 = v2 * 4l;
    long v4;
    v4 = card_suit_tag_5(v0);
    long v5;
    v5 = v3 + v4;
    return v5;
}
__device__ US2 US2_0() { // Computer
    US2 x;
    x.tag = 0;
    return x;
}
__device__ US2 US2_1() { // Human
    US2 x;
    x.tag = 1;
    return x;
}
__device__ US4 US4_0() { // A_All_In
    US4 x;
    x.tag = 0;
    return x;
}
__device__ US4 US4_1() { // A_Call
    US4 x;
    x.tag = 1;
    return x;
}
__device__ US4 US4_2() { // A_Fold
    US4 x;
    x.tag = 2;
    return x;
}
__device__ US4 US4_3(long v0) { // A_Raise
    US4 x;
    x.tag = 3;
    x.v.case3.v0 = v0;
    return x;
}
__device__ US3 US3_0(static_array_list<unsigned char,5l,long> v0) { // CommunityCardsAre
    US3 x;
    x.tag = 0;
    x.v.case0.v0 = v0;
    return x;
}
__device__ US3 US3_1(long v0, long v1) { // Fold
    US3 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1;
    return x;
}
__device__ US3 US3_2(long v0, US4 v1) { // PlayerAction
    US3 x;
    x.tag = 2;
    x.v.case2.v0 = v0; x.v.case2.v1 = v1;
    return x;
}
__device__ US3 US3_3(long v0, static_array<unsigned char,2l> v1) { // PlayerGotCards
    US3 x;
    x.tag = 3;
    x.v.case3.v0 = v0; x.v.case3.v1 = v1;
    return x;
}
__device__ US3 US3_4(long v0, static_array<Tuple1,2l> v1, long v2) { // Showdown
    US3 x;
    x.tag = 4;
    x.v.case4.v0 = v0; x.v.case4.v1 = v1; x.v.case4.v2 = v2;
    return x;
}
__device__ US5 US5_0(US4 v0) { // ActionSelected
    US5 x;
    x.tag = 0;
    x.v.case0.v0 = v0;
    return x;
}
__device__ US5 US5_1(static_array<US2,2l> v0) { // PlayerChanged
    US5 x;
    x.tag = 1;
    x.v.case1.v0 = v0;
    return x;
}
__device__ US5 US5_2() { // StartGame
    US5 x;
    x.tag = 2;
    return x;
}
__device__ US8 US8_0(static_array<unsigned char,3l> v0) { // Flop
    US8 x;
    x.tag = 0;
    x.v.case0.v0 = v0;
    return x;
}
__device__ US8 US8_1() { // Preflop
    US8 x;
    x.tag = 1;
    return x;
}
__device__ US8 US8_2(static_array<unsigned char,5l> v0) { // River
    US8 x;
    x.tag = 2;
    x.v.case2.v0 = v0;
    return x;
}
__device__ US8 US8_3(static_array<unsigned char,4l> v0) { // Turn
    US8 x;
    x.tag = 3;
    x.v.case3.v0 = v0;
    return x;
}
__device__ US7 US7_0(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // G_Flop
    US7 x;
    x.tag = 0;
    x.v.case0.v0 = v0; x.v.case0.v1 = v1; x.v.case0.v2 = v2; x.v.case0.v3 = v3; x.v.case0.v4 = v4; x.v.case0.v5 = v5;
    return x;
}
__device__ US7 US7_1(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // G_Fold
    US7 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1; x.v.case1.v2 = v2; x.v.case1.v3 = v3; x.v.case1.v4 = v4; x.v.case1.v5 = v5;
    return x;
}
__device__ US7 US7_2() { // G_Preflop
    US7 x;
    x.tag = 2;
    return x;
}
__device__ US7 US7_3(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // G_River
    US7 x;
    x.tag = 3;
    x.v.case3.v0 = v0; x.v.case3.v1 = v1; x.v.case3.v2 = v2; x.v.case3.v3 = v3; x.v.case3.v4 = v4; x.v.case3.v5 = v5;
    return x;
}
__device__ US7 US7_4(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // G_Round
    US7 x;
    x.tag = 4;
    x.v.case4.v0 = v0; x.v.case4.v1 = v1; x.v.case4.v2 = v2; x.v.case4.v3 = v3; x.v.case4.v4 = v4; x.v.case4.v5 = v5;
    return x;
}
__device__ US7 US7_5(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5, US4 v6) { // G_Round'
    US7 x;
    x.tag = 5;
    x.v.case5.v0 = v0; x.v.case5.v1 = v1; x.v.case5.v2 = v2; x.v.case5.v3 = v3; x.v.case5.v4 = v4; x.v.case5.v5 = v5; x.v.case5.v6 = v6;
    return x;
}
__device__ US7 US7_6(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // G_Showdown
    US7 x;
    x.tag = 6;
    x.v.case6.v0 = v0; x.v.case6.v1 = v1; x.v.case6.v2 = v2; x.v.case6.v3 = v3; x.v.case6.v4 = v4; x.v.case6.v5 = v5;
    return x;
}
__device__ US7 US7_7(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // G_Turn
    US7 x;
    x.tag = 7;
    x.v.case7.v0 = v0; x.v.case7.v1 = v1; x.v.case7.v2 = v2; x.v.case7.v3 = v3; x.v.case7.v4 = v4; x.v.case7.v5 = v5;
    return x;
}
__device__ US6 US6_0() { // None
    US6 x;
    x.tag = 0;
    return x;
}
__device__ US6 US6_1(US7 v0) { // Some
    US6 x;
    x.tag = 1;
    x.v.case1.v0 = v0;
    return x;
}
__device__ US9 US9_0() { // GameNotStarted
    US9 x;
    x.tag = 0;
    return x;
}
__device__ US9 US9_1(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // GameOver
    US9 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1; x.v.case1.v2 = v2; x.v.case1.v3 = v3; x.v.case1.v4 = v4; x.v.case1.v5 = v5;
    return x;
}
__device__ US9 US9_2(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5) { // WaitingForActionFromPlayerId
    US9 x;
    x.tag = 2;
    x.v.case2.v0 = v0; x.v.case2.v1 = v1; x.v.case2.v2 = v2; x.v.case2.v3 = v3; x.v.case2.v4 = v4; x.v.case2.v5 = v5;
    return x;
}
__device__ inline bool while_method_0(bool v0, US7 v1){
    return v0;
}
__device__ inline bool while_method_1(long v0){
    bool v1;
    v1 = v0 < 3l;
    return v1;
}
__device__ unsigned long loop_10(unsigned long v0, curandStatePhilox4_32_10_t & v1){
    unsigned long v2;
    v2 = curand(&v1);
    unsigned long v3;
    v3 = v2 % v0;
    unsigned long v4;
    v4 = v2 - v3;
    unsigned long v5;
    v5 = 0ul - v0;
    bool v6;
    v6 = v4 <= v5;
    if (v6){
        return v3;
    } else {
        return loop_10(v0, v1);
    }
}
__device__ Tuple6 draw_card_9(curandStatePhilox4_32_10_t & v0, unsigned long long v1){
    long v2;
    v2 = __popcll(v1);
    unsigned long v3;
    v3 = (unsigned long)v2;
    unsigned long v4;
    v4 = loop_10(v3, v0);
    long v5;
    v5 = (long)v4;
    unsigned long v6;
    v6 = (unsigned long)v1;
    unsigned long long v7;
    v7 = v1 >> 32l;
    unsigned long v8;
    v8 = (unsigned long)v7;
    long v9;
    v9 = __popc(v6);
    bool v10;
    v10 = v5 < v9;
    unsigned long v17;
    if (v10){
        long v11;
        v11 = v5 + 1l;
        unsigned long v12;
        v12 = __fns(v6,0ul,v11);
        v17 = v12;
    } else {
        long v13;
        v13 = v5 - v9;
        long v14;
        v14 = v13 + 1l;
        unsigned long v15;
        v15 = __fns(v8,0ul,v14);
        unsigned long v16;
        v16 = v15 + 32ul;
        v17 = v16;
    }
    unsigned char v18;
    v18 = (unsigned char)v17;
    long v19;
    v19 = (long)v17;
    unsigned long long v20;
    v20 = 1ull << v19;
    unsigned long long v21;
    v21 = v1 ^ v20;
    return Tuple6(v18, v21);
}
__device__ Tuple4 draw_cards_8(curandStatePhilox4_32_10_t & v0, unsigned long long v1){
    static_array<unsigned char,3l> v2;
    long v3; unsigned long long v4;
    Tuple5 tmp2 = Tuple5(0l, v1);
    v3 = tmp2.v0; v4 = tmp2.v1;
    while (while_method_1(v3)){
        unsigned char v6; unsigned long long v7;
        Tuple6 tmp3 = draw_card_9(v0, v4);
        v6 = tmp3.v0; v7 = tmp3.v1;
        bool v8;
        v8 = 0l <= v3;
        bool v10;
        if (v8){
            bool v9;
            v9 = v3 < 3l;
            v10 = v9;
        } else {
            v10 = false;
        }
        bool v11;
        v11 = v10 == false;
        if (v11){
            assert("The read index needs to be in range for the static array." && v10);
        } else {
        }
        v2.v[v3] = v6;
        v4 = v7;
        v3 += 1l ;
    }
    return Tuple4(v2, v4);
}
__device__ inline bool while_method_2(long v0){
    bool v1;
    v1 = v0 < 5l;
    return v1;
}
__device__ inline bool while_method_3(long v0){
    bool v1;
    v1 = v0 < 4l;
    return v1;
}
__device__ static_array_list<unsigned char,5l,long> get_community_cards_11(US8 v0, static_array<unsigned char,3l> v1){
    static_array_list<unsigned char,5l,long> v2;
    v2.length = 0;
    switch (v0.tag) {
        case 0: { // Flop
            static_array<unsigned char,3l> v3 = v0.v.case0.v0;
            long v4;
            v4 = 0l;
            while (while_method_1(v4)){
                bool v6;
                v6 = 0l <= v4;
                bool v8;
                if (v6){
                    bool v7;
                    v7 = v4 < 3l;
                    v8 = v7;
                } else {
                    v8 = false;
                }
                bool v9;
                v9 = v8 == false;
                if (v9){
                    assert("The read index needs to be in range for the static array." && v8);
                } else {
                }
                unsigned char v10;
                v10 = v3.v[v4];
                long v11;
                v11 = v2.length;
                bool v12;
                v12 = v11 < 5l;
                bool v13;
                v13 = v12 == false;
                if (v13){
                    assert("The length has to be less than the maximum length of the array." && v12);
                } else {
                }
                long v14;
                v14 = v11 + 1l;
                v2.length = v14;
                bool v15;
                v15 = 0l <= v11;
                bool v18;
                if (v15){
                    long v16;
                    v16 = v2.length;
                    bool v17;
                    v17 = v11 < v16;
                    v18 = v17;
                } else {
                    v18 = false;
                }
                bool v19;
                v19 = v18 == false;
                if (v19){
                    assert("The set index needs to be in range for the static array list." && v18);
                } else {
                }
                v2.v[v11] = v10;
                v4 += 1l ;
            }
            break;
        }
        case 1: { // Preflop
            break;
        }
        case 2: { // River
            static_array<unsigned char,5l> v37 = v0.v.case2.v0;
            long v38;
            v38 = 0l;
            while (while_method_2(v38)){
                bool v40;
                v40 = 0l <= v38;
                bool v42;
                if (v40){
                    bool v41;
                    v41 = v38 < 5l;
                    v42 = v41;
                } else {
                    v42 = false;
                }
                bool v43;
                v43 = v42 == false;
                if (v43){
                    assert("The read index needs to be in range for the static array." && v42);
                } else {
                }
                unsigned char v44;
                v44 = v37.v[v38];
                long v45;
                v45 = v2.length;
                bool v46;
                v46 = v45 < 5l;
                bool v47;
                v47 = v46 == false;
                if (v47){
                    assert("The length has to be less than the maximum length of the array." && v46);
                } else {
                }
                long v48;
                v48 = v45 + 1l;
                v2.length = v48;
                bool v49;
                v49 = 0l <= v45;
                bool v52;
                if (v49){
                    long v50;
                    v50 = v2.length;
                    bool v51;
                    v51 = v45 < v50;
                    v52 = v51;
                } else {
                    v52 = false;
                }
                bool v53;
                v53 = v52 == false;
                if (v53){
                    assert("The set index needs to be in range for the static array list." && v52);
                } else {
                }
                v2.v[v45] = v44;
                v38 += 1l ;
            }
            break;
        }
        case 3: { // Turn
            static_array<unsigned char,4l> v20 = v0.v.case3.v0;
            long v21;
            v21 = 0l;
            while (while_method_3(v21)){
                bool v23;
                v23 = 0l <= v21;
                bool v25;
                if (v23){
                    bool v24;
                    v24 = v21 < 4l;
                    v25 = v24;
                } else {
                    v25 = false;
                }
                bool v26;
                v26 = v25 == false;
                if (v26){
                    assert("The read index needs to be in range for the static array." && v25);
                } else {
                }
                unsigned char v27;
                v27 = v20.v[v21];
                long v28;
                v28 = v2.length;
                bool v29;
                v29 = v28 < 5l;
                bool v30;
                v30 = v29 == false;
                if (v30){
                    assert("The length has to be less than the maximum length of the array." && v29);
                } else {
                }
                long v31;
                v31 = v28 + 1l;
                v2.length = v31;
                bool v32;
                v32 = 0l <= v28;
                bool v35;
                if (v32){
                    long v33;
                    v33 = v2.length;
                    bool v34;
                    v34 = v28 < v33;
                    v35 = v34;
                } else {
                    v35 = false;
                }
                bool v36;
                v36 = v35 == false;
                if (v36){
                    assert("The set index needs to be in range for the static array list." && v35);
                } else {
                }
                v2.v[v28] = v27;
                v21 += 1l ;
            }
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
    long v54;
    v54 = 0l;
    while (while_method_1(v54)){
        bool v56;
        v56 = 0l <= v54;
        bool v58;
        if (v56){
            bool v57;
            v57 = v54 < 3l;
            v58 = v57;
        } else {
            v58 = false;
        }
        bool v59;
        v59 = v58 == false;
        if (v59){
            assert("The read index needs to be in range for the static array." && v58);
        } else {
        }
        unsigned char v60;
        v60 = v1.v[v54];
        long v61;
        v61 = v2.length;
        bool v62;
        v62 = v61 < 5l;
        bool v63;
        v63 = v62 == false;
        if (v63){
            assert("The length has to be less than the maximum length of the array." && v62);
        } else {
        }
        long v64;
        v64 = v61 + 1l;
        v2.length = v64;
        bool v65;
        v65 = 0l <= v61;
        bool v68;
        if (v65){
            long v66;
            v66 = v2.length;
            bool v67;
            v67 = v61 < v66;
            v68 = v67;
        } else {
            v68 = false;
        }
        bool v69;
        v69 = v68 == false;
        if (v69){
            assert("The set index needs to be in range for the static array list." && v68);
        } else {
        }
        v2.v[v61] = v60;
        v54 += 1l ;
    }
    return v2;
}
__device__ inline bool while_method_4(long v0){
    bool v1;
    v1 = v0 < 2l;
    return v1;
}
__device__ bool player_can_act_13(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5){
    long v6;
    v6 = v3 % 2l;
    bool v7;
    v7 = 0l <= v6;
    bool v9;
    if (v7){
        bool v8;
        v8 = v6 < 2l;
        v9 = v8;
    } else {
        v9 = false;
    }
    bool v10;
    v10 = v9 == false;
    if (v10){
        assert("The read index needs to be in range for the static array." && v9);
    } else {
    }
    long v11;
    v11 = v4.v[v6];
    bool v12;
    v12 = v11 > 0l;
    bool v14;
    if (v7){
        bool v13;
        v13 = v6 < 2l;
        v14 = v13;
    } else {
        v14 = false;
    }
    bool v15;
    v15 = v14 == false;
    if (v15){
        assert("The read index needs to be in range for the static array." && v14);
    } else {
    }
    long v16;
    v16 = v2.v[v6];
    long v17;
    v17 = v2.v[0l];
    long v18; long v19;
    Tuple7 tmp5 = Tuple7(1l, v17);
    v18 = tmp5.v0; v19 = tmp5.v1;
    while (while_method_4(v18)){
        bool v21;
        v21 = 0l <= v18;
        bool v23;
        if (v21){
            bool v22;
            v22 = v18 < 2l;
            v23 = v22;
        } else {
            v23 = false;
        }
        bool v24;
        v24 = v23 == false;
        if (v24){
            assert("The read index needs to be in range for the static array." && v23);
        } else {
        }
        long v25;
        v25 = v2.v[v18];
        bool v26;
        v26 = v19 >= v25;
        long v27;
        if (v26){
            v27 = v19;
        } else {
            v27 = v25;
        }
        v19 = v27;
        v18 += 1l ;
    }
    bool v28;
    v28 = v16 < v19;
    long v29; long v30;
    Tuple7 tmp6 = Tuple7(0l, 0l);
    v29 = tmp6.v0; v30 = tmp6.v1;
    while (while_method_4(v29)){
        bool v32;
        v32 = 0l <= v29;
        bool v34;
        if (v32){
            bool v33;
            v33 = v29 < 2l;
            v34 = v33;
        } else {
            v34 = false;
        }
        bool v35;
        v35 = v34 == false;
        if (v35){
            assert("The read index needs to be in range for the static array." && v34);
        } else {
        }
        long v36;
        v36 = v4.v[v29];
        bool v37;
        v37 = 0l < v36;
        long v38;
        if (v37){
            v38 = 1l;
        } else {
            v38 = 0l;
        }
        long v39;
        v39 = v30 + v38;
        v30 = v39;
        v29 += 1l ;
    }
    if (v12){
        if (v28){
            return true;
        } else {
            bool v40;
            v40 = v3 < 2l;
            if (v40){
                bool v41;
                v41 = 0l < v30;
                return v41;
            } else {
                return false;
            }
        }
    } else {
        return false;
    }
}
__device__ US7 go_next_street_14(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5){
    switch (v5.tag) {
        case 0: { // Flop
            static_array<unsigned char,3l> v7 = v5.v.case0.v0;
            return US7_7(v0, v1, v2, v3, v4, v5);
            break;
        }
        case 1: { // Preflop
            return US7_0(v0, v1, v2, v3, v4, v5);
            break;
        }
        case 2: { // River
            static_array<unsigned char,5l> v11 = v5.v.case2.v0;
            return US7_6(v0, v1, v2, v3, v4, v5);
            break;
        }
        case 3: { // Turn
            static_array<unsigned char,4l> v9 = v5.v.case3.v0;
            return US7_3(v0, v1, v2, v3, v4, v5);
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ US7 try_round_12(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5){
    long v6;
    v6 = v3 + 1l;
    bool v7;
    v7 = player_can_act_13(v0, v1, v2, v3, v4, v5);
    if (v7){
        return US7_4(v0, v1, v2, v3, v4, v5);
    } else {
        bool v9;
        v9 = player_can_act_13(v0, v1, v2, v6, v4, v5);
        if (v9){
            return US7_4(v0, v1, v2, v6, v4, v5);
        } else {
            return go_next_street_14(v0, v1, v2, v3, v4, v5);
        }
    }
}
__device__ Tuple8 draw_cards_15(curandStatePhilox4_32_10_t & v0, unsigned long long v1){
    static_array<unsigned char,2l> v2;
    long v3; unsigned long long v4;
    Tuple5 tmp7 = Tuple5(0l, v1);
    v3 = tmp7.v0; v4 = tmp7.v1;
    while (while_method_4(v3)){
        unsigned char v6; unsigned long long v7;
        Tuple6 tmp8 = draw_card_9(v0, v4);
        v6 = tmp8.v0; v7 = tmp8.v1;
        bool v8;
        v8 = 0l <= v3;
        bool v10;
        if (v8){
            bool v9;
            v9 = v3 < 2l;
            v10 = v9;
        } else {
            v10 = false;
        }
        bool v11;
        v11 = v10 == false;
        if (v11){
            assert("The read index needs to be in range for the static array." && v10);
        } else {
        }
        v2.v[v3] = v6;
        v4 = v7;
        v3 += 1l ;
    }
    return Tuple8(v2, v4);
}
__device__ inline bool while_method_5(long v0){
    bool v1;
    v1 = v0 < 1l;
    return v1;
}
__device__ Tuple9 draw_cards_16(curandStatePhilox4_32_10_t & v0, unsigned long long v1){
    static_array<unsigned char,1l> v2;
    long v3; unsigned long long v4;
    Tuple5 tmp11 = Tuple5(0l, v1);
    v3 = tmp11.v0; v4 = tmp11.v1;
    while (while_method_5(v3)){
        unsigned char v6; unsigned long long v7;
        Tuple6 tmp12 = draw_card_9(v0, v4);
        v6 = tmp12.v0; v7 = tmp12.v1;
        bool v8;
        v8 = 0l <= v3;
        bool v10;
        if (v8){
            bool v9;
            v9 = v3 < 1l;
            v10 = v9;
        } else {
            v10 = false;
        }
        bool v11;
        v11 = v10 == false;
        if (v11){
            assert("The read index needs to be in range for the static array." && v10);
        } else {
        }
        v2.v[v3] = v6;
        v4 = v7;
        v3 += 1l ;
    }
    return Tuple9(v2, v4);
}
__device__ static_array_list<unsigned char,5l,long> get_community_cards_17(US8 v0, static_array<unsigned char,1l> v1){
    static_array_list<unsigned char,5l,long> v2;
    v2.length = 0;
    switch (v0.tag) {
        case 0: { // Flop
            static_array<unsigned char,3l> v3 = v0.v.case0.v0;
            long v4;
            v4 = 0l;
            while (while_method_1(v4)){
                bool v6;
                v6 = 0l <= v4;
                bool v8;
                if (v6){
                    bool v7;
                    v7 = v4 < 3l;
                    v8 = v7;
                } else {
                    v8 = false;
                }
                bool v9;
                v9 = v8 == false;
                if (v9){
                    assert("The read index needs to be in range for the static array." && v8);
                } else {
                }
                unsigned char v10;
                v10 = v3.v[v4];
                long v11;
                v11 = v2.length;
                bool v12;
                v12 = v11 < 5l;
                bool v13;
                v13 = v12 == false;
                if (v13){
                    assert("The length has to be less than the maximum length of the array." && v12);
                } else {
                }
                long v14;
                v14 = v11 + 1l;
                v2.length = v14;
                bool v15;
                v15 = 0l <= v11;
                bool v18;
                if (v15){
                    long v16;
                    v16 = v2.length;
                    bool v17;
                    v17 = v11 < v16;
                    v18 = v17;
                } else {
                    v18 = false;
                }
                bool v19;
                v19 = v18 == false;
                if (v19){
                    assert("The set index needs to be in range for the static array list." && v18);
                } else {
                }
                v2.v[v11] = v10;
                v4 += 1l ;
            }
            break;
        }
        case 1: { // Preflop
            break;
        }
        case 2: { // River
            static_array<unsigned char,5l> v37 = v0.v.case2.v0;
            long v38;
            v38 = 0l;
            while (while_method_2(v38)){
                bool v40;
                v40 = 0l <= v38;
                bool v42;
                if (v40){
                    bool v41;
                    v41 = v38 < 5l;
                    v42 = v41;
                } else {
                    v42 = false;
                }
                bool v43;
                v43 = v42 == false;
                if (v43){
                    assert("The read index needs to be in range for the static array." && v42);
                } else {
                }
                unsigned char v44;
                v44 = v37.v[v38];
                long v45;
                v45 = v2.length;
                bool v46;
                v46 = v45 < 5l;
                bool v47;
                v47 = v46 == false;
                if (v47){
                    assert("The length has to be less than the maximum length of the array." && v46);
                } else {
                }
                long v48;
                v48 = v45 + 1l;
                v2.length = v48;
                bool v49;
                v49 = 0l <= v45;
                bool v52;
                if (v49){
                    long v50;
                    v50 = v2.length;
                    bool v51;
                    v51 = v45 < v50;
                    v52 = v51;
                } else {
                    v52 = false;
                }
                bool v53;
                v53 = v52 == false;
                if (v53){
                    assert("The set index needs to be in range for the static array list." && v52);
                } else {
                }
                v2.v[v45] = v44;
                v38 += 1l ;
            }
            break;
        }
        case 3: { // Turn
            static_array<unsigned char,4l> v20 = v0.v.case3.v0;
            long v21;
            v21 = 0l;
            while (while_method_3(v21)){
                bool v23;
                v23 = 0l <= v21;
                bool v25;
                if (v23){
                    bool v24;
                    v24 = v21 < 4l;
                    v25 = v24;
                } else {
                    v25 = false;
                }
                bool v26;
                v26 = v25 == false;
                if (v26){
                    assert("The read index needs to be in range for the static array." && v25);
                } else {
                }
                unsigned char v27;
                v27 = v20.v[v21];
                long v28;
                v28 = v2.length;
                bool v29;
                v29 = v28 < 5l;
                bool v30;
                v30 = v29 == false;
                if (v30){
                    assert("The length has to be less than the maximum length of the array." && v29);
                } else {
                }
                long v31;
                v31 = v28 + 1l;
                v2.length = v31;
                bool v32;
                v32 = 0l <= v28;
                bool v35;
                if (v32){
                    long v33;
                    v33 = v2.length;
                    bool v34;
                    v34 = v28 < v33;
                    v35 = v34;
                } else {
                    v35 = false;
                }
                bool v36;
                v36 = v35 == false;
                if (v36){
                    assert("The set index needs to be in range for the static array list." && v35);
                } else {
                }
                v2.v[v28] = v27;
                v21 += 1l ;
            }
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
    long v54;
    v54 = 0l;
    while (while_method_5(v54)){
        bool v56;
        v56 = 0l <= v54;
        bool v58;
        if (v56){
            bool v57;
            v57 = v54 < 1l;
            v58 = v57;
        } else {
            v58 = false;
        }
        bool v59;
        v59 = v58 == false;
        if (v59){
            assert("The read index needs to be in range for the static array." && v58);
        } else {
        }
        unsigned char v60;
        v60 = v1.v[v54];
        long v61;
        v61 = v2.length;
        bool v62;
        v62 = v61 < 5l;
        bool v63;
        v63 = v62 == false;
        if (v63){
            assert("The length has to be less than the maximum length of the array." && v62);
        } else {
        }
        long v64;
        v64 = v61 + 1l;
        v2.length = v64;
        bool v65;
        v65 = 0l <= v61;
        bool v68;
        if (v65){
            long v66;
            v66 = v2.length;
            bool v67;
            v67 = v61 < v66;
            v68 = v67;
        } else {
            v68 = false;
        }
        bool v69;
        v69 = v68 == false;
        if (v69){
            assert("The set index needs to be in range for the static array list." && v68);
        } else {
        }
        v2.v[v61] = v60;
        v54 += 1l ;
    }
    return v2;
}
__device__ inline bool while_method_6(long v0){
    bool v1;
    v1 = v0 < 6l;
    return v1;
}
__device__ inline bool while_method_7(static_array<float,6l> v0, long v1){
    bool v2;
    v2 = v1 < 6l;
    return v2;
}
__device__ inline bool while_method_8(long v0, long v1){
    bool v2;
    v2 = v1 > v0;
    return v2;
}
__device__ long loop_20(static_array<float,6l> v0, float v1, long v2){
    bool v3;
    v3 = v2 < 6l;
    if (v3){
        bool v4;
        v4 = 0l <= v2;
        bool v5;
        v5 = v4 && v3;
        bool v6;
        v6 = v5 == false;
        if (v6){
            assert("The read index needs to be in range for the static array." && v5);
        } else {
        }
        float v7;
        v7 = v0.v[v2];
        bool v8;
        v8 = v1 <= v7;
        if (v8){
            return v2;
        } else {
            long v9;
            v9 = v2 + 1l;
            return loop_20(v0, v1, v9);
        }
    } else {
        return 5l;
    }
}
__device__ long sample_discrete__19(static_array<float,6l> v0, curandStatePhilox4_32_10_t & v1){
    static_array<float,6l> v2;
    long v3;
    v3 = 0l;
    while (while_method_6(v3)){
        bool v5;
        v5 = 0l <= v3;
        bool v7;
        if (v5){
            bool v6;
            v6 = v3 < 6l;
            v7 = v6;
        } else {
            v7 = false;
        }
        bool v8;
        v8 = v7 == false;
        if (v8){
            assert("The read index needs to be in range for the static array." && v7);
        } else {
        }
        float v9;
        v9 = v0.v[v3];
        bool v11;
        if (v5){
            bool v10;
            v10 = v3 < 6l;
            v11 = v10;
        } else {
            v11 = false;
        }
        bool v12;
        v12 = v11 == false;
        if (v12){
            assert("The read index needs to be in range for the static array." && v11);
        } else {
        }
        v2.v[v3] = v9;
        v3 += 1l ;
    }
    long v13;
    v13 = 1l;
    while (while_method_7(v2, v13)){
        long v15;
        v15 = 6l;
        while (while_method_8(v13, v15)){
            v15 -= 1l ;
            long v17;
            v17 = v15 - v13;
            bool v18;
            v18 = 0l <= v17;
            bool v20;
            if (v18){
                bool v19;
                v19 = v17 < 6l;
                v20 = v19;
            } else {
                v20 = false;
            }
            bool v21;
            v21 = v20 == false;
            if (v21){
                assert("The read index needs to be in range for the static array." && v20);
            } else {
            }
            float v22;
            v22 = v2.v[v17];
            bool v23;
            v23 = 0l <= v15;
            bool v25;
            if (v23){
                bool v24;
                v24 = v15 < 6l;
                v25 = v24;
            } else {
                v25 = false;
            }
            bool v26;
            v26 = v25 == false;
            if (v26){
                assert("The read index needs to be in range for the static array." && v25);
            } else {
            }
            float v27;
            v27 = v2.v[v15];
            float v28;
            v28 = v22 + v27;
            bool v30;
            if (v23){
                bool v29;
                v29 = v15 < 6l;
                v30 = v29;
            } else {
                v30 = false;
            }
            bool v31;
            v31 = v30 == false;
            if (v31){
                assert("The read index needs to be in range for the static array." && v30);
            } else {
            }
            v2.v[v15] = v28;
        }
        long v32;
        v32 = v13 * 2l;
        v13 = v32;
    }
    float v33;
    v33 = v2.v[5l];
    float v34;
    v34 = curand_uniform(&v1);
    float v35;
    v35 = v34 * v33;
    long v36;
    v36 = 0l;
    return loop_20(v2, v35, v36);
}
__device__ US4 sample_discrete_18(static_array<Tuple10,6l> v0, curandStatePhilox4_32_10_t & v1){
    static_array<float,6l> v2;
    long v3;
    v3 = 0l;
    while (while_method_6(v3)){
        bool v5;
        v5 = 0l <= v3;
        bool v7;
        if (v5){
            bool v6;
            v6 = v3 < 6l;
            v7 = v6;
        } else {
            v7 = false;
        }
        bool v8;
        v8 = v7 == false;
        if (v8){
            assert("The read index needs to be in range for the static array." && v7);
        } else {
        }
        US4 v9; float v10;
        Tuple10 tmp16 = v0.v[v3];
        v9 = tmp16.v0; v10 = tmp16.v1;
        bool v12;
        if (v5){
            bool v11;
            v11 = v3 < 6l;
            v12 = v11;
        } else {
            v12 = false;
        }
        bool v13;
        v13 = v12 == false;
        if (v13){
            assert("The read index needs to be in range for the static array." && v12);
        } else {
        }
        v2.v[v3] = v10;
        v3 += 1l ;
    }
    long v14;
    v14 = sample_discrete__19(v2, v1);
    bool v15;
    v15 = 0l <= v14;
    bool v17;
    if (v15){
        bool v16;
        v16 = v14 < 6l;
        v17 = v16;
    } else {
        v17 = false;
    }
    bool v18;
    v18 = v17 == false;
    if (v18){
        assert("The read index needs to be in range for the static array." && v17);
    } else {
    }
    US4 v19; float v20;
    Tuple10 tmp17 = v0.v[v14];
    v19 = tmp17.v0; v20 = tmp17.v1;
    return v19;
}
__device__ inline bool while_method_9(long v0){
    bool v1;
    v1 = v0 < 7l;
    return v1;
}
__device__ inline bool while_method_10(static_array<unsigned char,7l> v0, bool v1, long v2){
    bool v3;
    v3 = v2 < 7l;
    return v3;
}
__device__ inline bool while_method_11(static_array<unsigned char,7l> v0, long v1){
    bool v2;
    v2 = v1 < 7l;
    return v2;
}
__device__ inline bool while_method_12(long v0, long v1, long v2, long v3){
    bool v4;
    v4 = v3 < v0;
    return v4;
}
__device__ US10 US10_0() { // Eq
    US10 x;
    x.tag = 0;
    return x;
}
__device__ US10 US10_1() { // Gt
    US10 x;
    x.tag = 1;
    return x;
}
__device__ US10 US10_2() { // Lt
    US10 x;
    x.tag = 2;
    return x;
}
__device__ US11 US11_0() { // None
    US11 x;
    x.tag = 0;
    return x;
}
__device__ US11 US11_1(static_array<unsigned char,5l> v0) { // Some
    US11 x;
    x.tag = 1;
    x.v.case1.v0 = v0;
    return x;
}
__device__ US12 US12_0() { // None
    US12 x;
    x.tag = 0;
    return x;
}
__device__ US12 US12_1(static_array<unsigned char,4l> v0, static_array<unsigned char,3l> v1) { // Some
    US12 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1;
    return x;
}
__device__ US13 US13_0() { // None
    US13 x;
    x.tag = 0;
    return x;
}
__device__ US13 US13_1(static_array<unsigned char,3l> v0, static_array<unsigned char,4l> v1) { // Some
    US13 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1;
    return x;
}
__device__ US14 US14_0() { // None
    US14 x;
    x.tag = 0;
    return x;
}
__device__ US14 US14_1(static_array<unsigned char,2l> v0, static_array<unsigned char,2l> v1) { // Some
    US14 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1;
    return x;
}
__device__ US15 US15_0() { // None
    US15 x;
    x.tag = 0;
    return x;
}
__device__ US15 US15_1(static_array<unsigned char,2l> v0, static_array<unsigned char,5l> v1) { // Some
    US15 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1;
    return x;
}
__device__ US16 US16_0() { // None
    US16 x;
    x.tag = 0;
    return x;
}
__device__ US16 US16_1(static_array<unsigned char,2l> v0, static_array<unsigned char,3l> v1) { // Some
    US16 x;
    x.tag = 1;
    x.v.case1.v0 = v0; x.v.case1.v1 = v1;
    return x;
}
__device__ Tuple1 score_21(static_array<unsigned char,7l> v0){
    static_array<unsigned char,7l> v1;
    long v2;
    v2 = 0l;
    while (while_method_9(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 7l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        unsigned char v8;
        v8 = v0.v[v2];
        bool v10;
        if (v4){
            bool v9;
            v9 = v2 < 7l;
            v10 = v9;
        } else {
            v10 = false;
        }
        bool v11;
        v11 = v10 == false;
        if (v11){
            assert("The read index needs to be in range for the static array." && v10);
        } else {
        }
        v1.v[v2] = v8;
        v2 += 1l ;
    }
    static_array<unsigned char,7l> v12;
    bool v13; long v14;
    Tuple11 tmp24 = Tuple11(true, 1l);
    v13 = tmp24.v0; v14 = tmp24.v1;
    while (while_method_10(v1, v13, v14)){
        long v16;
        v16 = 0l;
        while (while_method_11(v1, v16)){
            long v18;
            v18 = v16 + v14;
            bool v19;
            v19 = v18 < 7l;
            long v20;
            if (v19){
                v20 = v18;
            } else {
                v20 = 7l;
            }
            long v21;
            v21 = v14 * 2l;
            long v22;
            v22 = v16 + v21;
            bool v23;
            v23 = v22 < 7l;
            long v24;
            if (v23){
                v24 = v22;
            } else {
                v24 = 7l;
            }
            long v25; long v26; long v27;
            Tuple12 tmp25 = Tuple12(v16, v20, v16);
            v25 = tmp25.v0; v26 = tmp25.v1; v27 = tmp25.v2;
            while (while_method_12(v24, v25, v26, v27)){
                bool v29;
                v29 = v25 < v20;
                bool v31;
                if (v29){
                    bool v30;
                    v30 = v26 < v24;
                    v31 = v30;
                } else {
                    v31 = false;
                }
                unsigned char v105; long v106; long v107;
                if (v31){
                    unsigned char v42;
                    if (v13){
                        bool v32;
                        v32 = 0l <= v25;
                        bool v34;
                        if (v32){
                            bool v33;
                            v33 = v25 < 7l;
                            v34 = v33;
                        } else {
                            v34 = false;
                        }
                        bool v35;
                        v35 = v34 == false;
                        if (v35){
                            assert("The read index needs to be in range for the static array." && v34);
                        } else {
                        }
                        unsigned char v36;
                        v36 = v1.v[v25];
                        v42 = v36;
                    } else {
                        bool v37;
                        v37 = 0l <= v25;
                        bool v39;
                        if (v37){
                            bool v38;
                            v38 = v25 < 7l;
                            v39 = v38;
                        } else {
                            v39 = false;
                        }
                        bool v40;
                        v40 = v39 == false;
                        if (v40){
                            assert("The read index needs to be in range for the static array." && v39);
                        } else {
                        }
                        unsigned char v41;
                        v41 = v12.v[v25];
                        v42 = v41;
                    }
                    unsigned char v53;
                    if (v13){
                        bool v43;
                        v43 = 0l <= v26;
                        bool v45;
                        if (v43){
                            bool v44;
                            v44 = v26 < 7l;
                            v45 = v44;
                        } else {
                            v45 = false;
                        }
                        bool v46;
                        v46 = v45 == false;
                        if (v46){
                            assert("The read index needs to be in range for the static array." && v45);
                        } else {
                        }
                        unsigned char v47;
                        v47 = v1.v[v26];
                        v53 = v47;
                    } else {
                        bool v48;
                        v48 = 0l <= v26;
                        bool v50;
                        if (v48){
                            bool v49;
                            v49 = v26 < 7l;
                            v50 = v49;
                        } else {
                            v50 = false;
                        }
                        bool v51;
                        v51 = v50 == false;
                        if (v51){
                            assert("The read index needs to be in range for the static array." && v50);
                        } else {
                        }
                        unsigned char v52;
                        v52 = v12.v[v26];
                        v53 = v52;
                    }
                    unsigned char v54;
                    v54 = v53 / 4u;
                    unsigned char v55;
                    v55 = v42 / 4u;
                    bool v56;
                    v56 = v54 < v55;
                    US10 v62;
                    if (v56){
                        v62 = US10_2();
                    } else {
                        bool v58;
                        v58 = v54 > v55;
                        if (v58){
                            v62 = US10_1();
                        } else {
                            v62 = US10_0();
                        }
                    }
                    US10 v72;
                    switch (v62.tag) {
                        case 0: { // Eq
                            unsigned char v63;
                            v63 = v42 % 4u;
                            unsigned char v64;
                            v64 = v53 % 4u;
                            bool v65;
                            v65 = v63 < v64;
                            if (v65){
                                v72 = US10_2();
                            } else {
                                bool v67;
                                v67 = v63 > v64;
                                if (v67){
                                    v72 = US10_1();
                                } else {
                                    v72 = US10_0();
                                }
                            }
                            break;
                        }
                        default: {
                            v72 = v62;
                        }
                    }
                    switch (v72.tag) {
                        case 1: { // Gt
                            long v73;
                            v73 = v26 + 1l;
                            v105 = v53; v106 = v25; v107 = v73;
                            break;
                        }
                        default: {
                            long v74;
                            v74 = v25 + 1l;
                            v105 = v42; v106 = v74; v107 = v26;
                        }
                    }
                } else {
                    if (v29){
                        unsigned char v88;
                        if (v13){
                            bool v78;
                            v78 = 0l <= v25;
                            bool v80;
                            if (v78){
                                bool v79;
                                v79 = v25 < 7l;
                                v80 = v79;
                            } else {
                                v80 = false;
                            }
                            bool v81;
                            v81 = v80 == false;
                            if (v81){
                                assert("The read index needs to be in range for the static array." && v80);
                            } else {
                            }
                            unsigned char v82;
                            v82 = v1.v[v25];
                            v88 = v82;
                        } else {
                            bool v83;
                            v83 = 0l <= v25;
                            bool v85;
                            if (v83){
                                bool v84;
                                v84 = v25 < 7l;
                                v85 = v84;
                            } else {
                                v85 = false;
                            }
                            bool v86;
                            v86 = v85 == false;
                            if (v86){
                                assert("The read index needs to be in range for the static array." && v85);
                            } else {
                            }
                            unsigned char v87;
                            v87 = v12.v[v25];
                            v88 = v87;
                        }
                        long v89;
                        v89 = v25 + 1l;
                        v105 = v88; v106 = v89; v107 = v26;
                    } else {
                        unsigned char v100;
                        if (v13){
                            bool v90;
                            v90 = 0l <= v26;
                            bool v92;
                            if (v90){
                                bool v91;
                                v91 = v26 < 7l;
                                v92 = v91;
                            } else {
                                v92 = false;
                            }
                            bool v93;
                            v93 = v92 == false;
                            if (v93){
                                assert("The read index needs to be in range for the static array." && v92);
                            } else {
                            }
                            unsigned char v94;
                            v94 = v1.v[v26];
                            v100 = v94;
                        } else {
                            bool v95;
                            v95 = 0l <= v26;
                            bool v97;
                            if (v95){
                                bool v96;
                                v96 = v26 < 7l;
                                v97 = v96;
                            } else {
                                v97 = false;
                            }
                            bool v98;
                            v98 = v97 == false;
                            if (v98){
                                assert("The read index needs to be in range for the static array." && v97);
                            } else {
                            }
                            unsigned char v99;
                            v99 = v12.v[v26];
                            v100 = v99;
                        }
                        long v101;
                        v101 = v26 + 1l;
                        v105 = v100; v106 = v25; v107 = v101;
                    }
                }
                if (v13){
                    bool v108;
                    v108 = 0l <= v27;
                    bool v110;
                    if (v108){
                        bool v109;
                        v109 = v27 < 7l;
                        v110 = v109;
                    } else {
                        v110 = false;
                    }
                    bool v111;
                    v111 = v110 == false;
                    if (v111){
                        assert("The read index needs to be in range for the static array." && v110);
                    } else {
                    }
                    v12.v[v27] = v105;
                } else {
                    bool v112;
                    v112 = 0l <= v27;
                    bool v114;
                    if (v112){
                        bool v113;
                        v113 = v27 < 7l;
                        v114 = v113;
                    } else {
                        v114 = false;
                    }
                    bool v115;
                    v115 = v114 == false;
                    if (v115){
                        assert("The read index needs to be in range for the static array." && v114);
                    } else {
                    }
                    v1.v[v27] = v105;
                }
                long v116;
                v116 = v27 + 1l;
                v25 = v106;
                v26 = v107;
                v27 = v116;
            }
            v16 = v22;
        }
        bool v117;
        v117 = v13 == false;
        long v118;
        v118 = v14 * 2l;
        v13 = v117;
        v14 = v118;
    }
    bool v119;
    v119 = v13 == false;
    static_array<unsigned char,7l> v120;
    if (v119){
        v120 = v12;
    } else {
        v120 = v1;
    }
    static_array<unsigned char,5l> v121;
    long v122; long v123; unsigned char v124;
    Tuple13 tmp26 = Tuple13(0l, 0l, 12u);
    v122 = tmp26.v0; v123 = tmp26.v1; v124 = tmp26.v2;
    while (while_method_9(v122)){
        bool v126;
        v126 = 0l <= v122;
        bool v128;
        if (v126){
            bool v127;
            v127 = v122 < 7l;
            v128 = v127;
        } else {
            v128 = false;
        }
        bool v129;
        v129 = v128 == false;
        if (v129){
            assert("The read index needs to be in range for the static array." && v128);
        } else {
        }
        unsigned char v130;
        v130 = v120.v[v122];
        bool v131;
        v131 = v123 < 5l;
        long v147; unsigned char v148;
        if (v131){
            unsigned char v132;
            v132 = v130 % 4u;
            bool v133;
            v133 = 0u == v132;
            if (v133){
                unsigned char v134;
                v134 = v130 / 4u;
                bool v135;
                v135 = v124 == v134;
                long v136;
                if (v135){
                    v136 = v123;
                } else {
                    v136 = 0l;
                }
                bool v137;
                v137 = 0l <= v136;
                bool v139;
                if (v137){
                    bool v138;
                    v138 = v136 < 5l;
                    v139 = v138;
                } else {
                    v139 = false;
                }
                bool v140;
                v140 = v139 == false;
                if (v140){
                    assert("The read index needs to be in range for the static array." && v139);
                } else {
                }
                v121.v[v136] = v130;
                long v141;
                v141 = v136 + 1l;
                unsigned char v142;
                v142 = v134 - 1u;
                v147 = v141; v148 = v142;
            } else {
                v147 = v123; v148 = v124;
            }
        } else {
            break;
        }
        v123 = v147;
        v124 = v148;
        v122 += 1l ;
    }
    bool v149;
    v149 = v123 == 4l;
    bool v184;
    if (v149){
        unsigned char v150;
        v150 = v124 + 1u;
        bool v151;
        v151 = v150 == 0u;
        if (v151){
            unsigned char v152;
            v152 = v120.v[0l];
            unsigned char v153;
            v153 = v152 % 4u;
            bool v154;
            v154 = 0u == v153;
            bool v158;
            if (v154){
                unsigned char v155;
                v155 = v152 / 4u;
                bool v156;
                v156 = v155 == 12u;
                if (v156){
                    v121.v[4l] = v152;
                    v158 = true;
                } else {
                    v158 = false;
                }
            } else {
                v158 = false;
            }
            if (v158){
                v184 = true;
            } else {
                unsigned char v159;
                v159 = v120.v[1l];
                unsigned char v160;
                v160 = v159 % 4u;
                bool v161;
                v161 = 0u == v160;
                bool v165;
                if (v161){
                    unsigned char v162;
                    v162 = v159 / 4u;
                    bool v163;
                    v163 = v162 == 12u;
                    if (v163){
                        v121.v[4l] = v159;
                        v165 = true;
                    } else {
                        v165 = false;
                    }
                } else {
                    v165 = false;
                }
                if (v165){
                    v184 = true;
                } else {
                    unsigned char v166;
                    v166 = v120.v[2l];
                    unsigned char v167;
                    v167 = v166 % 4u;
                    bool v168;
                    v168 = 0u == v167;
                    bool v172;
                    if (v168){
                        unsigned char v169;
                        v169 = v166 / 4u;
                        bool v170;
                        v170 = v169 == 12u;
                        if (v170){
                            v121.v[4l] = v166;
                            v172 = true;
                        } else {
                            v172 = false;
                        }
                    } else {
                        v172 = false;
                    }
                    if (v172){
                        v184 = true;
                    } else {
                        unsigned char v173;
                        v173 = v120.v[3l];
                        unsigned char v174;
                        v174 = v173 % 4u;
                        bool v175;
                        v175 = 0u == v174;
                        if (v175){
                            unsigned char v176;
                            v176 = v173 / 4u;
                            bool v177;
                            v177 = v176 == 12u;
                            if (v177){
                                v121.v[4l] = v173;
                                v184 = true;
                            } else {
                                v184 = false;
                            }
                        } else {
                            v184 = false;
                        }
                    }
                }
            }
        } else {
            v184 = false;
        }
    } else {
        v184 = false;
    }
    US11 v190;
    if (v184){
        v190 = US11_1(v121);
    } else {
        bool v186;
        v186 = v123 == 5l;
        if (v186){
            v190 = US11_1(v121);
        } else {
            v190 = US11_0();
        }
    }
    static_array<unsigned char,5l> v191;
    long v192; long v193; unsigned char v194;
    Tuple13 tmp27 = Tuple13(0l, 0l, 12u);
    v192 = tmp27.v0; v193 = tmp27.v1; v194 = tmp27.v2;
    while (while_method_9(v192)){
        bool v196;
        v196 = 0l <= v192;
        bool v198;
        if (v196){
            bool v197;
            v197 = v192 < 7l;
            v198 = v197;
        } else {
            v198 = false;
        }
        bool v199;
        v199 = v198 == false;
        if (v199){
            assert("The read index needs to be in range for the static array." && v198);
        } else {
        }
        unsigned char v200;
        v200 = v120.v[v192];
        bool v201;
        v201 = v193 < 5l;
        long v217; unsigned char v218;
        if (v201){
            unsigned char v202;
            v202 = v200 % 4u;
            bool v203;
            v203 = 1u == v202;
            if (v203){
                unsigned char v204;
                v204 = v200 / 4u;
                bool v205;
                v205 = v194 == v204;
                long v206;
                if (v205){
                    v206 = v193;
                } else {
                    v206 = 0l;
                }
                bool v207;
                v207 = 0l <= v206;
                bool v209;
                if (v207){
                    bool v208;
                    v208 = v206 < 5l;
                    v209 = v208;
                } else {
                    v209 = false;
                }
                bool v210;
                v210 = v209 == false;
                if (v210){
                    assert("The read index needs to be in range for the static array." && v209);
                } else {
                }
                v191.v[v206] = v200;
                long v211;
                v211 = v206 + 1l;
                unsigned char v212;
                v212 = v204 - 1u;
                v217 = v211; v218 = v212;
            } else {
                v217 = v193; v218 = v194;
            }
        } else {
            break;
        }
        v193 = v217;
        v194 = v218;
        v192 += 1l ;
    }
    bool v219;
    v219 = v193 == 4l;
    bool v254;
    if (v219){
        unsigned char v220;
        v220 = v194 + 1u;
        bool v221;
        v221 = v220 == 0u;
        if (v221){
            unsigned char v222;
            v222 = v120.v[0l];
            unsigned char v223;
            v223 = v222 % 4u;
            bool v224;
            v224 = 1u == v223;
            bool v228;
            if (v224){
                unsigned char v225;
                v225 = v222 / 4u;
                bool v226;
                v226 = v225 == 12u;
                if (v226){
                    v191.v[4l] = v222;
                    v228 = true;
                } else {
                    v228 = false;
                }
            } else {
                v228 = false;
            }
            if (v228){
                v254 = true;
            } else {
                unsigned char v229;
                v229 = v120.v[1l];
                unsigned char v230;
                v230 = v229 % 4u;
                bool v231;
                v231 = 1u == v230;
                bool v235;
                if (v231){
                    unsigned char v232;
                    v232 = v229 / 4u;
                    bool v233;
                    v233 = v232 == 12u;
                    if (v233){
                        v191.v[4l] = v229;
                        v235 = true;
                    } else {
                        v235 = false;
                    }
                } else {
                    v235 = false;
                }
                if (v235){
                    v254 = true;
                } else {
                    unsigned char v236;
                    v236 = v120.v[2l];
                    unsigned char v237;
                    v237 = v236 % 4u;
                    bool v238;
                    v238 = 1u == v237;
                    bool v242;
                    if (v238){
                        unsigned char v239;
                        v239 = v236 / 4u;
                        bool v240;
                        v240 = v239 == 12u;
                        if (v240){
                            v191.v[4l] = v236;
                            v242 = true;
                        } else {
                            v242 = false;
                        }
                    } else {
                        v242 = false;
                    }
                    if (v242){
                        v254 = true;
                    } else {
                        unsigned char v243;
                        v243 = v120.v[3l];
                        unsigned char v244;
                        v244 = v243 % 4u;
                        bool v245;
                        v245 = 1u == v244;
                        if (v245){
                            unsigned char v246;
                            v246 = v243 / 4u;
                            bool v247;
                            v247 = v246 == 12u;
                            if (v247){
                                v191.v[4l] = v243;
                                v254 = true;
                            } else {
                                v254 = false;
                            }
                        } else {
                            v254 = false;
                        }
                    }
                }
            }
        } else {
            v254 = false;
        }
    } else {
        v254 = false;
    }
    US11 v260;
    if (v254){
        v260 = US11_1(v191);
    } else {
        bool v256;
        v256 = v193 == 5l;
        if (v256){
            v260 = US11_1(v191);
        } else {
            v260 = US11_0();
        }
    }
    US11 v293;
    switch (v190.tag) {
        case 0: { // None
            v293 = v260;
            break;
        }
        case 1: { // Some
            static_array<unsigned char,5l> v261 = v190.v.case1.v0;
            switch (v260.tag) {
                case 0: { // None
                    v293 = v190;
                    break;
                }
                case 1: { // Some
                    static_array<unsigned char,5l> v262 = v260.v.case1.v0;
                    US10 v263;
                    v263 = US10_0();
                    long v264; US10 v265;
                    Tuple14 tmp28 = Tuple14(0l, v263);
                    v264 = tmp28.v0; v265 = tmp28.v1;
                    while (while_method_2(v264)){
                        bool v267;
                        v267 = 0l <= v264;
                        bool v269;
                        if (v267){
                            bool v268;
                            v268 = v264 < 5l;
                            v269 = v268;
                        } else {
                            v269 = false;
                        }
                        bool v270;
                        v270 = v269 == false;
                        if (v270){
                            assert("The read index needs to be in range for the static array." && v269);
                        } else {
                        }
                        unsigned char v271;
                        v271 = v261.v[v264];
                        bool v273;
                        if (v267){
                            bool v272;
                            v272 = v264 < 5l;
                            v273 = v272;
                        } else {
                            v273 = false;
                        }
                        bool v274;
                        v274 = v273 == false;
                        if (v274){
                            assert("The read index needs to be in range for the static array." && v273);
                        } else {
                        }
                        unsigned char v275;
                        v275 = v262.v[v264];
                        US10 v286;
                        switch (v265.tag) {
                            case 0: { // Eq
                                unsigned char v276;
                                v276 = v271 / 4u;
                                unsigned char v277;
                                v277 = v275 / 4u;
                                bool v278;
                                v278 = v276 < v277;
                                if (v278){
                                    v286 = US10_2();
                                } else {
                                    bool v280;
                                    v280 = v276 > v277;
                                    if (v280){
                                        v286 = US10_1();
                                    } else {
                                        v286 = US10_0();
                                    }
                                }
                                break;
                            }
                            default: {
                                break;
                            }
                        }
                        v265 = v286;
                        v264 += 1l ;
                    }
                    bool v287;
                    switch (v265.tag) {
                        case 1: { // Gt
                            v287 = true;
                            break;
                        }
                        default: {
                            v287 = false;
                        }
                    }
                    static_array<unsigned char,5l> v288;
                    if (v287){
                        v288 = v261;
                    } else {
                        v288 = v262;
                    }
                    v293 = US11_1(v288);
                    break;
                }
                default: {
                    assert("Invalid tag." && false);
                }
            }
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
    static_array<unsigned char,5l> v294;
    long v295; long v296; unsigned char v297;
    Tuple13 tmp29 = Tuple13(0l, 0l, 12u);
    v295 = tmp29.v0; v296 = tmp29.v1; v297 = tmp29.v2;
    while (while_method_9(v295)){
        bool v299;
        v299 = 0l <= v295;
        bool v301;
        if (v299){
            bool v300;
            v300 = v295 < 7l;
            v301 = v300;
        } else {
            v301 = false;
        }
        bool v302;
        v302 = v301 == false;
        if (v302){
            assert("The read index needs to be in range for the static array." && v301);
        } else {
        }
        unsigned char v303;
        v303 = v120.v[v295];
        bool v304;
        v304 = v296 < 5l;
        long v320; unsigned char v321;
        if (v304){
            unsigned char v305;
            v305 = v303 % 4u;
            bool v306;
            v306 = 2u == v305;
            if (v306){
                unsigned char v307;
                v307 = v303 / 4u;
                bool v308;
                v308 = v297 == v307;
                long v309;
                if (v308){
                    v309 = v296;
                } else {
                    v309 = 0l;
                }
                bool v310;
                v310 = 0l <= v309;
                bool v312;
                if (v310){
                    bool v311;
                    v311 = v309 < 5l;
                    v312 = v311;
                } else {
                    v312 = false;
                }
                bool v313;
                v313 = v312 == false;
                if (v313){
                    assert("The read index needs to be in range for the static array." && v312);
                } else {
                }
                v294.v[v309] = v303;
                long v314;
                v314 = v309 + 1l;
                unsigned char v315;
                v315 = v307 - 1u;
                v320 = v314; v321 = v315;
            } else {
                v320 = v296; v321 = v297;
            }
        } else {
            break;
        }
        v296 = v320;
        v297 = v321;
        v295 += 1l ;
    }
    bool v322;
    v322 = v296 == 4l;
    bool v357;
    if (v322){
        unsigned char v323;
        v323 = v297 + 1u;
        bool v324;
        v324 = v323 == 0u;
        if (v324){
            unsigned char v325;
            v325 = v120.v[0l];
            unsigned char v326;
            v326 = v325 % 4u;
            bool v327;
            v327 = 2u == v326;
            bool v331;
            if (v327){
                unsigned char v328;
                v328 = v325 / 4u;
                bool v329;
                v329 = v328 == 12u;
                if (v329){
                    v294.v[4l] = v325;
                    v331 = true;
                } else {
                    v331 = false;
                }
            } else {
                v331 = false;
            }
            if (v331){
                v357 = true;
            } else {
                unsigned char v332;
                v332 = v120.v[1l];
                unsigned char v333;
                v333 = v332 % 4u;
                bool v334;
                v334 = 2u == v333;
                bool v338;
                if (v334){
                    unsigned char v335;
                    v335 = v332 / 4u;
                    bool v336;
                    v336 = v335 == 12u;
                    if (v336){
                        v294.v[4l] = v332;
                        v338 = true;
                    } else {
                        v338 = false;
                    }
                } else {
                    v338 = false;
                }
                if (v338){
                    v357 = true;
                } else {
                    unsigned char v339;
                    v339 = v120.v[2l];
                    unsigned char v340;
                    v340 = v339 % 4u;
                    bool v341;
                    v341 = 2u == v340;
                    bool v345;
                    if (v341){
                        unsigned char v342;
                        v342 = v339 / 4u;
                        bool v343;
                        v343 = v342 == 12u;
                        if (v343){
                            v294.v[4l] = v339;
                            v345 = true;
                        } else {
                            v345 = false;
                        }
                    } else {
                        v345 = false;
                    }
                    if (v345){
                        v357 = true;
                    } else {
                        unsigned char v346;
                        v346 = v120.v[3l];
                        unsigned char v347;
                        v347 = v346 % 4u;
                        bool v348;
                        v348 = 2u == v347;
                        if (v348){
                            unsigned char v349;
                            v349 = v346 / 4u;
                            bool v350;
                            v350 = v349 == 12u;
                            if (v350){
                                v294.v[4l] = v346;
                                v357 = true;
                            } else {
                                v357 = false;
                            }
                        } else {
                            v357 = false;
                        }
                    }
                }
            }
        } else {
            v357 = false;
        }
    } else {
        v357 = false;
    }
    US11 v363;
    if (v357){
        v363 = US11_1(v294);
    } else {
        bool v359;
        v359 = v296 == 5l;
        if (v359){
            v363 = US11_1(v294);
        } else {
            v363 = US11_0();
        }
    }
    US11 v396;
    switch (v293.tag) {
        case 0: { // None
            v396 = v363;
            break;
        }
        case 1: { // Some
            static_array<unsigned char,5l> v364 = v293.v.case1.v0;
            switch (v363.tag) {
                case 0: { // None
                    v396 = v293;
                    break;
                }
                case 1: { // Some
                    static_array<unsigned char,5l> v365 = v363.v.case1.v0;
                    US10 v366;
                    v366 = US10_0();
                    long v367; US10 v368;
                    Tuple14 tmp30 = Tuple14(0l, v366);
                    v367 = tmp30.v0; v368 = tmp30.v1;
                    while (while_method_2(v367)){
                        bool v370;
                        v370 = 0l <= v367;
                        bool v372;
                        if (v370){
                            bool v371;
                            v371 = v367 < 5l;
                            v372 = v371;
                        } else {
                            v372 = false;
                        }
                        bool v373;
                        v373 = v372 == false;
                        if (v373){
                            assert("The read index needs to be in range for the static array." && v372);
                        } else {
                        }
                        unsigned char v374;
                        v374 = v364.v[v367];
                        bool v376;
                        if (v370){
                            bool v375;
                            v375 = v367 < 5l;
                            v376 = v375;
                        } else {
                            v376 = false;
                        }
                        bool v377;
                        v377 = v376 == false;
                        if (v377){
                            assert("The read index needs to be in range for the static array." && v376);
                        } else {
                        }
                        unsigned char v378;
                        v378 = v365.v[v367];
                        US10 v389;
                        switch (v368.tag) {
                            case 0: { // Eq
                                unsigned char v379;
                                v379 = v374 / 4u;
                                unsigned char v380;
                                v380 = v378 / 4u;
                                bool v381;
                                v381 = v379 < v380;
                                if (v381){
                                    v389 = US10_2();
                                } else {
                                    bool v383;
                                    v383 = v379 > v380;
                                    if (v383){
                                        v389 = US10_1();
                                    } else {
                                        v389 = US10_0();
                                    }
                                }
                                break;
                            }
                            default: {
                                break;
                            }
                        }
                        v368 = v389;
                        v367 += 1l ;
                    }
                    bool v390;
                    switch (v368.tag) {
                        case 1: { // Gt
                            v390 = true;
                            break;
                        }
                        default: {
                            v390 = false;
                        }
                    }
                    static_array<unsigned char,5l> v391;
                    if (v390){
                        v391 = v364;
                    } else {
                        v391 = v365;
                    }
                    v396 = US11_1(v391);
                    break;
                }
                default: {
                    assert("Invalid tag." && false);
                }
            }
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
    static_array<unsigned char,5l> v397;
    long v398; long v399; unsigned char v400;
    Tuple13 tmp31 = Tuple13(0l, 0l, 12u);
    v398 = tmp31.v0; v399 = tmp31.v1; v400 = tmp31.v2;
    while (while_method_9(v398)){
        bool v402;
        v402 = 0l <= v398;
        bool v404;
        if (v402){
            bool v403;
            v403 = v398 < 7l;
            v404 = v403;
        } else {
            v404 = false;
        }
        bool v405;
        v405 = v404 == false;
        if (v405){
            assert("The read index needs to be in range for the static array." && v404);
        } else {
        }
        unsigned char v406;
        v406 = v120.v[v398];
        bool v407;
        v407 = v399 < 5l;
        long v423; unsigned char v424;
        if (v407){
            unsigned char v408;
            v408 = v406 % 4u;
            bool v409;
            v409 = 3u == v408;
            if (v409){
                unsigned char v410;
                v410 = v406 / 4u;
                bool v411;
                v411 = v400 == v410;
                long v412;
                if (v411){
                    v412 = v399;
                } else {
                    v412 = 0l;
                }
                bool v413;
                v413 = 0l <= v412;
                bool v415;
                if (v413){
                    bool v414;
                    v414 = v412 < 5l;
                    v415 = v414;
                } else {
                    v415 = false;
                }
                bool v416;
                v416 = v415 == false;
                if (v416){
                    assert("The read index needs to be in range for the static array." && v415);
                } else {
                }
                v397.v[v412] = v406;
                long v417;
                v417 = v412 + 1l;
                unsigned char v418;
                v418 = v410 - 1u;
                v423 = v417; v424 = v418;
            } else {
                v423 = v399; v424 = v400;
            }
        } else {
            break;
        }
        v399 = v423;
        v400 = v424;
        v398 += 1l ;
    }
    bool v425;
    v425 = v399 == 4l;
    bool v460;
    if (v425){
        unsigned char v426;
        v426 = v400 + 1u;
        bool v427;
        v427 = v426 == 0u;
        if (v427){
            unsigned char v428;
            v428 = v120.v[0l];
            unsigned char v429;
            v429 = v428 % 4u;
            bool v430;
            v430 = 3u == v429;
            bool v434;
            if (v430){
                unsigned char v431;
                v431 = v428 / 4u;
                bool v432;
                v432 = v431 == 12u;
                if (v432){
                    v397.v[4l] = v428;
                    v434 = true;
                } else {
                    v434 = false;
                }
            } else {
                v434 = false;
            }
            if (v434){
                v460 = true;
            } else {
                unsigned char v435;
                v435 = v120.v[1l];
                unsigned char v436;
                v436 = v435 % 4u;
                bool v437;
                v437 = 3u == v436;
                bool v441;
                if (v437){
                    unsigned char v438;
                    v438 = v435 / 4u;
                    bool v439;
                    v439 = v438 == 12u;
                    if (v439){
                        v397.v[4l] = v435;
                        v441 = true;
                    } else {
                        v441 = false;
                    }
                } else {
                    v441 = false;
                }
                if (v441){
                    v460 = true;
                } else {
                    unsigned char v442;
                    v442 = v120.v[2l];
                    unsigned char v443;
                    v443 = v442 % 4u;
                    bool v444;
                    v444 = 3u == v443;
                    bool v448;
                    if (v444){
                        unsigned char v445;
                        v445 = v442 / 4u;
                        bool v446;
                        v446 = v445 == 12u;
                        if (v446){
                            v397.v[4l] = v442;
                            v448 = true;
                        } else {
                            v448 = false;
                        }
                    } else {
                        v448 = false;
                    }
                    if (v448){
                        v460 = true;
                    } else {
                        unsigned char v449;
                        v449 = v120.v[3l];
                        unsigned char v450;
                        v450 = v449 % 4u;
                        bool v451;
                        v451 = 3u == v450;
                        if (v451){
                            unsigned char v452;
                            v452 = v449 / 4u;
                            bool v453;
                            v453 = v452 == 12u;
                            if (v453){
                                v397.v[4l] = v449;
                                v460 = true;
                            } else {
                                v460 = false;
                            }
                        } else {
                            v460 = false;
                        }
                    }
                }
            }
        } else {
            v460 = false;
        }
    } else {
        v460 = false;
    }
    US11 v466;
    if (v460){
        v466 = US11_1(v397);
    } else {
        bool v462;
        v462 = v399 == 5l;
        if (v462){
            v466 = US11_1(v397);
        } else {
            v466 = US11_0();
        }
    }
    US11 v499;
    switch (v396.tag) {
        case 0: { // None
            v499 = v466;
            break;
        }
        case 1: { // Some
            static_array<unsigned char,5l> v467 = v396.v.case1.v0;
            switch (v466.tag) {
                case 0: { // None
                    v499 = v396;
                    break;
                }
                case 1: { // Some
                    static_array<unsigned char,5l> v468 = v466.v.case1.v0;
                    US10 v469;
                    v469 = US10_0();
                    long v470; US10 v471;
                    Tuple14 tmp32 = Tuple14(0l, v469);
                    v470 = tmp32.v0; v471 = tmp32.v1;
                    while (while_method_2(v470)){
                        bool v473;
                        v473 = 0l <= v470;
                        bool v475;
                        if (v473){
                            bool v474;
                            v474 = v470 < 5l;
                            v475 = v474;
                        } else {
                            v475 = false;
                        }
                        bool v476;
                        v476 = v475 == false;
                        if (v476){
                            assert("The read index needs to be in range for the static array." && v475);
                        } else {
                        }
                        unsigned char v477;
                        v477 = v467.v[v470];
                        bool v479;
                        if (v473){
                            bool v478;
                            v478 = v470 < 5l;
                            v479 = v478;
                        } else {
                            v479 = false;
                        }
                        bool v480;
                        v480 = v479 == false;
                        if (v480){
                            assert("The read index needs to be in range for the static array." && v479);
                        } else {
                        }
                        unsigned char v481;
                        v481 = v468.v[v470];
                        US10 v492;
                        switch (v471.tag) {
                            case 0: { // Eq
                                unsigned char v482;
                                v482 = v477 / 4u;
                                unsigned char v483;
                                v483 = v481 / 4u;
                                bool v484;
                                v484 = v482 < v483;
                                if (v484){
                                    v492 = US10_2();
                                } else {
                                    bool v486;
                                    v486 = v482 > v483;
                                    if (v486){
                                        v492 = US10_1();
                                    } else {
                                        v492 = US10_0();
                                    }
                                }
                                break;
                            }
                            default: {
                                break;
                            }
                        }
                        v471 = v492;
                        v470 += 1l ;
                    }
                    bool v493;
                    switch (v471.tag) {
                        case 1: { // Gt
                            v493 = true;
                            break;
                        }
                        default: {
                            v493 = false;
                        }
                    }
                    static_array<unsigned char,5l> v494;
                    if (v493){
                        v494 = v467;
                    } else {
                        v494 = v468;
                    }
                    v499 = US11_1(v494);
                    break;
                }
                default: {
                    assert("Invalid tag." && false);
                }
            }
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
    static_array<unsigned char,5l> v1316; char v1317;
    switch (v499.tag) {
        case 0: { // None
            static_array<unsigned char,4l> v501;
            static_array<unsigned char,3l> v502;
            long v503; long v504; long v505; unsigned char v506;
            Tuple15 tmp33 = Tuple15(0l, 0l, 0l, 12u);
            v503 = tmp33.v0; v504 = tmp33.v1; v505 = tmp33.v2; v506 = tmp33.v3;
            while (while_method_9(v503)){
                bool v508;
                v508 = 0l <= v503;
                bool v510;
                if (v508){
                    bool v509;
                    v509 = v503 < 7l;
                    v510 = v509;
                } else {
                    v510 = false;
                }
                bool v511;
                v511 = v510 == false;
                if (v511){
                    assert("The read index needs to be in range for the static array." && v510);
                } else {
                }
                unsigned char v512;
                v512 = v120.v[v503];
                bool v513;
                v513 = v505 < 4l;
                long v525; long v526; unsigned char v527;
                if (v513){
                    unsigned char v514;
                    v514 = v512 / 4u;
                    bool v515;
                    v515 = v506 == v514;
                    long v516;
                    if (v515){
                        v516 = v505;
                    } else {
                        v516 = 0l;
                    }
                    bool v517;
                    v517 = 0l <= v516;
                    bool v519;
                    if (v517){
                        bool v518;
                        v518 = v516 < 4l;
                        v519 = v518;
                    } else {
                        v519 = false;
                    }
                    bool v520;
                    v520 = v519 == false;
                    if (v520){
                        assert("The read index needs to be in range for the static array." && v519);
                    } else {
                    }
                    v501.v[v516] = v512;
                    long v521;
                    v521 = v516 + 1l;
                    v525 = v503; v526 = v521; v527 = v514;
                } else {
                    break;
                }
                v504 = v525;
                v505 = v526;
                v506 = v527;
                v503 += 1l ;
            }
            bool v528;
            v528 = v505 == 4l;
            US12 v546;
            if (v528){
                long v529;
                v529 = 0l;
                while (while_method_1(v529)){
                    long v531;
                    v531 = v504 + -3l;
                    bool v532;
                    v532 = v529 < v531;
                    long v533;
                    if (v532){
                        v533 = 0l;
                    } else {
                        v533 = 4l;
                    }
                    long v534;
                    v534 = v533 + v529;
                    bool v535;
                    v535 = 0l <= v534;
                    bool v537;
                    if (v535){
                        bool v536;
                        v536 = v534 < 7l;
                        v537 = v536;
                    } else {
                        v537 = false;
                    }
                    bool v538;
                    v538 = v537 == false;
                    if (v538){
                        assert("The read index needs to be in range for the static array." && v537);
                    } else {
                    }
                    unsigned char v539;
                    v539 = v120.v[v534];
                    bool v540;
                    v540 = 0l <= v529;
                    bool v542;
                    if (v540){
                        bool v541;
                        v541 = v529 < 3l;
                        v542 = v541;
                    } else {
                        v542 = false;
                    }
                    bool v543;
                    v543 = v542 == false;
                    if (v543){
                        assert("The read index needs to be in range for the static array." && v542);
                    } else {
                    }
                    v502.v[v529] = v539;
                    v529 += 1l ;
                }
                v546 = US12_1(v501, v502);
            } else {
                v546 = US12_0();
            }
            US11 v586;
            switch (v546.tag) {
                case 0: { // None
                    v586 = US11_0();
                    break;
                }
                case 1: { // Some
                    static_array<unsigned char,4l> v547 = v546.v.case1.v0; static_array<unsigned char,3l> v548 = v546.v.case1.v1;
                    static_array<unsigned char,1l> v549;
                    long v550;
                    v550 = 0l;
                    while (while_method_5(v550)){
                        bool v552;
                        v552 = 0l <= v550;
                        bool v554;
                        if (v552){
                            bool v553;
                            v553 = v550 < 3l;
                            v554 = v553;
                        } else {
                            v554 = false;
                        }
                        bool v555;
                        v555 = v554 == false;
                        if (v555){
                            assert("The read index needs to be in range for the static array." && v554);
                        } else {
                        }
                        unsigned char v556;
                        v556 = v548.v[v550];
                        bool v558;
                        if (v552){
                            bool v557;
                            v557 = v550 < 1l;
                            v558 = v557;
                        } else {
                            v558 = false;
                        }
                        bool v559;
                        v559 = v558 == false;
                        if (v559){
                            assert("The read index needs to be in range for the static array." && v558);
                        } else {
                        }
                        v549.v[v550] = v556;
                        v550 += 1l ;
                    }
                    static_array<unsigned char,5l> v560;
                    long v561;
                    v561 = 0l;
                    while (while_method_3(v561)){
                        bool v563;
                        v563 = 0l <= v561;
                        bool v565;
                        if (v563){
                            bool v564;
                            v564 = v561 < 4l;
                            v565 = v564;
                        } else {
                            v565 = false;
                        }
                        bool v566;
                        v566 = v565 == false;
                        if (v566){
                            assert("The read index needs to be in range for the static array." && v565);
                        } else {
                        }
                        unsigned char v567;
                        v567 = v547.v[v561];
                        bool v569;
                        if (v563){
                            bool v568;
                            v568 = v561 < 5l;
                            v569 = v568;
                        } else {
                            v569 = false;
                        }
                        bool v570;
                        v570 = v569 == false;
                        if (v570){
                            assert("The read index needs to be in range for the static array." && v569);
                        } else {
                        }
                        v560.v[v561] = v567;
                        v561 += 1l ;
                    }
                    long v571;
                    v571 = 0l;
                    while (while_method_5(v571)){
                        bool v573;
                        v573 = 0l <= v571;
                        bool v575;
                        if (v573){
                            bool v574;
                            v574 = v571 < 1l;
                            v575 = v574;
                        } else {
                            v575 = false;
                        }
                        bool v576;
                        v576 = v575 == false;
                        if (v576){
                            assert("The read index needs to be in range for the static array." && v575);
                        } else {
                        }
                        unsigned char v577;
                        v577 = v549.v[v571];
                        long v578;
                        v578 = 4l + v571;
                        bool v579;
                        v579 = 0l <= v578;
                        bool v581;
                        if (v579){
                            bool v580;
                            v580 = v578 < 5l;
                            v581 = v580;
                        } else {
                            v581 = false;
                        }
                        bool v582;
                        v582 = v581 == false;
                        if (v582){
                            assert("The read index needs to be in range for the static array." && v581);
                        } else {
                        }
                        v560.v[v578] = v577;
                        v571 += 1l ;
                    }
                    v586 = US11_1(v560);
                    break;
                }
                default: {
                    assert("Invalid tag." && false);
                }
            }
            switch (v586.tag) {
                case 0: { // None
                    static_array<unsigned char,3l> v588;
                    static_array<unsigned char,4l> v589;
                    long v590; long v591; long v592; unsigned char v593;
                    Tuple15 tmp34 = Tuple15(0l, 0l, 0l, 12u);
                    v590 = tmp34.v0; v591 = tmp34.v1; v592 = tmp34.v2; v593 = tmp34.v3;
                    while (while_method_9(v590)){
                        bool v595;
                        v595 = 0l <= v590;
                        bool v597;
                        if (v595){
                            bool v596;
                            v596 = v590 < 7l;
                            v597 = v596;
                        } else {
                            v597 = false;
                        }
                        bool v598;
                        v598 = v597 == false;
                        if (v598){
                            assert("The read index needs to be in range for the static array." && v597);
                        } else {
                        }
                        unsigned char v599;
                        v599 = v120.v[v590];
                        bool v600;
                        v600 = v592 < 3l;
                        long v612; long v613; unsigned char v614;
                        if (v600){
                            unsigned char v601;
                            v601 = v599 / 4u;
                            bool v602;
                            v602 = v593 == v601;
                            long v603;
                            if (v602){
                                v603 = v592;
                            } else {
                                v603 = 0l;
                            }
                            bool v604;
                            v604 = 0l <= v603;
                            bool v606;
                            if (v604){
                                bool v605;
                                v605 = v603 < 3l;
                                v606 = v605;
                            } else {
                                v606 = false;
                            }
                            bool v607;
                            v607 = v606 == false;
                            if (v607){
                                assert("The read index needs to be in range for the static array." && v606);
                            } else {
                            }
                            v588.v[v603] = v599;
                            long v608;
                            v608 = v603 + 1l;
                            v612 = v590; v613 = v608; v614 = v601;
                        } else {
                            break;
                        }
                        v591 = v612;
                        v592 = v613;
                        v593 = v614;
                        v590 += 1l ;
                    }
                    bool v615;
                    v615 = v592 == 3l;
                    US13 v633;
                    if (v615){
                        long v616;
                        v616 = 0l;
                        while (while_method_3(v616)){
                            long v618;
                            v618 = v591 + -2l;
                            bool v619;
                            v619 = v616 < v618;
                            long v620;
                            if (v619){
                                v620 = 0l;
                            } else {
                                v620 = 3l;
                            }
                            long v621;
                            v621 = v620 + v616;
                            bool v622;
                            v622 = 0l <= v621;
                            bool v624;
                            if (v622){
                                bool v623;
                                v623 = v621 < 7l;
                                v624 = v623;
                            } else {
                                v624 = false;
                            }
                            bool v625;
                            v625 = v624 == false;
                            if (v625){
                                assert("The read index needs to be in range for the static array." && v624);
                            } else {
                            }
                            unsigned char v626;
                            v626 = v120.v[v621];
                            bool v627;
                            v627 = 0l <= v616;
                            bool v629;
                            if (v627){
                                bool v628;
                                v628 = v616 < 4l;
                                v629 = v628;
                            } else {
                                v629 = false;
                            }
                            bool v630;
                            v630 = v629 == false;
                            if (v630){
                                assert("The read index needs to be in range for the static array." && v629);
                            } else {
                            }
                            v589.v[v616] = v626;
                            v616 += 1l ;
                        }
                        v633 = US13_1(v588, v589);
                    } else {
                        v633 = US13_0();
                    }
                    US11 v713;
                    switch (v633.tag) {
                        case 0: { // None
                            v713 = US11_0();
                            break;
                        }
                        case 1: { // Some
                            static_array<unsigned char,3l> v634 = v633.v.case1.v0; static_array<unsigned char,4l> v635 = v633.v.case1.v1;
                            static_array<unsigned char,2l> v636;
                            static_array<unsigned char,2l> v637;
                            long v638; long v639; long v640; unsigned char v641;
                            Tuple15 tmp35 = Tuple15(0l, 0l, 0l, 12u);
                            v638 = tmp35.v0; v639 = tmp35.v1; v640 = tmp35.v2; v641 = tmp35.v3;
                            while (while_method_3(v638)){
                                bool v643;
                                v643 = 0l <= v638;
                                bool v645;
                                if (v643){
                                    bool v644;
                                    v644 = v638 < 4l;
                                    v645 = v644;
                                } else {
                                    v645 = false;
                                }
                                bool v646;
                                v646 = v645 == false;
                                if (v646){
                                    assert("The read index needs to be in range for the static array." && v645);
                                } else {
                                }
                                unsigned char v647;
                                v647 = v635.v[v638];
                                bool v648;
                                v648 = v640 < 2l;
                                long v660; long v661; unsigned char v662;
                                if (v648){
                                    unsigned char v649;
                                    v649 = v647 / 4u;
                                    bool v650;
                                    v650 = v641 == v649;
                                    long v651;
                                    if (v650){
                                        v651 = v640;
                                    } else {
                                        v651 = 0l;
                                    }
                                    bool v652;
                                    v652 = 0l <= v651;
                                    bool v654;
                                    if (v652){
                                        bool v653;
                                        v653 = v651 < 2l;
                                        v654 = v653;
                                    } else {
                                        v654 = false;
                                    }
                                    bool v655;
                                    v655 = v654 == false;
                                    if (v655){
                                        assert("The read index needs to be in range for the static array." && v654);
                                    } else {
                                    }
                                    v636.v[v651] = v647;
                                    long v656;
                                    v656 = v651 + 1l;
                                    v660 = v638; v661 = v656; v662 = v649;
                                } else {
                                    break;
                                }
                                v639 = v660;
                                v640 = v661;
                                v641 = v662;
                                v638 += 1l ;
                            }
                            bool v663;
                            v663 = v640 == 2l;
                            US14 v681;
                            if (v663){
                                long v664;
                                v664 = 0l;
                                while (while_method_4(v664)){
                                    long v666;
                                    v666 = v639 + -1l;
                                    bool v667;
                                    v667 = v664 < v666;
                                    long v668;
                                    if (v667){
                                        v668 = 0l;
                                    } else {
                                        v668 = 2l;
                                    }
                                    long v669;
                                    v669 = v668 + v664;
                                    bool v670;
                                    v670 = 0l <= v669;
                                    bool v672;
                                    if (v670){
                                        bool v671;
                                        v671 = v669 < 4l;
                                        v672 = v671;
                                    } else {
                                        v672 = false;
                                    }
                                    bool v673;
                                    v673 = v672 == false;
                                    if (v673){
                                        assert("The read index needs to be in range for the static array." && v672);
                                    } else {
                                    }
                                    unsigned char v674;
                                    v674 = v635.v[v669];
                                    bool v675;
                                    v675 = 0l <= v664;
                                    bool v677;
                                    if (v675){
                                        bool v676;
                                        v676 = v664 < 2l;
                                        v677 = v676;
                                    } else {
                                        v677 = false;
                                    }
                                    bool v678;
                                    v678 = v677 == false;
                                    if (v678){
                                        assert("The read index needs to be in range for the static array." && v677);
                                    } else {
                                    }
                                    v637.v[v664] = v674;
                                    v664 += 1l ;
                                }
                                v681 = US14_1(v636, v637);
                            } else {
                                v681 = US14_0();
                            }
                            switch (v681.tag) {
                                case 0: { // None
                                    v713 = US11_0();
                                    break;
                                }
                                case 1: { // Some
                                    static_array<unsigned char,2l> v682 = v681.v.case1.v0; static_array<unsigned char,2l> v683 = v681.v.case1.v1;
                                    static_array<unsigned char,5l> v684;
                                    long v685;
                                    v685 = 0l;
                                    while (while_method_1(v685)){
                                        bool v687;
                                        v687 = 0l <= v685;
                                        bool v689;
                                        if (v687){
                                            bool v688;
                                            v688 = v685 < 3l;
                                            v689 = v688;
                                        } else {
                                            v689 = false;
                                        }
                                        bool v690;
                                        v690 = v689 == false;
                                        if (v690){
                                            assert("The read index needs to be in range for the static array." && v689);
                                        } else {
                                        }
                                        unsigned char v691;
                                        v691 = v634.v[v685];
                                        bool v693;
                                        if (v687){
                                            bool v692;
                                            v692 = v685 < 5l;
                                            v693 = v692;
                                        } else {
                                            v693 = false;
                                        }
                                        bool v694;
                                        v694 = v693 == false;
                                        if (v694){
                                            assert("The read index needs to be in range for the static array." && v693);
                                        } else {
                                        }
                                        v684.v[v685] = v691;
                                        v685 += 1l ;
                                    }
                                    long v695;
                                    v695 = 0l;
                                    while (while_method_4(v695)){
                                        bool v697;
                                        v697 = 0l <= v695;
                                        bool v699;
                                        if (v697){
                                            bool v698;
                                            v698 = v695 < 2l;
                                            v699 = v698;
                                        } else {
                                            v699 = false;
                                        }
                                        bool v700;
                                        v700 = v699 == false;
                                        if (v700){
                                            assert("The read index needs to be in range for the static array." && v699);
                                        } else {
                                        }
                                        unsigned char v701;
                                        v701 = v682.v[v695];
                                        long v702;
                                        v702 = 3l + v695;
                                        bool v703;
                                        v703 = 0l <= v702;
                                        bool v705;
                                        if (v703){
                                            bool v704;
                                            v704 = v702 < 5l;
                                            v705 = v704;
                                        } else {
                                            v705 = false;
                                        }
                                        bool v706;
                                        v706 = v705 == false;
                                        if (v706){
                                            assert("The read index needs to be in range for the static array." && v705);
                                        } else {
                                        }
                                        v684.v[v702] = v701;
                                        v695 += 1l ;
                                    }
                                    v713 = US11_1(v684);
                                    break;
                                }
                                default: {
                                    assert("Invalid tag." && false);
                                }
                            }
                            break;
                        }
                        default: {
                            assert("Invalid tag." && false);
                        }
                    }
                    switch (v713.tag) {
                        case 0: { // None
                            static_array<unsigned char,5l> v715;
                            long v716; long v717;
                            Tuple7 tmp36 = Tuple7(0l, 0l);
                            v716 = tmp36.v0; v717 = tmp36.v1;
                            while (while_method_9(v716)){
                                bool v719;
                                v719 = 0l <= v716;
                                bool v721;
                                if (v719){
                                    bool v720;
                                    v720 = v716 < 7l;
                                    v721 = v720;
                                } else {
                                    v721 = false;
                                }
                                bool v722;
                                v722 = v721 == false;
                                if (v722){
                                    assert("The read index needs to be in range for the static array." && v721);
                                } else {
                                }
                                unsigned char v723;
                                v723 = v120.v[v716];
                                unsigned char v724;
                                v724 = v723 % 4u;
                                bool v725;
                                v725 = v724 == 0u;
                                bool v727;
                                if (v725){
                                    bool v726;
                                    v726 = v717 < 5l;
                                    v727 = v726;
                                } else {
                                    v727 = false;
                                }
                                long v733;
                                if (v727){
                                    bool v728;
                                    v728 = 0l <= v717;
                                    bool v730;
                                    if (v728){
                                        bool v729;
                                        v729 = v717 < 5l;
                                        v730 = v729;
                                    } else {
                                        v730 = false;
                                    }
                                    bool v731;
                                    v731 = v730 == false;
                                    if (v731){
                                        assert("The read index needs to be in range for the static array." && v730);
                                    } else {
                                    }
                                    v715.v[v717] = v723;
                                    long v732;
                                    v732 = v717 + 1l;
                                    v733 = v732;
                                } else {
                                    v733 = v717;
                                }
                                v717 = v733;
                                v716 += 1l ;
                            }
                            bool v734;
                            v734 = v717 == 5l;
                            US11 v737;
                            if (v734){
                                v737 = US11_1(v715);
                            } else {
                                v737 = US11_0();
                            }
                            static_array<unsigned char,5l> v738;
                            long v739; long v740;
                            Tuple7 tmp37 = Tuple7(0l, 0l);
                            v739 = tmp37.v0; v740 = tmp37.v1;
                            while (while_method_9(v739)){
                                bool v742;
                                v742 = 0l <= v739;
                                bool v744;
                                if (v742){
                                    bool v743;
                                    v743 = v739 < 7l;
                                    v744 = v743;
                                } else {
                                    v744 = false;
                                }
                                bool v745;
                                v745 = v744 == false;
                                if (v745){
                                    assert("The read index needs to be in range for the static array." && v744);
                                } else {
                                }
                                unsigned char v746;
                                v746 = v120.v[v739];
                                unsigned char v747;
                                v747 = v746 % 4u;
                                bool v748;
                                v748 = v747 == 1u;
                                bool v750;
                                if (v748){
                                    bool v749;
                                    v749 = v740 < 5l;
                                    v750 = v749;
                                } else {
                                    v750 = false;
                                }
                                long v756;
                                if (v750){
                                    bool v751;
                                    v751 = 0l <= v740;
                                    bool v753;
                                    if (v751){
                                        bool v752;
                                        v752 = v740 < 5l;
                                        v753 = v752;
                                    } else {
                                        v753 = false;
                                    }
                                    bool v754;
                                    v754 = v753 == false;
                                    if (v754){
                                        assert("The read index needs to be in range for the static array." && v753);
                                    } else {
                                    }
                                    v738.v[v740] = v746;
                                    long v755;
                                    v755 = v740 + 1l;
                                    v756 = v755;
                                } else {
                                    v756 = v740;
                                }
                                v740 = v756;
                                v739 += 1l ;
                            }
                            bool v757;
                            v757 = v740 == 5l;
                            US11 v760;
                            if (v757){
                                v760 = US11_1(v738);
                            } else {
                                v760 = US11_0();
                            }
                            US11 v793;
                            switch (v737.tag) {
                                case 0: { // None
                                    v793 = v760;
                                    break;
                                }
                                case 1: { // Some
                                    static_array<unsigned char,5l> v761 = v737.v.case1.v0;
                                    switch (v760.tag) {
                                        case 0: { // None
                                            v793 = v737;
                                            break;
                                        }
                                        case 1: { // Some
                                            static_array<unsigned char,5l> v762 = v760.v.case1.v0;
                                            US10 v763;
                                            v763 = US10_0();
                                            long v764; US10 v765;
                                            Tuple14 tmp38 = Tuple14(0l, v763);
                                            v764 = tmp38.v0; v765 = tmp38.v1;
                                            while (while_method_2(v764)){
                                                bool v767;
                                                v767 = 0l <= v764;
                                                bool v769;
                                                if (v767){
                                                    bool v768;
                                                    v768 = v764 < 5l;
                                                    v769 = v768;
                                                } else {
                                                    v769 = false;
                                                }
                                                bool v770;
                                                v770 = v769 == false;
                                                if (v770){
                                                    assert("The read index needs to be in range for the static array." && v769);
                                                } else {
                                                }
                                                unsigned char v771;
                                                v771 = v761.v[v764];
                                                bool v773;
                                                if (v767){
                                                    bool v772;
                                                    v772 = v764 < 5l;
                                                    v773 = v772;
                                                } else {
                                                    v773 = false;
                                                }
                                                bool v774;
                                                v774 = v773 == false;
                                                if (v774){
                                                    assert("The read index needs to be in range for the static array." && v773);
                                                } else {
                                                }
                                                unsigned char v775;
                                                v775 = v762.v[v764];
                                                US10 v786;
                                                switch (v765.tag) {
                                                    case 0: { // Eq
                                                        unsigned char v776;
                                                        v776 = v771 / 4u;
                                                        unsigned char v777;
                                                        v777 = v775 / 4u;
                                                        bool v778;
                                                        v778 = v776 < v777;
                                                        if (v778){
                                                            v786 = US10_2();
                                                        } else {
                                                            bool v780;
                                                            v780 = v776 > v777;
                                                            if (v780){
                                                                v786 = US10_1();
                                                            } else {
                                                                v786 = US10_0();
                                                            }
                                                        }
                                                        break;
                                                    }
                                                    default: {
                                                        break;
                                                    }
                                                }
                                                v765 = v786;
                                                v764 += 1l ;
                                            }
                                            bool v787;
                                            switch (v765.tag) {
                                                case 1: { // Gt
                                                    v787 = true;
                                                    break;
                                                }
                                                default: {
                                                    v787 = false;
                                                }
                                            }
                                            static_array<unsigned char,5l> v788;
                                            if (v787){
                                                v788 = v761;
                                            } else {
                                                v788 = v762;
                                            }
                                            v793 = US11_1(v788);
                                            break;
                                        }
                                        default: {
                                            assert("Invalid tag." && false);
                                        }
                                    }
                                    break;
                                }
                                default: {
                                    assert("Invalid tag." && false);
                                }
                            }
                            static_array<unsigned char,5l> v794;
                            long v795; long v796;
                            Tuple7 tmp39 = Tuple7(0l, 0l);
                            v795 = tmp39.v0; v796 = tmp39.v1;
                            while (while_method_9(v795)){
                                bool v798;
                                v798 = 0l <= v795;
                                bool v800;
                                if (v798){
                                    bool v799;
                                    v799 = v795 < 7l;
                                    v800 = v799;
                                } else {
                                    v800 = false;
                                }
                                bool v801;
                                v801 = v800 == false;
                                if (v801){
                                    assert("The read index needs to be in range for the static array." && v800);
                                } else {
                                }
                                unsigned char v802;
                                v802 = v120.v[v795];
                                unsigned char v803;
                                v803 = v802 % 4u;
                                bool v804;
                                v804 = v803 == 2u;
                                bool v806;
                                if (v804){
                                    bool v805;
                                    v805 = v796 < 5l;
                                    v806 = v805;
                                } else {
                                    v806 = false;
                                }
                                long v812;
                                if (v806){
                                    bool v807;
                                    v807 = 0l <= v796;
                                    bool v809;
                                    if (v807){
                                        bool v808;
                                        v808 = v796 < 5l;
                                        v809 = v808;
                                    } else {
                                        v809 = false;
                                    }
                                    bool v810;
                                    v810 = v809 == false;
                                    if (v810){
                                        assert("The read index needs to be in range for the static array." && v809);
                                    } else {
                                    }
                                    v794.v[v796] = v802;
                                    long v811;
                                    v811 = v796 + 1l;
                                    v812 = v811;
                                } else {
                                    v812 = v796;
                                }
                                v796 = v812;
                                v795 += 1l ;
                            }
                            bool v813;
                            v813 = v796 == 5l;
                            US11 v816;
                            if (v813){
                                v816 = US11_1(v794);
                            } else {
                                v816 = US11_0();
                            }
                            US11 v849;
                            switch (v793.tag) {
                                case 0: { // None
                                    v849 = v816;
                                    break;
                                }
                                case 1: { // Some
                                    static_array<unsigned char,5l> v817 = v793.v.case1.v0;
                                    switch (v816.tag) {
                                        case 0: { // None
                                            v849 = v793;
                                            break;
                                        }
                                        case 1: { // Some
                                            static_array<unsigned char,5l> v818 = v816.v.case1.v0;
                                            US10 v819;
                                            v819 = US10_0();
                                            long v820; US10 v821;
                                            Tuple14 tmp40 = Tuple14(0l, v819);
                                            v820 = tmp40.v0; v821 = tmp40.v1;
                                            while (while_method_2(v820)){
                                                bool v823;
                                                v823 = 0l <= v820;
                                                bool v825;
                                                if (v823){
                                                    bool v824;
                                                    v824 = v820 < 5l;
                                                    v825 = v824;
                                                } else {
                                                    v825 = false;
                                                }
                                                bool v826;
                                                v826 = v825 == false;
                                                if (v826){
                                                    assert("The read index needs to be in range for the static array." && v825);
                                                } else {
                                                }
                                                unsigned char v827;
                                                v827 = v817.v[v820];
                                                bool v829;
                                                if (v823){
                                                    bool v828;
                                                    v828 = v820 < 5l;
                                                    v829 = v828;
                                                } else {
                                                    v829 = false;
                                                }
                                                bool v830;
                                                v830 = v829 == false;
                                                if (v830){
                                                    assert("The read index needs to be in range for the static array." && v829);
                                                } else {
                                                }
                                                unsigned char v831;
                                                v831 = v818.v[v820];
                                                US10 v842;
                                                switch (v821.tag) {
                                                    case 0: { // Eq
                                                        unsigned char v832;
                                                        v832 = v827 / 4u;
                                                        unsigned char v833;
                                                        v833 = v831 / 4u;
                                                        bool v834;
                                                        v834 = v832 < v833;
                                                        if (v834){
                                                            v842 = US10_2();
                                                        } else {
                                                            bool v836;
                                                            v836 = v832 > v833;
                                                            if (v836){
                                                                v842 = US10_1();
                                                            } else {
                                                                v842 = US10_0();
                                                            }
                                                        }
                                                        break;
                                                    }
                                                    default: {
                                                        break;
                                                    }
                                                }
                                                v821 = v842;
                                                v820 += 1l ;
                                            }
                                            bool v843;
                                            switch (v821.tag) {
                                                case 1: { // Gt
                                                    v843 = true;
                                                    break;
                                                }
                                                default: {
                                                    v843 = false;
                                                }
                                            }
                                            static_array<unsigned char,5l> v844;
                                            if (v843){
                                                v844 = v817;
                                            } else {
                                                v844 = v818;
                                            }
                                            v849 = US11_1(v844);
                                            break;
                                        }
                                        default: {
                                            assert("Invalid tag." && false);
                                        }
                                    }
                                    break;
                                }
                                default: {
                                    assert("Invalid tag." && false);
                                }
                            }
                            static_array<unsigned char,5l> v850;
                            long v851; long v852;
                            Tuple7 tmp41 = Tuple7(0l, 0l);
                            v851 = tmp41.v0; v852 = tmp41.v1;
                            while (while_method_9(v851)){
                                bool v854;
                                v854 = 0l <= v851;
                                bool v856;
                                if (v854){
                                    bool v855;
                                    v855 = v851 < 7l;
                                    v856 = v855;
                                } else {
                                    v856 = false;
                                }
                                bool v857;
                                v857 = v856 == false;
                                if (v857){
                                    assert("The read index needs to be in range for the static array." && v856);
                                } else {
                                }
                                unsigned char v858;
                                v858 = v120.v[v851];
                                unsigned char v859;
                                v859 = v858 % 4u;
                                bool v860;
                                v860 = v859 == 3u;
                                bool v862;
                                if (v860){
                                    bool v861;
                                    v861 = v852 < 5l;
                                    v862 = v861;
                                } else {
                                    v862 = false;
                                }
                                long v868;
                                if (v862){
                                    bool v863;
                                    v863 = 0l <= v852;
                                    bool v865;
                                    if (v863){
                                        bool v864;
                                        v864 = v852 < 5l;
                                        v865 = v864;
                                    } else {
                                        v865 = false;
                                    }
                                    bool v866;
                                    v866 = v865 == false;
                                    if (v866){
                                        assert("The read index needs to be in range for the static array." && v865);
                                    } else {
                                    }
                                    v850.v[v852] = v858;
                                    long v867;
                                    v867 = v852 + 1l;
                                    v868 = v867;
                                } else {
                                    v868 = v852;
                                }
                                v852 = v868;
                                v851 += 1l ;
                            }
                            bool v869;
                            v869 = v852 == 5l;
                            US11 v872;
                            if (v869){
                                v872 = US11_1(v850);
                            } else {
                                v872 = US11_0();
                            }
                            US11 v905;
                            switch (v849.tag) {
                                case 0: { // None
                                    v905 = v872;
                                    break;
                                }
                                case 1: { // Some
                                    static_array<unsigned char,5l> v873 = v849.v.case1.v0;
                                    switch (v872.tag) {
                                        case 0: { // None
                                            v905 = v849;
                                            break;
                                        }
                                        case 1: { // Some
                                            static_array<unsigned char,5l> v874 = v872.v.case1.v0;
                                            US10 v875;
                                            v875 = US10_0();
                                            long v876; US10 v877;
                                            Tuple14 tmp42 = Tuple14(0l, v875);
                                            v876 = tmp42.v0; v877 = tmp42.v1;
                                            while (while_method_2(v876)){
                                                bool v879;
                                                v879 = 0l <= v876;
                                                bool v881;
                                                if (v879){
                                                    bool v880;
                                                    v880 = v876 < 5l;
                                                    v881 = v880;
                                                } else {
                                                    v881 = false;
                                                }
                                                bool v882;
                                                v882 = v881 == false;
                                                if (v882){
                                                    assert("The read index needs to be in range for the static array." && v881);
                                                } else {
                                                }
                                                unsigned char v883;
                                                v883 = v873.v[v876];
                                                bool v885;
                                                if (v879){
                                                    bool v884;
                                                    v884 = v876 < 5l;
                                                    v885 = v884;
                                                } else {
                                                    v885 = false;
                                                }
                                                bool v886;
                                                v886 = v885 == false;
                                                if (v886){
                                                    assert("The read index needs to be in range for the static array." && v885);
                                                } else {
                                                }
                                                unsigned char v887;
                                                v887 = v874.v[v876];
                                                US10 v898;
                                                switch (v877.tag) {
                                                    case 0: { // Eq
                                                        unsigned char v888;
                                                        v888 = v883 / 4u;
                                                        unsigned char v889;
                                                        v889 = v887 / 4u;
                                                        bool v890;
                                                        v890 = v888 < v889;
                                                        if (v890){
                                                            v898 = US10_2();
                                                        } else {
                                                            bool v892;
                                                            v892 = v888 > v889;
                                                            if (v892){
                                                                v898 = US10_1();
                                                            } else {
                                                                v898 = US10_0();
                                                            }
                                                        }
                                                        break;
                                                    }
                                                    default: {
                                                        break;
                                                    }
                                                }
                                                v877 = v898;
                                                v876 += 1l ;
                                            }
                                            bool v899;
                                            switch (v877.tag) {
                                                case 1: { // Gt
                                                    v899 = true;
                                                    break;
                                                }
                                                default: {
                                                    v899 = false;
                                                }
                                            }
                                            static_array<unsigned char,5l> v900;
                                            if (v899){
                                                v900 = v873;
                                            } else {
                                                v900 = v874;
                                            }
                                            v905 = US11_1(v900);
                                            break;
                                        }
                                        default: {
                                            assert("Invalid tag." && false);
                                        }
                                    }
                                    break;
                                }
                                default: {
                                    assert("Invalid tag." && false);
                                }
                            }
                            switch (v905.tag) {
                                case 0: { // None
                                    static_array<unsigned char,5l> v907;
                                    long v908; long v909; unsigned char v910;
                                    Tuple13 tmp43 = Tuple13(0l, 0l, 12u);
                                    v908 = tmp43.v0; v909 = tmp43.v1; v910 = tmp43.v2;
                                    while (while_method_9(v908)){
                                        bool v912;
                                        v912 = 0l <= v908;
                                        bool v914;
                                        if (v912){
                                            bool v913;
                                            v913 = v908 < 7l;
                                            v914 = v913;
                                        } else {
                                            v914 = false;
                                        }
                                        bool v915;
                                        v915 = v914 == false;
                                        if (v915){
                                            assert("The read index needs to be in range for the static array." && v914);
                                        } else {
                                        }
                                        unsigned char v916;
                                        v916 = v120.v[v908];
                                        bool v917;
                                        v917 = v909 < 5l;
                                        long v933; unsigned char v934;
                                        if (v917){
                                            unsigned char v918;
                                            v918 = v916 / 4u;
                                            unsigned char v919;
                                            v919 = v918 - 1u;
                                            bool v920;
                                            v920 = v910 == v919;
                                            bool v921;
                                            v921 = v920 != true;
                                            if (v921){
                                                bool v922;
                                                v922 = v910 == v918;
                                                long v923;
                                                if (v922){
                                                    v923 = v909;
                                                } else {
                                                    v923 = 0l;
                                                }
                                                bool v924;
                                                v924 = 0l <= v923;
                                                bool v926;
                                                if (v924){
                                                    bool v925;
                                                    v925 = v923 < 5l;
                                                    v926 = v925;
                                                } else {
                                                    v926 = false;
                                                }
                                                bool v927;
                                                v927 = v926 == false;
                                                if (v927){
                                                    assert("The read index needs to be in range for the static array." && v926);
                                                } else {
                                                }
                                                v907.v[v923] = v916;
                                                long v928;
                                                v928 = v923 + 1l;
                                                v933 = v928; v934 = v919;
                                            } else {
                                                v933 = v909; v934 = v910;
                                            }
                                        } else {
                                            break;
                                        }
                                        v909 = v933;
                                        v910 = v934;
                                        v908 += 1l ;
                                    }
                                    bool v935;
                                    v935 = v909 == 4l;
                                    bool v943;
                                    if (v935){
                                        unsigned char v936;
                                        v936 = v910 + 1u;
                                        bool v937;
                                        v937 = v936 == 0u;
                                        if (v937){
                                            unsigned char v938;
                                            v938 = v120.v[0l];
                                            unsigned char v939;
                                            v939 = v938 / 4u;
                                            bool v940;
                                            v940 = v939 == 12u;
                                            if (v940){
                                                v907.v[4l] = v938;
                                                v943 = true;
                                            } else {
                                                v943 = false;
                                            }
                                        } else {
                                            v943 = false;
                                        }
                                    } else {
                                        v943 = false;
                                    }
                                    US11 v949;
                                    if (v943){
                                        v949 = US11_1(v907);
                                    } else {
                                        bool v945;
                                        v945 = v909 == 5l;
                                        if (v945){
                                            v949 = US11_1(v907);
                                        } else {
                                            v949 = US11_0();
                                        }
                                    }
                                    switch (v949.tag) {
                                        case 0: { // None
                                            static_array<unsigned char,3l> v951;
                                            static_array<unsigned char,4l> v952;
                                            long v953; long v954; long v955; unsigned char v956;
                                            Tuple15 tmp44 = Tuple15(0l, 0l, 0l, 12u);
                                            v953 = tmp44.v0; v954 = tmp44.v1; v955 = tmp44.v2; v956 = tmp44.v3;
                                            while (while_method_9(v953)){
                                                bool v958;
                                                v958 = 0l <= v953;
                                                bool v960;
                                                if (v958){
                                                    bool v959;
                                                    v959 = v953 < 7l;
                                                    v960 = v959;
                                                } else {
                                                    v960 = false;
                                                }
                                                bool v961;
                                                v961 = v960 == false;
                                                if (v961){
                                                    assert("The read index needs to be in range for the static array." && v960);
                                                } else {
                                                }
                                                unsigned char v962;
                                                v962 = v120.v[v953];
                                                bool v963;
                                                v963 = v955 < 3l;
                                                long v975; long v976; unsigned char v977;
                                                if (v963){
                                                    unsigned char v964;
                                                    v964 = v962 / 4u;
                                                    bool v965;
                                                    v965 = v956 == v964;
                                                    long v966;
                                                    if (v965){
                                                        v966 = v955;
                                                    } else {
                                                        v966 = 0l;
                                                    }
                                                    bool v967;
                                                    v967 = 0l <= v966;
                                                    bool v969;
                                                    if (v967){
                                                        bool v968;
                                                        v968 = v966 < 3l;
                                                        v969 = v968;
                                                    } else {
                                                        v969 = false;
                                                    }
                                                    bool v970;
                                                    v970 = v969 == false;
                                                    if (v970){
                                                        assert("The read index needs to be in range for the static array." && v969);
                                                    } else {
                                                    }
                                                    v951.v[v966] = v962;
                                                    long v971;
                                                    v971 = v966 + 1l;
                                                    v975 = v953; v976 = v971; v977 = v964;
                                                } else {
                                                    break;
                                                }
                                                v954 = v975;
                                                v955 = v976;
                                                v956 = v977;
                                                v953 += 1l ;
                                            }
                                            bool v978;
                                            v978 = v955 == 3l;
                                            US13 v996;
                                            if (v978){
                                                long v979;
                                                v979 = 0l;
                                                while (while_method_3(v979)){
                                                    long v981;
                                                    v981 = v954 + -2l;
                                                    bool v982;
                                                    v982 = v979 < v981;
                                                    long v983;
                                                    if (v982){
                                                        v983 = 0l;
                                                    } else {
                                                        v983 = 3l;
                                                    }
                                                    long v984;
                                                    v984 = v983 + v979;
                                                    bool v985;
                                                    v985 = 0l <= v984;
                                                    bool v987;
                                                    if (v985){
                                                        bool v986;
                                                        v986 = v984 < 7l;
                                                        v987 = v986;
                                                    } else {
                                                        v987 = false;
                                                    }
                                                    bool v988;
                                                    v988 = v987 == false;
                                                    if (v988){
                                                        assert("The read index needs to be in range for the static array." && v987);
                                                    } else {
                                                    }
                                                    unsigned char v989;
                                                    v989 = v120.v[v984];
                                                    bool v990;
                                                    v990 = 0l <= v979;
                                                    bool v992;
                                                    if (v990){
                                                        bool v991;
                                                        v991 = v979 < 4l;
                                                        v992 = v991;
                                                    } else {
                                                        v992 = false;
                                                    }
                                                    bool v993;
                                                    v993 = v992 == false;
                                                    if (v993){
                                                        assert("The read index needs to be in range for the static array." && v992);
                                                    } else {
                                                    }
                                                    v952.v[v979] = v989;
                                                    v979 += 1l ;
                                                }
                                                v996 = US13_1(v951, v952);
                                            } else {
                                                v996 = US13_0();
                                            }
                                            US11 v1036;
                                            switch (v996.tag) {
                                                case 0: { // None
                                                    v1036 = US11_0();
                                                    break;
                                                }
                                                case 1: { // Some
                                                    static_array<unsigned char,3l> v997 = v996.v.case1.v0; static_array<unsigned char,4l> v998 = v996.v.case1.v1;
                                                    static_array<unsigned char,2l> v999;
                                                    long v1000;
                                                    v1000 = 0l;
                                                    while (while_method_4(v1000)){
                                                        bool v1002;
                                                        v1002 = 0l <= v1000;
                                                        bool v1004;
                                                        if (v1002){
                                                            bool v1003;
                                                            v1003 = v1000 < 4l;
                                                            v1004 = v1003;
                                                        } else {
                                                            v1004 = false;
                                                        }
                                                        bool v1005;
                                                        v1005 = v1004 == false;
                                                        if (v1005){
                                                            assert("The read index needs to be in range for the static array." && v1004);
                                                        } else {
                                                        }
                                                        unsigned char v1006;
                                                        v1006 = v998.v[v1000];
                                                        bool v1008;
                                                        if (v1002){
                                                            bool v1007;
                                                            v1007 = v1000 < 2l;
                                                            v1008 = v1007;
                                                        } else {
                                                            v1008 = false;
                                                        }
                                                        bool v1009;
                                                        v1009 = v1008 == false;
                                                        if (v1009){
                                                            assert("The read index needs to be in range for the static array." && v1008);
                                                        } else {
                                                        }
                                                        v999.v[v1000] = v1006;
                                                        v1000 += 1l ;
                                                    }
                                                    static_array<unsigned char,5l> v1010;
                                                    long v1011;
                                                    v1011 = 0l;
                                                    while (while_method_1(v1011)){
                                                        bool v1013;
                                                        v1013 = 0l <= v1011;
                                                        bool v1015;
                                                        if (v1013){
                                                            bool v1014;
                                                            v1014 = v1011 < 3l;
                                                            v1015 = v1014;
                                                        } else {
                                                            v1015 = false;
                                                        }
                                                        bool v1016;
                                                        v1016 = v1015 == false;
                                                        if (v1016){
                                                            assert("The read index needs to be in range for the static array." && v1015);
                                                        } else {
                                                        }
                                                        unsigned char v1017;
                                                        v1017 = v997.v[v1011];
                                                        bool v1019;
                                                        if (v1013){
                                                            bool v1018;
                                                            v1018 = v1011 < 5l;
                                                            v1019 = v1018;
                                                        } else {
                                                            v1019 = false;
                                                        }
                                                        bool v1020;
                                                        v1020 = v1019 == false;
                                                        if (v1020){
                                                            assert("The read index needs to be in range for the static array." && v1019);
                                                        } else {
                                                        }
                                                        v1010.v[v1011] = v1017;
                                                        v1011 += 1l ;
                                                    }
                                                    long v1021;
                                                    v1021 = 0l;
                                                    while (while_method_4(v1021)){
                                                        bool v1023;
                                                        v1023 = 0l <= v1021;
                                                        bool v1025;
                                                        if (v1023){
                                                            bool v1024;
                                                            v1024 = v1021 < 2l;
                                                            v1025 = v1024;
                                                        } else {
                                                            v1025 = false;
                                                        }
                                                        bool v1026;
                                                        v1026 = v1025 == false;
                                                        if (v1026){
                                                            assert("The read index needs to be in range for the static array." && v1025);
                                                        } else {
                                                        }
                                                        unsigned char v1027;
                                                        v1027 = v999.v[v1021];
                                                        long v1028;
                                                        v1028 = 3l + v1021;
                                                        bool v1029;
                                                        v1029 = 0l <= v1028;
                                                        bool v1031;
                                                        if (v1029){
                                                            bool v1030;
                                                            v1030 = v1028 < 5l;
                                                            v1031 = v1030;
                                                        } else {
                                                            v1031 = false;
                                                        }
                                                        bool v1032;
                                                        v1032 = v1031 == false;
                                                        if (v1032){
                                                            assert("The read index needs to be in range for the static array." && v1031);
                                                        } else {
                                                        }
                                                        v1010.v[v1028] = v1027;
                                                        v1021 += 1l ;
                                                    }
                                                    v1036 = US11_1(v1010);
                                                    break;
                                                }
                                                default: {
                                                    assert("Invalid tag." && false);
                                                }
                                            }
                                            switch (v1036.tag) {
                                                case 0: { // None
                                                    static_array<unsigned char,2l> v1038;
                                                    static_array<unsigned char,5l> v1039;
                                                    long v1040; long v1041; long v1042; unsigned char v1043;
                                                    Tuple15 tmp45 = Tuple15(0l, 0l, 0l, 12u);
                                                    v1040 = tmp45.v0; v1041 = tmp45.v1; v1042 = tmp45.v2; v1043 = tmp45.v3;
                                                    while (while_method_9(v1040)){
                                                        bool v1045;
                                                        v1045 = 0l <= v1040;
                                                        bool v1047;
                                                        if (v1045){
                                                            bool v1046;
                                                            v1046 = v1040 < 7l;
                                                            v1047 = v1046;
                                                        } else {
                                                            v1047 = false;
                                                        }
                                                        bool v1048;
                                                        v1048 = v1047 == false;
                                                        if (v1048){
                                                            assert("The read index needs to be in range for the static array." && v1047);
                                                        } else {
                                                        }
                                                        unsigned char v1049;
                                                        v1049 = v120.v[v1040];
                                                        bool v1050;
                                                        v1050 = v1042 < 2l;
                                                        long v1062; long v1063; unsigned char v1064;
                                                        if (v1050){
                                                            unsigned char v1051;
                                                            v1051 = v1049 / 4u;
                                                            bool v1052;
                                                            v1052 = v1043 == v1051;
                                                            long v1053;
                                                            if (v1052){
                                                                v1053 = v1042;
                                                            } else {
                                                                v1053 = 0l;
                                                            }
                                                            bool v1054;
                                                            v1054 = 0l <= v1053;
                                                            bool v1056;
                                                            if (v1054){
                                                                bool v1055;
                                                                v1055 = v1053 < 2l;
                                                                v1056 = v1055;
                                                            } else {
                                                                v1056 = false;
                                                            }
                                                            bool v1057;
                                                            v1057 = v1056 == false;
                                                            if (v1057){
                                                                assert("The read index needs to be in range for the static array." && v1056);
                                                            } else {
                                                            }
                                                            v1038.v[v1053] = v1049;
                                                            long v1058;
                                                            v1058 = v1053 + 1l;
                                                            v1062 = v1040; v1063 = v1058; v1064 = v1051;
                                                        } else {
                                                            break;
                                                        }
                                                        v1041 = v1062;
                                                        v1042 = v1063;
                                                        v1043 = v1064;
                                                        v1040 += 1l ;
                                                    }
                                                    bool v1065;
                                                    v1065 = v1042 == 2l;
                                                    US15 v1083;
                                                    if (v1065){
                                                        long v1066;
                                                        v1066 = 0l;
                                                        while (while_method_2(v1066)){
                                                            long v1068;
                                                            v1068 = v1041 + -1l;
                                                            bool v1069;
                                                            v1069 = v1066 < v1068;
                                                            long v1070;
                                                            if (v1069){
                                                                v1070 = 0l;
                                                            } else {
                                                                v1070 = 2l;
                                                            }
                                                            long v1071;
                                                            v1071 = v1070 + v1066;
                                                            bool v1072;
                                                            v1072 = 0l <= v1071;
                                                            bool v1074;
                                                            if (v1072){
                                                                bool v1073;
                                                                v1073 = v1071 < 7l;
                                                                v1074 = v1073;
                                                            } else {
                                                                v1074 = false;
                                                            }
                                                            bool v1075;
                                                            v1075 = v1074 == false;
                                                            if (v1075){
                                                                assert("The read index needs to be in range for the static array." && v1074);
                                                            } else {
                                                            }
                                                            unsigned char v1076;
                                                            v1076 = v120.v[v1071];
                                                            bool v1077;
                                                            v1077 = 0l <= v1066;
                                                            bool v1079;
                                                            if (v1077){
                                                                bool v1078;
                                                                v1078 = v1066 < 5l;
                                                                v1079 = v1078;
                                                            } else {
                                                                v1079 = false;
                                                            }
                                                            bool v1080;
                                                            v1080 = v1079 == false;
                                                            if (v1080){
                                                                assert("The read index needs to be in range for the static array." && v1079);
                                                            } else {
                                                            }
                                                            v1039.v[v1066] = v1076;
                                                            v1066 += 1l ;
                                                        }
                                                        v1083 = US15_1(v1038, v1039);
                                                    } else {
                                                        v1083 = US15_0();
                                                    }
                                                    US11 v1186;
                                                    switch (v1083.tag) {
                                                        case 0: { // None
                                                            v1186 = US11_0();
                                                            break;
                                                        }
                                                        case 1: { // Some
                                                            static_array<unsigned char,2l> v1084 = v1083.v.case1.v0; static_array<unsigned char,5l> v1085 = v1083.v.case1.v1;
                                                            static_array<unsigned char,2l> v1086;
                                                            static_array<unsigned char,3l> v1087;
                                                            long v1088; long v1089; long v1090; unsigned char v1091;
                                                            Tuple15 tmp46 = Tuple15(0l, 0l, 0l, 12u);
                                                            v1088 = tmp46.v0; v1089 = tmp46.v1; v1090 = tmp46.v2; v1091 = tmp46.v3;
                                                            while (while_method_2(v1088)){
                                                                bool v1093;
                                                                v1093 = 0l <= v1088;
                                                                bool v1095;
                                                                if (v1093){
                                                                    bool v1094;
                                                                    v1094 = v1088 < 5l;
                                                                    v1095 = v1094;
                                                                } else {
                                                                    v1095 = false;
                                                                }
                                                                bool v1096;
                                                                v1096 = v1095 == false;
                                                                if (v1096){
                                                                    assert("The read index needs to be in range for the static array." && v1095);
                                                                } else {
                                                                }
                                                                unsigned char v1097;
                                                                v1097 = v1085.v[v1088];
                                                                bool v1098;
                                                                v1098 = v1090 < 2l;
                                                                long v1110; long v1111; unsigned char v1112;
                                                                if (v1098){
                                                                    unsigned char v1099;
                                                                    v1099 = v1097 / 4u;
                                                                    bool v1100;
                                                                    v1100 = v1091 == v1099;
                                                                    long v1101;
                                                                    if (v1100){
                                                                        v1101 = v1090;
                                                                    } else {
                                                                        v1101 = 0l;
                                                                    }
                                                                    bool v1102;
                                                                    v1102 = 0l <= v1101;
                                                                    bool v1104;
                                                                    if (v1102){
                                                                        bool v1103;
                                                                        v1103 = v1101 < 2l;
                                                                        v1104 = v1103;
                                                                    } else {
                                                                        v1104 = false;
                                                                    }
                                                                    bool v1105;
                                                                    v1105 = v1104 == false;
                                                                    if (v1105){
                                                                        assert("The read index needs to be in range for the static array." && v1104);
                                                                    } else {
                                                                    }
                                                                    v1086.v[v1101] = v1097;
                                                                    long v1106;
                                                                    v1106 = v1101 + 1l;
                                                                    v1110 = v1088; v1111 = v1106; v1112 = v1099;
                                                                } else {
                                                                    break;
                                                                }
                                                                v1089 = v1110;
                                                                v1090 = v1111;
                                                                v1091 = v1112;
                                                                v1088 += 1l ;
                                                            }
                                                            bool v1113;
                                                            v1113 = v1090 == 2l;
                                                            US16 v1131;
                                                            if (v1113){
                                                                long v1114;
                                                                v1114 = 0l;
                                                                while (while_method_1(v1114)){
                                                                    long v1116;
                                                                    v1116 = v1089 + -1l;
                                                                    bool v1117;
                                                                    v1117 = v1114 < v1116;
                                                                    long v1118;
                                                                    if (v1117){
                                                                        v1118 = 0l;
                                                                    } else {
                                                                        v1118 = 2l;
                                                                    }
                                                                    long v1119;
                                                                    v1119 = v1118 + v1114;
                                                                    bool v1120;
                                                                    v1120 = 0l <= v1119;
                                                                    bool v1122;
                                                                    if (v1120){
                                                                        bool v1121;
                                                                        v1121 = v1119 < 5l;
                                                                        v1122 = v1121;
                                                                    } else {
                                                                        v1122 = false;
                                                                    }
                                                                    bool v1123;
                                                                    v1123 = v1122 == false;
                                                                    if (v1123){
                                                                        assert("The read index needs to be in range for the static array." && v1122);
                                                                    } else {
                                                                    }
                                                                    unsigned char v1124;
                                                                    v1124 = v1085.v[v1119];
                                                                    bool v1125;
                                                                    v1125 = 0l <= v1114;
                                                                    bool v1127;
                                                                    if (v1125){
                                                                        bool v1126;
                                                                        v1126 = v1114 < 3l;
                                                                        v1127 = v1126;
                                                                    } else {
                                                                        v1127 = false;
                                                                    }
                                                                    bool v1128;
                                                                    v1128 = v1127 == false;
                                                                    if (v1128){
                                                                        assert("The read index needs to be in range for the static array." && v1127);
                                                                    } else {
                                                                    }
                                                                    v1087.v[v1114] = v1124;
                                                                    v1114 += 1l ;
                                                                }
                                                                v1131 = US16_1(v1086, v1087);
                                                            } else {
                                                                v1131 = US16_0();
                                                            }
                                                            switch (v1131.tag) {
                                                                case 0: { // None
                                                                    v1186 = US11_0();
                                                                    break;
                                                                }
                                                                case 1: { // Some
                                                                    static_array<unsigned char,2l> v1132 = v1131.v.case1.v0; static_array<unsigned char,3l> v1133 = v1131.v.case1.v1;
                                                                    static_array<unsigned char,1l> v1134;
                                                                    long v1135;
                                                                    v1135 = 0l;
                                                                    while (while_method_5(v1135)){
                                                                        bool v1137;
                                                                        v1137 = 0l <= v1135;
                                                                        bool v1139;
                                                                        if (v1137){
                                                                            bool v1138;
                                                                            v1138 = v1135 < 3l;
                                                                            v1139 = v1138;
                                                                        } else {
                                                                            v1139 = false;
                                                                        }
                                                                        bool v1140;
                                                                        v1140 = v1139 == false;
                                                                        if (v1140){
                                                                            assert("The read index needs to be in range for the static array." && v1139);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1141;
                                                                        v1141 = v1133.v[v1135];
                                                                        bool v1143;
                                                                        if (v1137){
                                                                            bool v1142;
                                                                            v1142 = v1135 < 1l;
                                                                            v1143 = v1142;
                                                                        } else {
                                                                            v1143 = false;
                                                                        }
                                                                        bool v1144;
                                                                        v1144 = v1143 == false;
                                                                        if (v1144){
                                                                            assert("The read index needs to be in range for the static array." && v1143);
                                                                        } else {
                                                                        }
                                                                        v1134.v[v1135] = v1141;
                                                                        v1135 += 1l ;
                                                                    }
                                                                    static_array<unsigned char,5l> v1145;
                                                                    long v1146;
                                                                    v1146 = 0l;
                                                                    while (while_method_4(v1146)){
                                                                        bool v1148;
                                                                        v1148 = 0l <= v1146;
                                                                        bool v1150;
                                                                        if (v1148){
                                                                            bool v1149;
                                                                            v1149 = v1146 < 2l;
                                                                            v1150 = v1149;
                                                                        } else {
                                                                            v1150 = false;
                                                                        }
                                                                        bool v1151;
                                                                        v1151 = v1150 == false;
                                                                        if (v1151){
                                                                            assert("The read index needs to be in range for the static array." && v1150);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1152;
                                                                        v1152 = v1084.v[v1146];
                                                                        bool v1154;
                                                                        if (v1148){
                                                                            bool v1153;
                                                                            v1153 = v1146 < 5l;
                                                                            v1154 = v1153;
                                                                        } else {
                                                                            v1154 = false;
                                                                        }
                                                                        bool v1155;
                                                                        v1155 = v1154 == false;
                                                                        if (v1155){
                                                                            assert("The read index needs to be in range for the static array." && v1154);
                                                                        } else {
                                                                        }
                                                                        v1145.v[v1146] = v1152;
                                                                        v1146 += 1l ;
                                                                    }
                                                                    long v1156;
                                                                    v1156 = 0l;
                                                                    while (while_method_4(v1156)){
                                                                        bool v1158;
                                                                        v1158 = 0l <= v1156;
                                                                        bool v1160;
                                                                        if (v1158){
                                                                            bool v1159;
                                                                            v1159 = v1156 < 2l;
                                                                            v1160 = v1159;
                                                                        } else {
                                                                            v1160 = false;
                                                                        }
                                                                        bool v1161;
                                                                        v1161 = v1160 == false;
                                                                        if (v1161){
                                                                            assert("The read index needs to be in range for the static array." && v1160);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1162;
                                                                        v1162 = v1132.v[v1156];
                                                                        long v1163;
                                                                        v1163 = 2l + v1156;
                                                                        bool v1164;
                                                                        v1164 = 0l <= v1163;
                                                                        bool v1166;
                                                                        if (v1164){
                                                                            bool v1165;
                                                                            v1165 = v1163 < 5l;
                                                                            v1166 = v1165;
                                                                        } else {
                                                                            v1166 = false;
                                                                        }
                                                                        bool v1167;
                                                                        v1167 = v1166 == false;
                                                                        if (v1167){
                                                                            assert("The read index needs to be in range for the static array." && v1166);
                                                                        } else {
                                                                        }
                                                                        v1145.v[v1163] = v1162;
                                                                        v1156 += 1l ;
                                                                    }
                                                                    long v1168;
                                                                    v1168 = 0l;
                                                                    while (while_method_5(v1168)){
                                                                        bool v1170;
                                                                        v1170 = 0l <= v1168;
                                                                        bool v1172;
                                                                        if (v1170){
                                                                            bool v1171;
                                                                            v1171 = v1168 < 1l;
                                                                            v1172 = v1171;
                                                                        } else {
                                                                            v1172 = false;
                                                                        }
                                                                        bool v1173;
                                                                        v1173 = v1172 == false;
                                                                        if (v1173){
                                                                            assert("The read index needs to be in range for the static array." && v1172);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1174;
                                                                        v1174 = v1134.v[v1168];
                                                                        long v1175;
                                                                        v1175 = 4l + v1168;
                                                                        bool v1176;
                                                                        v1176 = 0l <= v1175;
                                                                        bool v1178;
                                                                        if (v1176){
                                                                            bool v1177;
                                                                            v1177 = v1175 < 5l;
                                                                            v1178 = v1177;
                                                                        } else {
                                                                            v1178 = false;
                                                                        }
                                                                        bool v1179;
                                                                        v1179 = v1178 == false;
                                                                        if (v1179){
                                                                            assert("The read index needs to be in range for the static array." && v1178);
                                                                        } else {
                                                                        }
                                                                        v1145.v[v1175] = v1174;
                                                                        v1168 += 1l ;
                                                                    }
                                                                    v1186 = US11_1(v1145);
                                                                    break;
                                                                }
                                                                default: {
                                                                    assert("Invalid tag." && false);
                                                                }
                                                            }
                                                            break;
                                                        }
                                                        default: {
                                                            assert("Invalid tag." && false);
                                                        }
                                                    }
                                                    switch (v1186.tag) {
                                                        case 0: { // None
                                                            static_array<unsigned char,2l> v1188;
                                                            static_array<unsigned char,5l> v1189;
                                                            long v1190; long v1191; long v1192; unsigned char v1193;
                                                            Tuple15 tmp47 = Tuple15(0l, 0l, 0l, 12u);
                                                            v1190 = tmp47.v0; v1191 = tmp47.v1; v1192 = tmp47.v2; v1193 = tmp47.v3;
                                                            while (while_method_9(v1190)){
                                                                bool v1195;
                                                                v1195 = 0l <= v1190;
                                                                bool v1197;
                                                                if (v1195){
                                                                    bool v1196;
                                                                    v1196 = v1190 < 7l;
                                                                    v1197 = v1196;
                                                                } else {
                                                                    v1197 = false;
                                                                }
                                                                bool v1198;
                                                                v1198 = v1197 == false;
                                                                if (v1198){
                                                                    assert("The read index needs to be in range for the static array." && v1197);
                                                                } else {
                                                                }
                                                                unsigned char v1199;
                                                                v1199 = v120.v[v1190];
                                                                bool v1200;
                                                                v1200 = v1192 < 2l;
                                                                long v1212; long v1213; unsigned char v1214;
                                                                if (v1200){
                                                                    unsigned char v1201;
                                                                    v1201 = v1199 / 4u;
                                                                    bool v1202;
                                                                    v1202 = v1193 == v1201;
                                                                    long v1203;
                                                                    if (v1202){
                                                                        v1203 = v1192;
                                                                    } else {
                                                                        v1203 = 0l;
                                                                    }
                                                                    bool v1204;
                                                                    v1204 = 0l <= v1203;
                                                                    bool v1206;
                                                                    if (v1204){
                                                                        bool v1205;
                                                                        v1205 = v1203 < 2l;
                                                                        v1206 = v1205;
                                                                    } else {
                                                                        v1206 = false;
                                                                    }
                                                                    bool v1207;
                                                                    v1207 = v1206 == false;
                                                                    if (v1207){
                                                                        assert("The read index needs to be in range for the static array." && v1206);
                                                                    } else {
                                                                    }
                                                                    v1188.v[v1203] = v1199;
                                                                    long v1208;
                                                                    v1208 = v1203 + 1l;
                                                                    v1212 = v1190; v1213 = v1208; v1214 = v1201;
                                                                } else {
                                                                    break;
                                                                }
                                                                v1191 = v1212;
                                                                v1192 = v1213;
                                                                v1193 = v1214;
                                                                v1190 += 1l ;
                                                            }
                                                            bool v1215;
                                                            v1215 = v1192 == 2l;
                                                            US15 v1233;
                                                            if (v1215){
                                                                long v1216;
                                                                v1216 = 0l;
                                                                while (while_method_2(v1216)){
                                                                    long v1218;
                                                                    v1218 = v1191 + -1l;
                                                                    bool v1219;
                                                                    v1219 = v1216 < v1218;
                                                                    long v1220;
                                                                    if (v1219){
                                                                        v1220 = 0l;
                                                                    } else {
                                                                        v1220 = 2l;
                                                                    }
                                                                    long v1221;
                                                                    v1221 = v1220 + v1216;
                                                                    bool v1222;
                                                                    v1222 = 0l <= v1221;
                                                                    bool v1224;
                                                                    if (v1222){
                                                                        bool v1223;
                                                                        v1223 = v1221 < 7l;
                                                                        v1224 = v1223;
                                                                    } else {
                                                                        v1224 = false;
                                                                    }
                                                                    bool v1225;
                                                                    v1225 = v1224 == false;
                                                                    if (v1225){
                                                                        assert("The read index needs to be in range for the static array." && v1224);
                                                                    } else {
                                                                    }
                                                                    unsigned char v1226;
                                                                    v1226 = v120.v[v1221];
                                                                    bool v1227;
                                                                    v1227 = 0l <= v1216;
                                                                    bool v1229;
                                                                    if (v1227){
                                                                        bool v1228;
                                                                        v1228 = v1216 < 5l;
                                                                        v1229 = v1228;
                                                                    } else {
                                                                        v1229 = false;
                                                                    }
                                                                    bool v1230;
                                                                    v1230 = v1229 == false;
                                                                    if (v1230){
                                                                        assert("The read index needs to be in range for the static array." && v1229);
                                                                    } else {
                                                                    }
                                                                    v1189.v[v1216] = v1226;
                                                                    v1216 += 1l ;
                                                                }
                                                                v1233 = US15_1(v1188, v1189);
                                                            } else {
                                                                v1233 = US15_0();
                                                            }
                                                            US11 v1273;
                                                            switch (v1233.tag) {
                                                                case 0: { // None
                                                                    v1273 = US11_0();
                                                                    break;
                                                                }
                                                                case 1: { // Some
                                                                    static_array<unsigned char,2l> v1234 = v1233.v.case1.v0; static_array<unsigned char,5l> v1235 = v1233.v.case1.v1;
                                                                    static_array<unsigned char,3l> v1236;
                                                                    long v1237;
                                                                    v1237 = 0l;
                                                                    while (while_method_1(v1237)){
                                                                        bool v1239;
                                                                        v1239 = 0l <= v1237;
                                                                        bool v1241;
                                                                        if (v1239){
                                                                            bool v1240;
                                                                            v1240 = v1237 < 5l;
                                                                            v1241 = v1240;
                                                                        } else {
                                                                            v1241 = false;
                                                                        }
                                                                        bool v1242;
                                                                        v1242 = v1241 == false;
                                                                        if (v1242){
                                                                            assert("The read index needs to be in range for the static array." && v1241);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1243;
                                                                        v1243 = v1235.v[v1237];
                                                                        bool v1245;
                                                                        if (v1239){
                                                                            bool v1244;
                                                                            v1244 = v1237 < 3l;
                                                                            v1245 = v1244;
                                                                        } else {
                                                                            v1245 = false;
                                                                        }
                                                                        bool v1246;
                                                                        v1246 = v1245 == false;
                                                                        if (v1246){
                                                                            assert("The read index needs to be in range for the static array." && v1245);
                                                                        } else {
                                                                        }
                                                                        v1236.v[v1237] = v1243;
                                                                        v1237 += 1l ;
                                                                    }
                                                                    static_array<unsigned char,5l> v1247;
                                                                    long v1248;
                                                                    v1248 = 0l;
                                                                    while (while_method_4(v1248)){
                                                                        bool v1250;
                                                                        v1250 = 0l <= v1248;
                                                                        bool v1252;
                                                                        if (v1250){
                                                                            bool v1251;
                                                                            v1251 = v1248 < 2l;
                                                                            v1252 = v1251;
                                                                        } else {
                                                                            v1252 = false;
                                                                        }
                                                                        bool v1253;
                                                                        v1253 = v1252 == false;
                                                                        if (v1253){
                                                                            assert("The read index needs to be in range for the static array." && v1252);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1254;
                                                                        v1254 = v1234.v[v1248];
                                                                        bool v1256;
                                                                        if (v1250){
                                                                            bool v1255;
                                                                            v1255 = v1248 < 5l;
                                                                            v1256 = v1255;
                                                                        } else {
                                                                            v1256 = false;
                                                                        }
                                                                        bool v1257;
                                                                        v1257 = v1256 == false;
                                                                        if (v1257){
                                                                            assert("The read index needs to be in range for the static array." && v1256);
                                                                        } else {
                                                                        }
                                                                        v1247.v[v1248] = v1254;
                                                                        v1248 += 1l ;
                                                                    }
                                                                    long v1258;
                                                                    v1258 = 0l;
                                                                    while (while_method_1(v1258)){
                                                                        bool v1260;
                                                                        v1260 = 0l <= v1258;
                                                                        bool v1262;
                                                                        if (v1260){
                                                                            bool v1261;
                                                                            v1261 = v1258 < 3l;
                                                                            v1262 = v1261;
                                                                        } else {
                                                                            v1262 = false;
                                                                        }
                                                                        bool v1263;
                                                                        v1263 = v1262 == false;
                                                                        if (v1263){
                                                                            assert("The read index needs to be in range for the static array." && v1262);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1264;
                                                                        v1264 = v1236.v[v1258];
                                                                        long v1265;
                                                                        v1265 = 2l + v1258;
                                                                        bool v1266;
                                                                        v1266 = 0l <= v1265;
                                                                        bool v1268;
                                                                        if (v1266){
                                                                            bool v1267;
                                                                            v1267 = v1265 < 5l;
                                                                            v1268 = v1267;
                                                                        } else {
                                                                            v1268 = false;
                                                                        }
                                                                        bool v1269;
                                                                        v1269 = v1268 == false;
                                                                        if (v1269){
                                                                            assert("The read index needs to be in range for the static array." && v1268);
                                                                        } else {
                                                                        }
                                                                        v1247.v[v1265] = v1264;
                                                                        v1258 += 1l ;
                                                                    }
                                                                    v1273 = US11_1(v1247);
                                                                    break;
                                                                }
                                                                default: {
                                                                    assert("Invalid tag." && false);
                                                                }
                                                            }
                                                            switch (v1273.tag) {
                                                                case 0: { // None
                                                                    static_array<unsigned char,5l> v1275;
                                                                    long v1276;
                                                                    v1276 = 0l;
                                                                    while (while_method_2(v1276)){
                                                                        bool v1278;
                                                                        v1278 = 0l <= v1276;
                                                                        bool v1280;
                                                                        if (v1278){
                                                                            bool v1279;
                                                                            v1279 = v1276 < 7l;
                                                                            v1280 = v1279;
                                                                        } else {
                                                                            v1280 = false;
                                                                        }
                                                                        bool v1281;
                                                                        v1281 = v1280 == false;
                                                                        if (v1281){
                                                                            assert("The read index needs to be in range for the static array." && v1280);
                                                                        } else {
                                                                        }
                                                                        unsigned char v1282;
                                                                        v1282 = v120.v[v1276];
                                                                        bool v1284;
                                                                        if (v1278){
                                                                            bool v1283;
                                                                            v1283 = v1276 < 5l;
                                                                            v1284 = v1283;
                                                                        } else {
                                                                            v1284 = false;
                                                                        }
                                                                        bool v1285;
                                                                        v1285 = v1284 == false;
                                                                        if (v1285){
                                                                            assert("The read index needs to be in range for the static array." && v1284);
                                                                        } else {
                                                                        }
                                                                        v1275.v[v1276] = v1282;
                                                                        v1276 += 1l ;
                                                                    }
                                                                    v1316 = v1275; v1317 = 0;
                                                                    break;
                                                                }
                                                                case 1: { // Some
                                                                    static_array<unsigned char,5l> v1274 = v1273.v.case1.v0;
                                                                    v1316 = v1274; v1317 = 1;
                                                                    break;
                                                                }
                                                                default: {
                                                                    assert("Invalid tag." && false);
                                                                }
                                                            }
                                                            break;
                                                        }
                                                        case 1: { // Some
                                                            static_array<unsigned char,5l> v1187 = v1186.v.case1.v0;
                                                            v1316 = v1187; v1317 = 2;
                                                            break;
                                                        }
                                                        default: {
                                                            assert("Invalid tag." && false);
                                                        }
                                                    }
                                                    break;
                                                }
                                                case 1: { // Some
                                                    static_array<unsigned char,5l> v1037 = v1036.v.case1.v0;
                                                    v1316 = v1037; v1317 = 3;
                                                    break;
                                                }
                                                default: {
                                                    assert("Invalid tag." && false);
                                                }
                                            }
                                            break;
                                        }
                                        case 1: { // Some
                                            static_array<unsigned char,5l> v950 = v949.v.case1.v0;
                                            v1316 = v950; v1317 = 4;
                                            break;
                                        }
                                        default: {
                                            assert("Invalid tag." && false);
                                        }
                                    }
                                    break;
                                }
                                case 1: { // Some
                                    static_array<unsigned char,5l> v906 = v905.v.case1.v0;
                                    v1316 = v906; v1317 = 5;
                                    break;
                                }
                                default: {
                                    assert("Invalid tag." && false);
                                }
                            }
                            break;
                        }
                        case 1: { // Some
                            static_array<unsigned char,5l> v714 = v713.v.case1.v0;
                            v1316 = v714; v1317 = 6;
                            break;
                        }
                        default: {
                            assert("Invalid tag." && false);
                        }
                    }
                    break;
                }
                case 1: { // Some
                    static_array<unsigned char,5l> v587 = v586.v.case1.v0;
                    v1316 = v587; v1317 = 7;
                    break;
                }
                default: {
                    assert("Invalid tag." && false);
                }
            }
            break;
        }
        case 1: { // Some
            static_array<unsigned char,5l> v500 = v499.v.case1.v0;
            v1316 = v500; v1317 = 8;
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
    return Tuple1(v1316, v1317);
}
__device__ US7 play_loop_inner_7(unsigned long long & v0, static_array_list<US3,128l,long> & v1, curandStatePhilox4_32_10_t & v2, static_array<US2,2l> v3, US7 v4){
    static_array_list<US3,128l,long> & v5 = v1;
    unsigned long long & v6 = v0;
    bool v7; US7 v8;
    Tuple3 tmp1 = Tuple3(true, v4);
    v7 = tmp1.v0; v8 = tmp1.v1;
    while (while_method_0(v7, v8)){
        bool v1059; US7 v1060;
        switch (v8.tag) {
            case 0: { // G_Flop
                long v880 = v8.v.case0.v0; static_array<static_array<unsigned char,2l>,2l> v881 = v8.v.case0.v1; static_array<long,2l> v882 = v8.v.case0.v2; long v883 = v8.v.case0.v3; static_array<long,2l> v884 = v8.v.case0.v4; US8 v885 = v8.v.case0.v5;
                static_array<unsigned char,3l> v886; unsigned long long v887;
                Tuple4 tmp4 = draw_cards_8(v2, v6);
                v886 = tmp4.v0; v887 = tmp4.v1;
                v0 = v887;
                static_array_list<unsigned char,5l,long> v888;
                v888 = get_community_cards_11(v885, v886);
                long v889;
                v889 = v5.length;
                bool v890;
                v890 = v889 < 128l;
                bool v891;
                v891 = v890 == false;
                if (v891){
                    assert("The length has to be less than the maximum length of the array." && v890);
                } else {
                }
                long v892;
                v892 = v889 + 1l;
                v5.length = v892;
                bool v893;
                v893 = 0l <= v889;
                bool v896;
                if (v893){
                    long v894;
                    v894 = v5.length;
                    bool v895;
                    v895 = v889 < v894;
                    v896 = v895;
                } else {
                    v896 = false;
                }
                bool v897;
                v897 = v896 == false;
                if (v897){
                    assert("The set index needs to be in range for the static array list." && v896);
                } else {
                }
                US3 v898;
                v898 = US3_0(v888);
                v5.v[v889] = v898;
                US8 v901;
                switch (v885.tag) {
                    case 1: { // Preflop
                        v901 = US8_0(v886);
                        break;
                    }
                    default: {
                        printf("%s\n", "Invalid street in flop.");
                        asm("exit;");
                    }
                }
                long v902;
                v902 = 2l;
                long v903;
                v903 = 0l;
                US7 v904;
                v904 = try_round_12(v902, v881, v882, v903, v884, v901);
                v1059 = true; v1060 = v904;
                break;
            }
            case 1: { // G_Fold
                long v10 = v8.v.case1.v0; static_array<static_array<unsigned char,2l>,2l> v11 = v8.v.case1.v1; static_array<long,2l> v12 = v8.v.case1.v2; long v13 = v8.v.case1.v3; static_array<long,2l> v14 = v8.v.case1.v4; US8 v15 = v8.v.case1.v5;
                long v16;
                v16 = v13 % 2l;
                bool v17;
                v17 = 0l <= v16;
                bool v19;
                if (v17){
                    bool v18;
                    v18 = v16 < 2l;
                    v19 = v18;
                } else {
                    v19 = false;
                }
                bool v20;
                v20 = v19 == false;
                if (v20){
                    assert("The read index needs to be in range for the static array." && v19);
                } else {
                }
                long v21;
                v21 = v12.v[v16];
                long v22;
                v22 = v13 + 1l;
                long v23;
                v23 = v22 % 2l;
                long v24;
                v24 = v5.length;
                bool v25;
                v25 = v24 < 128l;
                bool v26;
                v26 = v25 == false;
                if (v26){
                    assert("The length has to be less than the maximum length of the array." && v25);
                } else {
                }
                long v27;
                v27 = v24 + 1l;
                v5.length = v27;
                bool v28;
                v28 = 0l <= v24;
                bool v31;
                if (v28){
                    long v29;
                    v29 = v5.length;
                    bool v30;
                    v30 = v24 < v29;
                    v31 = v30;
                } else {
                    v31 = false;
                }
                bool v32;
                v32 = v31 == false;
                if (v32){
                    assert("The set index needs to be in range for the static array list." && v31);
                } else {
                }
                US3 v33;
                v33 = US3_1(v21, v23);
                v5.v[v24] = v33;
                v1059 = false; v1060 = v8;
                break;
            }
            case 2: { // G_Preflop
                static_array<unsigned char,2l> v1003; unsigned long long v1004;
                Tuple8 tmp9 = draw_cards_15(v2, v6);
                v1003 = tmp9.v0; v1004 = tmp9.v1;
                v0 = v1004;
                static_array<unsigned char,2l> v1005; unsigned long long v1006;
                Tuple8 tmp10 = draw_cards_15(v2, v6);
                v1005 = tmp10.v0; v1006 = tmp10.v1;
                v0 = v1006;
                long v1007;
                v1007 = v5.length;
                bool v1008;
                v1008 = v1007 < 128l;
                bool v1009;
                v1009 = v1008 == false;
                if (v1009){
                    assert("The length has to be less than the maximum length of the array." && v1008);
                } else {
                }
                long v1010;
                v1010 = v1007 + 1l;
                v5.length = v1010;
                bool v1011;
                v1011 = 0l <= v1007;
                bool v1014;
                if (v1011){
                    long v1012;
                    v1012 = v5.length;
                    bool v1013;
                    v1013 = v1007 < v1012;
                    v1014 = v1013;
                } else {
                    v1014 = false;
                }
                bool v1015;
                v1015 = v1014 == false;
                if (v1015){
                    assert("The set index needs to be in range for the static array list." && v1014);
                } else {
                }
                US3 v1016;
                v1016 = US3_3(0l, v1003);
                v5.v[v1007] = v1016;
                long v1017;
                v1017 = v5.length;
                bool v1018;
                v1018 = v1017 < 128l;
                bool v1019;
                v1019 = v1018 == false;
                if (v1019){
                    assert("The length has to be less than the maximum length of the array." && v1018);
                } else {
                }
                long v1020;
                v1020 = v1017 + 1l;
                v5.length = v1020;
                bool v1021;
                v1021 = 0l <= v1017;
                bool v1024;
                if (v1021){
                    long v1022;
                    v1022 = v5.length;
                    bool v1023;
                    v1023 = v1017 < v1022;
                    v1024 = v1023;
                } else {
                    v1024 = false;
                }
                bool v1025;
                v1025 = v1024 == false;
                if (v1025){
                    assert("The set index needs to be in range for the static array list." && v1024);
                } else {
                }
                US3 v1026;
                v1026 = US3_3(1l, v1005);
                v5.v[v1017] = v1026;
                static_array<static_array<unsigned char,2l>,2l> v1027;
                v1027.v[0l] = v1003;
                v1027.v[1l] = v1005;
                static_array<long,2l> v1028;
                v1028.v[0l] = 2l;
                v1028.v[1l] = 1l;
                static_array<long,2l> v1029;
                long v1030;
                v1030 = 0l;
                while (while_method_4(v1030)){
                    bool v1032;
                    v1032 = 0l <= v1030;
                    bool v1034;
                    if (v1032){
                        bool v1033;
                        v1033 = v1030 < 2l;
                        v1034 = v1033;
                    } else {
                        v1034 = false;
                    }
                    bool v1035;
                    v1035 = v1034 == false;
                    if (v1035){
                        assert("The read index needs to be in range for the static array." && v1034);
                    } else {
                    }
                    long v1036;
                    v1036 = v1028.v[v1030];
                    long v1037;
                    v1037 = 100l - v1036;
                    bool v1039;
                    if (v1032){
                        bool v1038;
                        v1038 = v1030 < 2l;
                        v1039 = v1038;
                    } else {
                        v1039 = false;
                    }
                    bool v1040;
                    v1040 = v1039 == false;
                    if (v1040){
                        assert("The read index needs to be in range for the static array." && v1039);
                    } else {
                    }
                    v1029.v[v1030] = v1037;
                    v1030 += 1l ;
                }
                long v1041;
                v1041 = 2l;
                long v1042;
                v1042 = 0l;
                US8 v1043;
                v1043 = US8_1();
                US7 v1044;
                v1044 = try_round_12(v1041, v1027, v1028, v1042, v1029, v1043);
                v1059 = true; v1060 = v1044;
                break;
            }
            case 3: { // G_River
                long v954 = v8.v.case3.v0; static_array<static_array<unsigned char,2l>,2l> v955 = v8.v.case3.v1; static_array<long,2l> v956 = v8.v.case3.v2; long v957 = v8.v.case3.v3; static_array<long,2l> v958 = v8.v.case3.v4; US8 v959 = v8.v.case3.v5;
                static_array<unsigned char,1l> v960; unsigned long long v961;
                Tuple9 tmp13 = draw_cards_16(v2, v6);
                v960 = tmp13.v0; v961 = tmp13.v1;
                v0 = v961;
                static_array_list<unsigned char,5l,long> v962;
                v962 = get_community_cards_17(v959, v960);
                long v963;
                v963 = v5.length;
                bool v964;
                v964 = v963 < 128l;
                bool v965;
                v965 = v964 == false;
                if (v965){
                    assert("The length has to be less than the maximum length of the array." && v964);
                } else {
                }
                long v966;
                v966 = v963 + 1l;
                v5.length = v966;
                bool v967;
                v967 = 0l <= v963;
                bool v970;
                if (v967){
                    long v968;
                    v968 = v5.length;
                    bool v969;
                    v969 = v963 < v968;
                    v970 = v969;
                } else {
                    v970 = false;
                }
                bool v971;
                v971 = v970 == false;
                if (v971){
                    assert("The set index needs to be in range for the static array list." && v970);
                } else {
                }
                US3 v972;
                v972 = US3_0(v962);
                v5.v[v963] = v972;
                US8 v999;
                switch (v959.tag) {
                    case 3: { // Turn
                        static_array<unsigned char,4l> v973 = v959.v.case3.v0;
                        static_array<unsigned char,5l> v974;
                        long v975;
                        v975 = 0l;
                        while (while_method_3(v975)){
                            bool v977;
                            v977 = 0l <= v975;
                            bool v979;
                            if (v977){
                                bool v978;
                                v978 = v975 < 4l;
                                v979 = v978;
                            } else {
                                v979 = false;
                            }
                            bool v980;
                            v980 = v979 == false;
                            if (v980){
                                assert("The read index needs to be in range for the static array." && v979);
                            } else {
                            }
                            unsigned char v981;
                            v981 = v973.v[v975];
                            bool v983;
                            if (v977){
                                bool v982;
                                v982 = v975 < 5l;
                                v983 = v982;
                            } else {
                                v983 = false;
                            }
                            bool v984;
                            v984 = v983 == false;
                            if (v984){
                                assert("The read index needs to be in range for the static array." && v983);
                            } else {
                            }
                            v974.v[v975] = v981;
                            v975 += 1l ;
                        }
                        long v985;
                        v985 = 0l;
                        while (while_method_5(v985)){
                            bool v987;
                            v987 = 0l <= v985;
                            bool v989;
                            if (v987){
                                bool v988;
                                v988 = v985 < 1l;
                                v989 = v988;
                            } else {
                                v989 = false;
                            }
                            bool v990;
                            v990 = v989 == false;
                            if (v990){
                                assert("The read index needs to be in range for the static array." && v989);
                            } else {
                            }
                            unsigned char v991;
                            v991 = v960.v[v985];
                            long v992;
                            v992 = 4l + v985;
                            bool v993;
                            v993 = 0l <= v992;
                            bool v995;
                            if (v993){
                                bool v994;
                                v994 = v992 < 5l;
                                v995 = v994;
                            } else {
                                v995 = false;
                            }
                            bool v996;
                            v996 = v995 == false;
                            if (v996){
                                assert("The read index needs to be in range for the static array." && v995);
                            } else {
                            }
                            v974.v[v992] = v991;
                            v985 += 1l ;
                        }
                        v999 = US8_2(v974);
                        break;
                    }
                    default: {
                        printf("%s\n", "Invalid street in river.");
                        asm("exit;");
                    }
                }
                long v1000;
                v1000 = 2l;
                long v1001;
                v1001 = 0l;
                US7 v1002;
                v1002 = try_round_12(v1000, v955, v956, v1001, v958, v999);
                v1059 = true; v1060 = v1002;
                break;
            }
            case 4: { // G_Round
                long v147 = v8.v.case4.v0; static_array<static_array<unsigned char,2l>,2l> v148 = v8.v.case4.v1; static_array<long,2l> v149 = v8.v.case4.v2; long v150 = v8.v.case4.v3; static_array<long,2l> v151 = v8.v.case4.v4; US8 v152 = v8.v.case4.v5;
                long v153;
                v153 = v150 % 2l;
                bool v154;
                v154 = 0l <= v153;
                bool v156;
                if (v154){
                    bool v155;
                    v155 = v153 < 2l;
                    v156 = v155;
                } else {
                    v156 = false;
                }
                bool v157;
                v157 = v156 == false;
                if (v157){
                    assert("The read index needs to be in range for the static array." && v156);
                } else {
                }
                US2 v158;
                v158 = v3.v[v153];
                switch (v158.tag) {
                    case 0: { // Computer
                        static_array<long,2l> v159;
                        long v160;
                        v160 = 0l;
                        while (while_method_4(v160)){
                            bool v162;
                            v162 = 0l <= v160;
                            bool v164;
                            if (v162){
                                bool v163;
                                v163 = v160 < 2l;
                                v164 = v163;
                            } else {
                                v164 = false;
                            }
                            bool v165;
                            v165 = v164 == false;
                            if (v165){
                                assert("The read index needs to be in range for the static array." && v164);
                            } else {
                            }
                            long v166;
                            v166 = v151.v[v160];
                            bool v168;
                            if (v162){
                                bool v167;
                                v167 = v160 < 2l;
                                v168 = v167;
                            } else {
                                v168 = false;
                            }
                            bool v169;
                            v169 = v168 == false;
                            if (v169){
                                assert("The read index needs to be in range for the static array." && v168);
                            } else {
                            }
                            long v170;
                            v170 = v149.v[v160];
                            long v171;
                            v171 = v166 + v170;
                            bool v173;
                            if (v162){
                                bool v172;
                                v172 = v160 < 2l;
                                v173 = v172;
                            } else {
                                v173 = false;
                            }
                            bool v174;
                            v174 = v173 == false;
                            if (v174){
                                assert("The read index needs to be in range for the static array." && v173);
                            } else {
                            }
                            v159.v[v160] = v171;
                            v160 += 1l ;
                        }
                        long v175;
                        v175 = v149.v[0l];
                        long v176; long v177;
                        Tuple7 tmp14 = Tuple7(1l, v175);
                        v176 = tmp14.v0; v177 = tmp14.v1;
                        while (while_method_4(v176)){
                            bool v179;
                            v179 = 0l <= v176;
                            bool v181;
                            if (v179){
                                bool v180;
                                v180 = v176 < 2l;
                                v181 = v180;
                            } else {
                                v181 = false;
                            }
                            bool v182;
                            v182 = v181 == false;
                            if (v182){
                                assert("The read index needs to be in range for the static array." && v181);
                            } else {
                            }
                            long v183;
                            v183 = v149.v[v176];
                            bool v184;
                            v184 = v177 >= v183;
                            long v185;
                            if (v184){
                                v185 = v177;
                            } else {
                                v185 = v183;
                            }
                            v177 = v185;
                            v176 += 1l ;
                        }
                        bool v187;
                        if (v154){
                            bool v186;
                            v186 = v153 < 2l;
                            v187 = v186;
                        } else {
                            v187 = false;
                        }
                        bool v188;
                        v188 = v187 == false;
                        if (v188){
                            assert("The read index needs to be in range for the static array." && v187);
                        } else {
                        }
                        long v189;
                        v189 = v159.v[v153];
                        bool v190;
                        v190 = v177 < v189;
                        long v191;
                        if (v190){
                            v191 = v177;
                        } else {
                            v191 = v189;
                        }
                        static_array<long,2l> v192;
                        long v193;
                        v193 = 0l;
                        while (while_method_4(v193)){
                            bool v195;
                            v195 = 0l <= v193;
                            bool v197;
                            if (v195){
                                bool v196;
                                v196 = v193 < 2l;
                                v197 = v196;
                            } else {
                                v197 = false;
                            }
                            bool v198;
                            v198 = v197 == false;
                            if (v198){
                                assert("The read index needs to be in range for the static array." && v197);
                            } else {
                            }
                            long v199;
                            v199 = v149.v[v193];
                            bool v200;
                            v200 = v153 == v193;
                            long v201;
                            if (v200){
                                v201 = v191;
                            } else {
                                v201 = v199;
                            }
                            bool v203;
                            if (v195){
                                bool v202;
                                v202 = v193 < 2l;
                                v203 = v202;
                            } else {
                                v203 = false;
                            }
                            bool v204;
                            v204 = v203 == false;
                            if (v204){
                                assert("The read index needs to be in range for the static array." && v203);
                            } else {
                            }
                            v192.v[v193] = v201;
                            v193 += 1l ;
                        }
                        static_array<long,2l> v205;
                        long v206;
                        v206 = 0l;
                        while (while_method_4(v206)){
                            bool v208;
                            v208 = 0l <= v206;
                            bool v210;
                            if (v208){
                                bool v209;
                                v209 = v206 < 2l;
                                v210 = v209;
                            } else {
                                v210 = false;
                            }
                            bool v211;
                            v211 = v210 == false;
                            if (v211){
                                assert("The read index needs to be in range for the static array." && v210);
                            } else {
                            }
                            long v212;
                            v212 = v159.v[v206];
                            bool v214;
                            if (v208){
                                bool v213;
                                v213 = v206 < 2l;
                                v214 = v213;
                            } else {
                                v214 = false;
                            }
                            bool v215;
                            v215 = v214 == false;
                            if (v215){
                                assert("The read index needs to be in range for the static array." && v214);
                            } else {
                            }
                            long v216;
                            v216 = v192.v[v206];
                            long v217;
                            v217 = v212 - v216;
                            bool v219;
                            if (v208){
                                bool v218;
                                v218 = v206 < 2l;
                                v219 = v218;
                            } else {
                                v219 = false;
                            }
                            bool v220;
                            v220 = v219 == false;
                            if (v220){
                                assert("The read index needs to be in range for the static array." && v219);
                            } else {
                            }
                            v205.v[v206] = v217;
                            v206 += 1l ;
                        }
                        long v221;
                        v221 = v192.v[0l];
                        long v222; long v223;
                        Tuple7 tmp15 = Tuple7(1l, v221);
                        v222 = tmp15.v0; v223 = tmp15.v1;
                        while (while_method_4(v222)){
                            bool v225;
                            v225 = 0l <= v222;
                            bool v227;
                            if (v225){
                                bool v226;
                                v226 = v222 < 2l;
                                v227 = v226;
                            } else {
                                v227 = false;
                            }
                            bool v228;
                            v228 = v227 == false;
                            if (v228){
                                assert("The read index needs to be in range for the static array." && v227);
                            } else {
                            }
                            long v229;
                            v229 = v192.v[v222];
                            long v230;
                            v230 = v223 + v229;
                            v223 = v230;
                            v222 += 1l ;
                        }
                        bool v232;
                        if (v154){
                            bool v231;
                            v231 = v153 < 2l;
                            v232 = v231;
                        } else {
                            v232 = false;
                        }
                        bool v233;
                        v233 = v232 == false;
                        if (v233){
                            assert("The read index needs to be in range for the static array." && v232);
                        } else {
                        }
                        long v234;
                        v234 = v149.v[v153];
                        bool v235;
                        v235 = v234 < v177;
                        float v236;
                        if (v235){
                            v236 = 1.0f;
                        } else {
                            v236 = 0.0f;
                        }
                        long v237;
                        v237 = v223 / 3l;
                        bool v238;
                        v238 = v147 <= v237;
                        bool v244;
                        if (v238){
                            bool v240;
                            if (v154){
                                bool v239;
                                v239 = v153 < 2l;
                                v240 = v239;
                            } else {
                                v240 = false;
                            }
                            bool v241;
                            v241 = v240 == false;
                            if (v241){
                                assert("The read index needs to be in range for the static array." && v240);
                            } else {
                            }
                            long v242;
                            v242 = v205.v[v153];
                            bool v243;
                            v243 = v237 < v242;
                            v244 = v243;
                        } else {
                            v244 = false;
                        }
                        float v245;
                        if (v244){
                            v245 = 1.0f;
                        } else {
                            v245 = 0.0f;
                        }
                        long v246;
                        v246 = v223 / 2l;
                        bool v247;
                        v247 = v147 <= v246;
                        bool v253;
                        if (v247){
                            bool v249;
                            if (v154){
                                bool v248;
                                v248 = v153 < 2l;
                                v249 = v248;
                            } else {
                                v249 = false;
                            }
                            bool v250;
                            v250 = v249 == false;
                            if (v250){
                                assert("The read index needs to be in range for the static array." && v249);
                            } else {
                            }
                            long v251;
                            v251 = v205.v[v153];
                            bool v252;
                            v252 = v246 < v251;
                            v253 = v252;
                        } else {
                            v253 = false;
                        }
                        float v254;
                        if (v253){
                            v254 = 1.0f;
                        } else {
                            v254 = 0.0f;
                        }
                        bool v255;
                        v255 = v147 <= v223;
                        bool v261;
                        if (v255){
                            bool v257;
                            if (v154){
                                bool v256;
                                v256 = v153 < 2l;
                                v257 = v256;
                            } else {
                                v257 = false;
                            }
                            bool v258;
                            v258 = v257 == false;
                            if (v258){
                                assert("The read index needs to be in range for the static array." && v257);
                            } else {
                            }
                            long v259;
                            v259 = v205.v[v153];
                            bool v260;
                            v260 = v223 < v259;
                            v261 = v260;
                        } else {
                            v261 = false;
                        }
                        float v262;
                        if (v261){
                            v262 = 1.0f;
                        } else {
                            v262 = 0.0f;
                        }
                        static_array<Tuple10,6l> v263;
                        US4 v264;
                        v264 = US4_2();
                        v263.v[0l] = Tuple10(v264, v236);
                        US4 v265;
                        v265 = US4_1();
                        v263.v[1l] = Tuple10(v265, 4.0f);
                        US4 v266;
                        v266 = US4_3(v237);
                        v263.v[2l] = Tuple10(v266, v245);
                        US4 v267;
                        v267 = US4_3(v246);
                        v263.v[3l] = Tuple10(v267, v254);
                        US4 v268;
                        v268 = US4_3(v223);
                        v263.v[4l] = Tuple10(v268, v262);
                        US4 v269;
                        v269 = US4_0();
                        v263.v[5l] = Tuple10(v269, 1.0f);
                        US4 v270;
                        v270 = sample_discrete_18(v263, v2);
                        long v271;
                        v271 = v5.length;
                        bool v272;
                        v272 = v271 < 128l;
                        bool v273;
                        v273 = v272 == false;
                        if (v273){
                            assert("The length has to be less than the maximum length of the array." && v272);
                        } else {
                        }
                        long v274;
                        v274 = v271 + 1l;
                        v5.length = v274;
                        bool v275;
                        v275 = 0l <= v271;
                        bool v278;
                        if (v275){
                            long v276;
                            v276 = v5.length;
                            bool v277;
                            v277 = v271 < v276;
                            v278 = v277;
                        } else {
                            v278 = false;
                        }
                        bool v279;
                        v279 = v278 == false;
                        if (v279){
                            assert("The set index needs to be in range for the static array list." && v278);
                        } else {
                        }
                        US3 v280;
                        v280 = US3_2(v153, v270);
                        v5.v[v271] = v280;
                        US7 v567;
                        switch (v270.tag) {
                            case 0: { // A_All_In
                                static_array<long,2l> v458;
                                long v459;
                                v459 = 0l;
                                while (while_method_4(v459)){
                                    bool v461;
                                    v461 = 0l <= v459;
                                    bool v463;
                                    if (v461){
                                        bool v462;
                                        v462 = v459 < 2l;
                                        v463 = v462;
                                    } else {
                                        v463 = false;
                                    }
                                    bool v464;
                                    v464 = v463 == false;
                                    if (v464){
                                        assert("The read index needs to be in range for the static array." && v463);
                                    } else {
                                    }
                                    long v465;
                                    v465 = v151.v[v459];
                                    bool v467;
                                    if (v461){
                                        bool v466;
                                        v466 = v459 < 2l;
                                        v467 = v466;
                                    } else {
                                        v467 = false;
                                    }
                                    bool v468;
                                    v468 = v467 == false;
                                    if (v468){
                                        assert("The read index needs to be in range for the static array." && v467);
                                    } else {
                                    }
                                    long v469;
                                    v469 = v149.v[v459];
                                    long v470;
                                    v470 = v465 + v469;
                                    bool v472;
                                    if (v461){
                                        bool v471;
                                        v471 = v459 < 2l;
                                        v472 = v471;
                                    } else {
                                        v472 = false;
                                    }
                                    bool v473;
                                    v473 = v472 == false;
                                    if (v473){
                                        assert("The read index needs to be in range for the static array." && v472);
                                    } else {
                                    }
                                    v458.v[v459] = v470;
                                    v459 += 1l ;
                                }
                                long v474;
                                v474 = v149.v[0l];
                                long v475; long v476;
                                Tuple7 tmp18 = Tuple7(1l, v474);
                                v475 = tmp18.v0; v476 = tmp18.v1;
                                while (while_method_4(v475)){
                                    bool v478;
                                    v478 = 0l <= v475;
                                    bool v480;
                                    if (v478){
                                        bool v479;
                                        v479 = v475 < 2l;
                                        v480 = v479;
                                    } else {
                                        v480 = false;
                                    }
                                    bool v481;
                                    v481 = v480 == false;
                                    if (v481){
                                        assert("The read index needs to be in range for the static array." && v480);
                                    } else {
                                    }
                                    long v482;
                                    v482 = v149.v[v475];
                                    bool v483;
                                    v483 = v476 >= v482;
                                    long v484;
                                    if (v483){
                                        v484 = v476;
                                    } else {
                                        v484 = v482;
                                    }
                                    v476 = v484;
                                    v475 += 1l ;
                                }
                                bool v486;
                                if (v154){
                                    bool v485;
                                    v485 = v153 < 2l;
                                    v486 = v485;
                                } else {
                                    v486 = false;
                                }
                                bool v487;
                                v487 = v486 == false;
                                if (v487){
                                    assert("The read index needs to be in range for the static array." && v486);
                                } else {
                                }
                                long v488;
                                v488 = v458.v[v153];
                                bool v489;
                                v489 = v476 < v488;
                                long v490;
                                if (v489){
                                    v490 = v476;
                                } else {
                                    v490 = v488;
                                }
                                static_array<long,2l> v491;
                                long v492;
                                v492 = 0l;
                                while (while_method_4(v492)){
                                    bool v494;
                                    v494 = 0l <= v492;
                                    bool v496;
                                    if (v494){
                                        bool v495;
                                        v495 = v492 < 2l;
                                        v496 = v495;
                                    } else {
                                        v496 = false;
                                    }
                                    bool v497;
                                    v497 = v496 == false;
                                    if (v497){
                                        assert("The read index needs to be in range for the static array." && v496);
                                    } else {
                                    }
                                    long v498;
                                    v498 = v149.v[v492];
                                    bool v499;
                                    v499 = v153 == v492;
                                    long v500;
                                    if (v499){
                                        v500 = v490;
                                    } else {
                                        v500 = v498;
                                    }
                                    bool v502;
                                    if (v494){
                                        bool v501;
                                        v501 = v492 < 2l;
                                        v502 = v501;
                                    } else {
                                        v502 = false;
                                    }
                                    bool v503;
                                    v503 = v502 == false;
                                    if (v503){
                                        assert("The read index needs to be in range for the static array." && v502);
                                    } else {
                                    }
                                    v491.v[v492] = v500;
                                    v492 += 1l ;
                                }
                                static_array<long,2l> v504;
                                long v505;
                                v505 = 0l;
                                while (while_method_4(v505)){
                                    bool v507;
                                    v507 = 0l <= v505;
                                    bool v509;
                                    if (v507){
                                        bool v508;
                                        v508 = v505 < 2l;
                                        v509 = v508;
                                    } else {
                                        v509 = false;
                                    }
                                    bool v510;
                                    v510 = v509 == false;
                                    if (v510){
                                        assert("The read index needs to be in range for the static array." && v509);
                                    } else {
                                    }
                                    long v511;
                                    v511 = v458.v[v505];
                                    bool v513;
                                    if (v507){
                                        bool v512;
                                        v512 = v505 < 2l;
                                        v513 = v512;
                                    } else {
                                        v513 = false;
                                    }
                                    bool v514;
                                    v514 = v513 == false;
                                    if (v514){
                                        assert("The read index needs to be in range for the static array." && v513);
                                    } else {
                                    }
                                    long v515;
                                    v515 = v491.v[v505];
                                    long v516;
                                    v516 = v511 - v515;
                                    bool v518;
                                    if (v507){
                                        bool v517;
                                        v517 = v505 < 2l;
                                        v518 = v517;
                                    } else {
                                        v518 = false;
                                    }
                                    bool v519;
                                    v519 = v518 == false;
                                    if (v519){
                                        assert("The read index needs to be in range for the static array." && v518);
                                    } else {
                                    }
                                    v504.v[v505] = v516;
                                    v505 += 1l ;
                                }
                                bool v521;
                                if (v154){
                                    bool v520;
                                    v520 = v153 < 2l;
                                    v521 = v520;
                                } else {
                                    v521 = false;
                                }
                                bool v522;
                                v522 = v521 == false;
                                if (v522){
                                    assert("The read index needs to be in range for the static array." && v521);
                                } else {
                                }
                                long v523;
                                v523 = v504.v[v153];
                                long v524;
                                v524 = v476 + v523;
                                bool v526;
                                if (v154){
                                    bool v525;
                                    v525 = v153 < 2l;
                                    v526 = v525;
                                } else {
                                    v526 = false;
                                }
                                bool v527;
                                v527 = v526 == false;
                                if (v527){
                                    assert("The read index needs to be in range for the static array." && v526);
                                } else {
                                }
                                long v528;
                                v528 = v458.v[v153];
                                bool v529;
                                v529 = v524 < v528;
                                long v530;
                                if (v529){
                                    v530 = v524;
                                } else {
                                    v530 = v528;
                                }
                                static_array<long,2l> v531;
                                long v532;
                                v532 = 0l;
                                while (while_method_4(v532)){
                                    bool v534;
                                    v534 = 0l <= v532;
                                    bool v536;
                                    if (v534){
                                        bool v535;
                                        v535 = v532 < 2l;
                                        v536 = v535;
                                    } else {
                                        v536 = false;
                                    }
                                    bool v537;
                                    v537 = v536 == false;
                                    if (v537){
                                        assert("The read index needs to be in range for the static array." && v536);
                                    } else {
                                    }
                                    long v538;
                                    v538 = v149.v[v532];
                                    bool v539;
                                    v539 = v153 == v532;
                                    long v540;
                                    if (v539){
                                        v540 = v530;
                                    } else {
                                        v540 = v538;
                                    }
                                    bool v542;
                                    if (v534){
                                        bool v541;
                                        v541 = v532 < 2l;
                                        v542 = v541;
                                    } else {
                                        v542 = false;
                                    }
                                    bool v543;
                                    v543 = v542 == false;
                                    if (v543){
                                        assert("The read index needs to be in range for the static array." && v542);
                                    } else {
                                    }
                                    v531.v[v532] = v540;
                                    v532 += 1l ;
                                }
                                static_array<long,2l> v544;
                                long v545;
                                v545 = 0l;
                                while (while_method_4(v545)){
                                    bool v547;
                                    v547 = 0l <= v545;
                                    bool v549;
                                    if (v547){
                                        bool v548;
                                        v548 = v545 < 2l;
                                        v549 = v548;
                                    } else {
                                        v549 = false;
                                    }
                                    bool v550;
                                    v550 = v549 == false;
                                    if (v550){
                                        assert("The read index needs to be in range for the static array." && v549);
                                    } else {
                                    }
                                    long v551;
                                    v551 = v458.v[v545];
                                    bool v553;
                                    if (v547){
                                        bool v552;
                                        v552 = v545 < 2l;
                                        v553 = v552;
                                    } else {
                                        v553 = false;
                                    }
                                    bool v554;
                                    v554 = v553 == false;
                                    if (v554){
                                        assert("The read index needs to be in range for the static array." && v553);
                                    } else {
                                    }
                                    long v555;
                                    v555 = v531.v[v545];
                                    long v556;
                                    v556 = v551 - v555;
                                    bool v558;
                                    if (v547){
                                        bool v557;
                                        v557 = v545 < 2l;
                                        v558 = v557;
                                    } else {
                                        v558 = false;
                                    }
                                    bool v559;
                                    v559 = v558 == false;
                                    if (v559){
                                        assert("The read index needs to be in range for the static array." && v558);
                                    } else {
                                    }
                                    v544.v[v545] = v556;
                                    v545 += 1l ;
                                }
                                bool v560;
                                v560 = v523 >= v147;
                                long v561;
                                if (v560){
                                    v561 = v523;
                                } else {
                                    v561 = v147;
                                }
                                long v562;
                                v562 = v150 + 1l;
                                v567 = try_round_12(v561, v148, v531, v562, v544, v152);
                                break;
                            }
                            case 1: { // A_Call
                                static_array<long,2l> v282;
                                long v283;
                                v283 = 0l;
                                while (while_method_4(v283)){
                                    bool v285;
                                    v285 = 0l <= v283;
                                    bool v287;
                                    if (v285){
                                        bool v286;
                                        v286 = v283 < 2l;
                                        v287 = v286;
                                    } else {
                                        v287 = false;
                                    }
                                    bool v288;
                                    v288 = v287 == false;
                                    if (v288){
                                        assert("The read index needs to be in range for the static array." && v287);
                                    } else {
                                    }
                                    long v289;
                                    v289 = v151.v[v283];
                                    bool v291;
                                    if (v285){
                                        bool v290;
                                        v290 = v283 < 2l;
                                        v291 = v290;
                                    } else {
                                        v291 = false;
                                    }
                                    bool v292;
                                    v292 = v291 == false;
                                    if (v292){
                                        assert("The read index needs to be in range for the static array." && v291);
                                    } else {
                                    }
                                    long v293;
                                    v293 = v149.v[v283];
                                    long v294;
                                    v294 = v289 + v293;
                                    bool v296;
                                    if (v285){
                                        bool v295;
                                        v295 = v283 < 2l;
                                        v296 = v295;
                                    } else {
                                        v296 = false;
                                    }
                                    bool v297;
                                    v297 = v296 == false;
                                    if (v297){
                                        assert("The read index needs to be in range for the static array." && v296);
                                    } else {
                                    }
                                    v282.v[v283] = v294;
                                    v283 += 1l ;
                                }
                                long v298;
                                v298 = v149.v[0l];
                                long v299; long v300;
                                Tuple7 tmp19 = Tuple7(1l, v298);
                                v299 = tmp19.v0; v300 = tmp19.v1;
                                while (while_method_4(v299)){
                                    bool v302;
                                    v302 = 0l <= v299;
                                    bool v304;
                                    if (v302){
                                        bool v303;
                                        v303 = v299 < 2l;
                                        v304 = v303;
                                    } else {
                                        v304 = false;
                                    }
                                    bool v305;
                                    v305 = v304 == false;
                                    if (v305){
                                        assert("The read index needs to be in range for the static array." && v304);
                                    } else {
                                    }
                                    long v306;
                                    v306 = v149.v[v299];
                                    bool v307;
                                    v307 = v300 >= v306;
                                    long v308;
                                    if (v307){
                                        v308 = v300;
                                    } else {
                                        v308 = v306;
                                    }
                                    v300 = v308;
                                    v299 += 1l ;
                                }
                                bool v310;
                                if (v154){
                                    bool v309;
                                    v309 = v153 < 2l;
                                    v310 = v309;
                                } else {
                                    v310 = false;
                                }
                                bool v311;
                                v311 = v310 == false;
                                if (v311){
                                    assert("The read index needs to be in range for the static array." && v310);
                                } else {
                                }
                                long v312;
                                v312 = v282.v[v153];
                                bool v313;
                                v313 = v300 < v312;
                                long v314;
                                if (v313){
                                    v314 = v300;
                                } else {
                                    v314 = v312;
                                }
                                static_array<long,2l> v315;
                                long v316;
                                v316 = 0l;
                                while (while_method_4(v316)){
                                    bool v318;
                                    v318 = 0l <= v316;
                                    bool v320;
                                    if (v318){
                                        bool v319;
                                        v319 = v316 < 2l;
                                        v320 = v319;
                                    } else {
                                        v320 = false;
                                    }
                                    bool v321;
                                    v321 = v320 == false;
                                    if (v321){
                                        assert("The read index needs to be in range for the static array." && v320);
                                    } else {
                                    }
                                    long v322;
                                    v322 = v149.v[v316];
                                    bool v323;
                                    v323 = v153 == v316;
                                    long v324;
                                    if (v323){
                                        v324 = v314;
                                    } else {
                                        v324 = v322;
                                    }
                                    bool v326;
                                    if (v318){
                                        bool v325;
                                        v325 = v316 < 2l;
                                        v326 = v325;
                                    } else {
                                        v326 = false;
                                    }
                                    bool v327;
                                    v327 = v326 == false;
                                    if (v327){
                                        assert("The read index needs to be in range for the static array." && v326);
                                    } else {
                                    }
                                    v315.v[v316] = v324;
                                    v316 += 1l ;
                                }
                                static_array<long,2l> v328;
                                long v329;
                                v329 = 0l;
                                while (while_method_4(v329)){
                                    bool v331;
                                    v331 = 0l <= v329;
                                    bool v333;
                                    if (v331){
                                        bool v332;
                                        v332 = v329 < 2l;
                                        v333 = v332;
                                    } else {
                                        v333 = false;
                                    }
                                    bool v334;
                                    v334 = v333 == false;
                                    if (v334){
                                        assert("The read index needs to be in range for the static array." && v333);
                                    } else {
                                    }
                                    long v335;
                                    v335 = v282.v[v329];
                                    bool v337;
                                    if (v331){
                                        bool v336;
                                        v336 = v329 < 2l;
                                        v337 = v336;
                                    } else {
                                        v337 = false;
                                    }
                                    bool v338;
                                    v338 = v337 == false;
                                    if (v338){
                                        assert("The read index needs to be in range for the static array." && v337);
                                    } else {
                                    }
                                    long v339;
                                    v339 = v315.v[v329];
                                    long v340;
                                    v340 = v335 - v339;
                                    bool v342;
                                    if (v331){
                                        bool v341;
                                        v341 = v329 < 2l;
                                        v342 = v341;
                                    } else {
                                        v342 = false;
                                    }
                                    bool v343;
                                    v343 = v342 == false;
                                    if (v343){
                                        assert("The read index needs to be in range for the static array." && v342);
                                    } else {
                                    }
                                    v328.v[v329] = v340;
                                    v329 += 1l ;
                                }
                                bool v344;
                                v344 = v153 < 2l;
                                if (v344){
                                    long v345;
                                    v345 = v150 + 1l;
                                    v567 = try_round_12(v147, v148, v315, v345, v328, v152);
                                } else {
                                    v567 = go_next_street_14(v147, v148, v315, v150, v328, v152);
                                }
                                break;
                            }
                            case 2: { // A_Fold
                                v567 = US7_1(v147, v148, v149, v150, v151, v152);
                                break;
                            }
                            case 3: { // A_Raise
                                long v349 = v270.v.case3.v0;
                                bool v350;
                                v350 = v147 <= v349;
                                bool v351;
                                v351 = v350 == false;
                                if (v351){
                                    assert("The raise amount must match the minimum." && v350);
                                } else {
                                }
                                static_array<long,2l> v352;
                                long v353;
                                v353 = 0l;
                                while (while_method_4(v353)){
                                    bool v355;
                                    v355 = 0l <= v353;
                                    bool v357;
                                    if (v355){
                                        bool v356;
                                        v356 = v353 < 2l;
                                        v357 = v356;
                                    } else {
                                        v357 = false;
                                    }
                                    bool v358;
                                    v358 = v357 == false;
                                    if (v358){
                                        assert("The read index needs to be in range for the static array." && v357);
                                    } else {
                                    }
                                    long v359;
                                    v359 = v151.v[v353];
                                    bool v361;
                                    if (v355){
                                        bool v360;
                                        v360 = v353 < 2l;
                                        v361 = v360;
                                    } else {
                                        v361 = false;
                                    }
                                    bool v362;
                                    v362 = v361 == false;
                                    if (v362){
                                        assert("The read index needs to be in range for the static array." && v361);
                                    } else {
                                    }
                                    long v363;
                                    v363 = v149.v[v353];
                                    long v364;
                                    v364 = v359 + v363;
                                    bool v366;
                                    if (v355){
                                        bool v365;
                                        v365 = v353 < 2l;
                                        v366 = v365;
                                    } else {
                                        v366 = false;
                                    }
                                    bool v367;
                                    v367 = v366 == false;
                                    if (v367){
                                        assert("The read index needs to be in range for the static array." && v366);
                                    } else {
                                    }
                                    v352.v[v353] = v364;
                                    v353 += 1l ;
                                }
                                long v368;
                                v368 = v149.v[0l];
                                long v369; long v370;
                                Tuple7 tmp20 = Tuple7(1l, v368);
                                v369 = tmp20.v0; v370 = tmp20.v1;
                                while (while_method_4(v369)){
                                    bool v372;
                                    v372 = 0l <= v369;
                                    bool v374;
                                    if (v372){
                                        bool v373;
                                        v373 = v369 < 2l;
                                        v374 = v373;
                                    } else {
                                        v374 = false;
                                    }
                                    bool v375;
                                    v375 = v374 == false;
                                    if (v375){
                                        assert("The read index needs to be in range for the static array." && v374);
                                    } else {
                                    }
                                    long v376;
                                    v376 = v149.v[v369];
                                    bool v377;
                                    v377 = v370 >= v376;
                                    long v378;
                                    if (v377){
                                        v378 = v370;
                                    } else {
                                        v378 = v376;
                                    }
                                    v370 = v378;
                                    v369 += 1l ;
                                }
                                bool v380;
                                if (v154){
                                    bool v379;
                                    v379 = v153 < 2l;
                                    v380 = v379;
                                } else {
                                    v380 = false;
                                }
                                bool v381;
                                v381 = v380 == false;
                                if (v381){
                                    assert("The read index needs to be in range for the static array." && v380);
                                } else {
                                }
                                long v382;
                                v382 = v352.v[v153];
                                bool v383;
                                v383 = v370 < v382;
                                long v384;
                                if (v383){
                                    v384 = v370;
                                } else {
                                    v384 = v382;
                                }
                                static_array<long,2l> v385;
                                long v386;
                                v386 = 0l;
                                while (while_method_4(v386)){
                                    bool v388;
                                    v388 = 0l <= v386;
                                    bool v390;
                                    if (v388){
                                        bool v389;
                                        v389 = v386 < 2l;
                                        v390 = v389;
                                    } else {
                                        v390 = false;
                                    }
                                    bool v391;
                                    v391 = v390 == false;
                                    if (v391){
                                        assert("The read index needs to be in range for the static array." && v390);
                                    } else {
                                    }
                                    long v392;
                                    v392 = v149.v[v386];
                                    bool v393;
                                    v393 = v153 == v386;
                                    long v394;
                                    if (v393){
                                        v394 = v384;
                                    } else {
                                        v394 = v392;
                                    }
                                    bool v396;
                                    if (v388){
                                        bool v395;
                                        v395 = v386 < 2l;
                                        v396 = v395;
                                    } else {
                                        v396 = false;
                                    }
                                    bool v397;
                                    v397 = v396 == false;
                                    if (v397){
                                        assert("The read index needs to be in range for the static array." && v396);
                                    } else {
                                    }
                                    v385.v[v386] = v394;
                                    v386 += 1l ;
                                }
                                static_array<long,2l> v398;
                                long v399;
                                v399 = 0l;
                                while (while_method_4(v399)){
                                    bool v401;
                                    v401 = 0l <= v399;
                                    bool v403;
                                    if (v401){
                                        bool v402;
                                        v402 = v399 < 2l;
                                        v403 = v402;
                                    } else {
                                        v403 = false;
                                    }
                                    bool v404;
                                    v404 = v403 == false;
                                    if (v404){
                                        assert("The read index needs to be in range for the static array." && v403);
                                    } else {
                                    }
                                    long v405;
                                    v405 = v352.v[v399];
                                    bool v407;
                                    if (v401){
                                        bool v406;
                                        v406 = v399 < 2l;
                                        v407 = v406;
                                    } else {
                                        v407 = false;
                                    }
                                    bool v408;
                                    v408 = v407 == false;
                                    if (v408){
                                        assert("The read index needs to be in range for the static array." && v407);
                                    } else {
                                    }
                                    long v409;
                                    v409 = v385.v[v399];
                                    long v410;
                                    v410 = v405 - v409;
                                    bool v412;
                                    if (v401){
                                        bool v411;
                                        v411 = v399 < 2l;
                                        v412 = v411;
                                    } else {
                                        v412 = false;
                                    }
                                    bool v413;
                                    v413 = v412 == false;
                                    if (v413){
                                        assert("The read index needs to be in range for the static array." && v412);
                                    } else {
                                    }
                                    v398.v[v399] = v410;
                                    v399 += 1l ;
                                }
                                bool v415;
                                if (v154){
                                    bool v414;
                                    v414 = v153 < 2l;
                                    v415 = v414;
                                } else {
                                    v415 = false;
                                }
                                bool v416;
                                v416 = v415 == false;
                                if (v416){
                                    assert("The read index needs to be in range for the static array." && v415);
                                } else {
                                }
                                long v417;
                                v417 = v398.v[v153];
                                bool v418;
                                v418 = v349 < v417;
                                bool v419;
                                v419 = v418 == false;
                                if (v419){
                                    assert("The raise amount must be less than the stack size after calling." && v418);
                                } else {
                                }
                                long v420;
                                v420 = v370 + v349;
                                bool v422;
                                if (v154){
                                    bool v421;
                                    v421 = v153 < 2l;
                                    v422 = v421;
                                } else {
                                    v422 = false;
                                }
                                bool v423;
                                v423 = v422 == false;
                                if (v423){
                                    assert("The read index needs to be in range for the static array." && v422);
                                } else {
                                }
                                long v424;
                                v424 = v352.v[v153];
                                bool v425;
                                v425 = v420 < v424;
                                long v426;
                                if (v425){
                                    v426 = v420;
                                } else {
                                    v426 = v424;
                                }
                                static_array<long,2l> v427;
                                long v428;
                                v428 = 0l;
                                while (while_method_4(v428)){
                                    bool v430;
                                    v430 = 0l <= v428;
                                    bool v432;
                                    if (v430){
                                        bool v431;
                                        v431 = v428 < 2l;
                                        v432 = v431;
                                    } else {
                                        v432 = false;
                                    }
                                    bool v433;
                                    v433 = v432 == false;
                                    if (v433){
                                        assert("The read index needs to be in range for the static array." && v432);
                                    } else {
                                    }
                                    long v434;
                                    v434 = v149.v[v428];
                                    bool v435;
                                    v435 = v153 == v428;
                                    long v436;
                                    if (v435){
                                        v436 = v426;
                                    } else {
                                        v436 = v434;
                                    }
                                    bool v438;
                                    if (v430){
                                        bool v437;
                                        v437 = v428 < 2l;
                                        v438 = v437;
                                    } else {
                                        v438 = false;
                                    }
                                    bool v439;
                                    v439 = v438 == false;
                                    if (v439){
                                        assert("The read index needs to be in range for the static array." && v438);
                                    } else {
                                    }
                                    v427.v[v428] = v436;
                                    v428 += 1l ;
                                }
                                static_array<long,2l> v440;
                                long v441;
                                v441 = 0l;
                                while (while_method_4(v441)){
                                    bool v443;
                                    v443 = 0l <= v441;
                                    bool v445;
                                    if (v443){
                                        bool v444;
                                        v444 = v441 < 2l;
                                        v445 = v444;
                                    } else {
                                        v445 = false;
                                    }
                                    bool v446;
                                    v446 = v445 == false;
                                    if (v446){
                                        assert("The read index needs to be in range for the static array." && v445);
                                    } else {
                                    }
                                    long v447;
                                    v447 = v352.v[v441];
                                    bool v449;
                                    if (v443){
                                        bool v448;
                                        v448 = v441 < 2l;
                                        v449 = v448;
                                    } else {
                                        v449 = false;
                                    }
                                    bool v450;
                                    v450 = v449 == false;
                                    if (v450){
                                        assert("The read index needs to be in range for the static array." && v449);
                                    } else {
                                    }
                                    long v451;
                                    v451 = v427.v[v441];
                                    long v452;
                                    v452 = v447 - v451;
                                    bool v454;
                                    if (v443){
                                        bool v453;
                                        v453 = v441 < 2l;
                                        v454 = v453;
                                    } else {
                                        v454 = false;
                                    }
                                    bool v455;
                                    v455 = v454 == false;
                                    if (v455){
                                        assert("The read index needs to be in range for the static array." && v454);
                                    } else {
                                    }
                                    v440.v[v441] = v452;
                                    v441 += 1l ;
                                }
                                long v456;
                                v456 = v150 + 1l;
                                v567 = try_round_12(v349, v148, v427, v456, v440, v152);
                                break;
                            }
                            default: {
                                assert("Invalid tag." && false);
                            }
                        }
                        v1059 = true; v1060 = v567;
                        break;
                    }
                    case 1: { // Human
                        v1059 = false; v1060 = v8;
                        break;
                    }
                    default: {
                        assert("Invalid tag." && false);
                    }
                }
                break;
            }
            case 5: { // G_Round'
                long v572 = v8.v.case5.v0; static_array<static_array<unsigned char,2l>,2l> v573 = v8.v.case5.v1; static_array<long,2l> v574 = v8.v.case5.v2; long v575 = v8.v.case5.v3; static_array<long,2l> v576 = v8.v.case5.v4; US8 v577 = v8.v.case5.v5; US4 v578 = v8.v.case5.v6;
                long v579;
                v579 = v575 % 2l;
                long v580;
                v580 = v5.length;
                bool v581;
                v581 = v580 < 128l;
                bool v582;
                v582 = v581 == false;
                if (v582){
                    assert("The length has to be less than the maximum length of the array." && v581);
                } else {
                }
                long v583;
                v583 = v580 + 1l;
                v5.length = v583;
                bool v584;
                v584 = 0l <= v580;
                bool v587;
                if (v584){
                    long v585;
                    v585 = v5.length;
                    bool v586;
                    v586 = v580 < v585;
                    v587 = v586;
                } else {
                    v587 = false;
                }
                bool v588;
                v588 = v587 == false;
                if (v588){
                    assert("The set index needs to be in range for the static array list." && v587);
                } else {
                }
                US3 v589;
                v589 = US3_2(v579, v578);
                v5.v[v580] = v589;
                US7 v879;
                switch (v578.tag) {
                    case 0: { // A_All_In
                        static_array<long,2l> v769;
                        long v770;
                        v770 = 0l;
                        while (while_method_4(v770)){
                            bool v772;
                            v772 = 0l <= v770;
                            bool v774;
                            if (v772){
                                bool v773;
                                v773 = v770 < 2l;
                                v774 = v773;
                            } else {
                                v774 = false;
                            }
                            bool v775;
                            v775 = v774 == false;
                            if (v775){
                                assert("The read index needs to be in range for the static array." && v774);
                            } else {
                            }
                            long v776;
                            v776 = v576.v[v770];
                            bool v778;
                            if (v772){
                                bool v777;
                                v777 = v770 < 2l;
                                v778 = v777;
                            } else {
                                v778 = false;
                            }
                            bool v779;
                            v779 = v778 == false;
                            if (v779){
                                assert("The read index needs to be in range for the static array." && v778);
                            } else {
                            }
                            long v780;
                            v780 = v574.v[v770];
                            long v781;
                            v781 = v776 + v780;
                            bool v783;
                            if (v772){
                                bool v782;
                                v782 = v770 < 2l;
                                v783 = v782;
                            } else {
                                v783 = false;
                            }
                            bool v784;
                            v784 = v783 == false;
                            if (v784){
                                assert("The read index needs to be in range for the static array." && v783);
                            } else {
                            }
                            v769.v[v770] = v781;
                            v770 += 1l ;
                        }
                        long v785;
                        v785 = v574.v[0l];
                        long v786; long v787;
                        Tuple7 tmp21 = Tuple7(1l, v785);
                        v786 = tmp21.v0; v787 = tmp21.v1;
                        while (while_method_4(v786)){
                            bool v789;
                            v789 = 0l <= v786;
                            bool v791;
                            if (v789){
                                bool v790;
                                v790 = v786 < 2l;
                                v791 = v790;
                            } else {
                                v791 = false;
                            }
                            bool v792;
                            v792 = v791 == false;
                            if (v792){
                                assert("The read index needs to be in range for the static array." && v791);
                            } else {
                            }
                            long v793;
                            v793 = v574.v[v786];
                            bool v794;
                            v794 = v787 >= v793;
                            long v795;
                            if (v794){
                                v795 = v787;
                            } else {
                                v795 = v793;
                            }
                            v787 = v795;
                            v786 += 1l ;
                        }
                        bool v796;
                        v796 = 0l <= v579;
                        bool v798;
                        if (v796){
                            bool v797;
                            v797 = v579 < 2l;
                            v798 = v797;
                        } else {
                            v798 = false;
                        }
                        bool v799;
                        v799 = v798 == false;
                        if (v799){
                            assert("The read index needs to be in range for the static array." && v798);
                        } else {
                        }
                        long v800;
                        v800 = v769.v[v579];
                        bool v801;
                        v801 = v787 < v800;
                        long v802;
                        if (v801){
                            v802 = v787;
                        } else {
                            v802 = v800;
                        }
                        static_array<long,2l> v803;
                        long v804;
                        v804 = 0l;
                        while (while_method_4(v804)){
                            bool v806;
                            v806 = 0l <= v804;
                            bool v808;
                            if (v806){
                                bool v807;
                                v807 = v804 < 2l;
                                v808 = v807;
                            } else {
                                v808 = false;
                            }
                            bool v809;
                            v809 = v808 == false;
                            if (v809){
                                assert("The read index needs to be in range for the static array." && v808);
                            } else {
                            }
                            long v810;
                            v810 = v574.v[v804];
                            bool v811;
                            v811 = v579 == v804;
                            long v812;
                            if (v811){
                                v812 = v802;
                            } else {
                                v812 = v810;
                            }
                            bool v814;
                            if (v806){
                                bool v813;
                                v813 = v804 < 2l;
                                v814 = v813;
                            } else {
                                v814 = false;
                            }
                            bool v815;
                            v815 = v814 == false;
                            if (v815){
                                assert("The read index needs to be in range for the static array." && v814);
                            } else {
                            }
                            v803.v[v804] = v812;
                            v804 += 1l ;
                        }
                        static_array<long,2l> v816;
                        long v817;
                        v817 = 0l;
                        while (while_method_4(v817)){
                            bool v819;
                            v819 = 0l <= v817;
                            bool v821;
                            if (v819){
                                bool v820;
                                v820 = v817 < 2l;
                                v821 = v820;
                            } else {
                                v821 = false;
                            }
                            bool v822;
                            v822 = v821 == false;
                            if (v822){
                                assert("The read index needs to be in range for the static array." && v821);
                            } else {
                            }
                            long v823;
                            v823 = v769.v[v817];
                            bool v825;
                            if (v819){
                                bool v824;
                                v824 = v817 < 2l;
                                v825 = v824;
                            } else {
                                v825 = false;
                            }
                            bool v826;
                            v826 = v825 == false;
                            if (v826){
                                assert("The read index needs to be in range for the static array." && v825);
                            } else {
                            }
                            long v827;
                            v827 = v803.v[v817];
                            long v828;
                            v828 = v823 - v827;
                            bool v830;
                            if (v819){
                                bool v829;
                                v829 = v817 < 2l;
                                v830 = v829;
                            } else {
                                v830 = false;
                            }
                            bool v831;
                            v831 = v830 == false;
                            if (v831){
                                assert("The read index needs to be in range for the static array." && v830);
                            } else {
                            }
                            v816.v[v817] = v828;
                            v817 += 1l ;
                        }
                        bool v833;
                        if (v796){
                            bool v832;
                            v832 = v579 < 2l;
                            v833 = v832;
                        } else {
                            v833 = false;
                        }
                        bool v834;
                        v834 = v833 == false;
                        if (v834){
                            assert("The read index needs to be in range for the static array." && v833);
                        } else {
                        }
                        long v835;
                        v835 = v816.v[v579];
                        long v836;
                        v836 = v787 + v835;
                        bool v838;
                        if (v796){
                            bool v837;
                            v837 = v579 < 2l;
                            v838 = v837;
                        } else {
                            v838 = false;
                        }
                        bool v839;
                        v839 = v838 == false;
                        if (v839){
                            assert("The read index needs to be in range for the static array." && v838);
                        } else {
                        }
                        long v840;
                        v840 = v769.v[v579];
                        bool v841;
                        v841 = v836 < v840;
                        long v842;
                        if (v841){
                            v842 = v836;
                        } else {
                            v842 = v840;
                        }
                        static_array<long,2l> v843;
                        long v844;
                        v844 = 0l;
                        while (while_method_4(v844)){
                            bool v846;
                            v846 = 0l <= v844;
                            bool v848;
                            if (v846){
                                bool v847;
                                v847 = v844 < 2l;
                                v848 = v847;
                            } else {
                                v848 = false;
                            }
                            bool v849;
                            v849 = v848 == false;
                            if (v849){
                                assert("The read index needs to be in range for the static array." && v848);
                            } else {
                            }
                            long v850;
                            v850 = v574.v[v844];
                            bool v851;
                            v851 = v579 == v844;
                            long v852;
                            if (v851){
                                v852 = v842;
                            } else {
                                v852 = v850;
                            }
                            bool v854;
                            if (v846){
                                bool v853;
                                v853 = v844 < 2l;
                                v854 = v853;
                            } else {
                                v854 = false;
                            }
                            bool v855;
                            v855 = v854 == false;
                            if (v855){
                                assert("The read index needs to be in range for the static array." && v854);
                            } else {
                            }
                            v843.v[v844] = v852;
                            v844 += 1l ;
                        }
                        static_array<long,2l> v856;
                        long v857;
                        v857 = 0l;
                        while (while_method_4(v857)){
                            bool v859;
                            v859 = 0l <= v857;
                            bool v861;
                            if (v859){
                                bool v860;
                                v860 = v857 < 2l;
                                v861 = v860;
                            } else {
                                v861 = false;
                            }
                            bool v862;
                            v862 = v861 == false;
                            if (v862){
                                assert("The read index needs to be in range for the static array." && v861);
                            } else {
                            }
                            long v863;
                            v863 = v769.v[v857];
                            bool v865;
                            if (v859){
                                bool v864;
                                v864 = v857 < 2l;
                                v865 = v864;
                            } else {
                                v865 = false;
                            }
                            bool v866;
                            v866 = v865 == false;
                            if (v866){
                                assert("The read index needs to be in range for the static array." && v865);
                            } else {
                            }
                            long v867;
                            v867 = v843.v[v857];
                            long v868;
                            v868 = v863 - v867;
                            bool v870;
                            if (v859){
                                bool v869;
                                v869 = v857 < 2l;
                                v870 = v869;
                            } else {
                                v870 = false;
                            }
                            bool v871;
                            v871 = v870 == false;
                            if (v871){
                                assert("The read index needs to be in range for the static array." && v870);
                            } else {
                            }
                            v856.v[v857] = v868;
                            v857 += 1l ;
                        }
                        bool v872;
                        v872 = v835 >= v572;
                        long v873;
                        if (v872){
                            v873 = v835;
                        } else {
                            v873 = v572;
                        }
                        long v874;
                        v874 = v575 + 1l;
                        v879 = try_round_12(v873, v573, v843, v874, v856, v577);
                        break;
                    }
                    case 1: { // A_Call
                        static_array<long,2l> v591;
                        long v592;
                        v592 = 0l;
                        while (while_method_4(v592)){
                            bool v594;
                            v594 = 0l <= v592;
                            bool v596;
                            if (v594){
                                bool v595;
                                v595 = v592 < 2l;
                                v596 = v595;
                            } else {
                                v596 = false;
                            }
                            bool v597;
                            v597 = v596 == false;
                            if (v597){
                                assert("The read index needs to be in range for the static array." && v596);
                            } else {
                            }
                            long v598;
                            v598 = v576.v[v592];
                            bool v600;
                            if (v594){
                                bool v599;
                                v599 = v592 < 2l;
                                v600 = v599;
                            } else {
                                v600 = false;
                            }
                            bool v601;
                            v601 = v600 == false;
                            if (v601){
                                assert("The read index needs to be in range for the static array." && v600);
                            } else {
                            }
                            long v602;
                            v602 = v574.v[v592];
                            long v603;
                            v603 = v598 + v602;
                            bool v605;
                            if (v594){
                                bool v604;
                                v604 = v592 < 2l;
                                v605 = v604;
                            } else {
                                v605 = false;
                            }
                            bool v606;
                            v606 = v605 == false;
                            if (v606){
                                assert("The read index needs to be in range for the static array." && v605);
                            } else {
                            }
                            v591.v[v592] = v603;
                            v592 += 1l ;
                        }
                        long v607;
                        v607 = v574.v[0l];
                        long v608; long v609;
                        Tuple7 tmp22 = Tuple7(1l, v607);
                        v608 = tmp22.v0; v609 = tmp22.v1;
                        while (while_method_4(v608)){
                            bool v611;
                            v611 = 0l <= v608;
                            bool v613;
                            if (v611){
                                bool v612;
                                v612 = v608 < 2l;
                                v613 = v612;
                            } else {
                                v613 = false;
                            }
                            bool v614;
                            v614 = v613 == false;
                            if (v614){
                                assert("The read index needs to be in range for the static array." && v613);
                            } else {
                            }
                            long v615;
                            v615 = v574.v[v608];
                            bool v616;
                            v616 = v609 >= v615;
                            long v617;
                            if (v616){
                                v617 = v609;
                            } else {
                                v617 = v615;
                            }
                            v609 = v617;
                            v608 += 1l ;
                        }
                        bool v618;
                        v618 = 0l <= v579;
                        bool v620;
                        if (v618){
                            bool v619;
                            v619 = v579 < 2l;
                            v620 = v619;
                        } else {
                            v620 = false;
                        }
                        bool v621;
                        v621 = v620 == false;
                        if (v621){
                            assert("The read index needs to be in range for the static array." && v620);
                        } else {
                        }
                        long v622;
                        v622 = v591.v[v579];
                        bool v623;
                        v623 = v609 < v622;
                        long v624;
                        if (v623){
                            v624 = v609;
                        } else {
                            v624 = v622;
                        }
                        static_array<long,2l> v625;
                        long v626;
                        v626 = 0l;
                        while (while_method_4(v626)){
                            bool v628;
                            v628 = 0l <= v626;
                            bool v630;
                            if (v628){
                                bool v629;
                                v629 = v626 < 2l;
                                v630 = v629;
                            } else {
                                v630 = false;
                            }
                            bool v631;
                            v631 = v630 == false;
                            if (v631){
                                assert("The read index needs to be in range for the static array." && v630);
                            } else {
                            }
                            long v632;
                            v632 = v574.v[v626];
                            bool v633;
                            v633 = v579 == v626;
                            long v634;
                            if (v633){
                                v634 = v624;
                            } else {
                                v634 = v632;
                            }
                            bool v636;
                            if (v628){
                                bool v635;
                                v635 = v626 < 2l;
                                v636 = v635;
                            } else {
                                v636 = false;
                            }
                            bool v637;
                            v637 = v636 == false;
                            if (v637){
                                assert("The read index needs to be in range for the static array." && v636);
                            } else {
                            }
                            v625.v[v626] = v634;
                            v626 += 1l ;
                        }
                        static_array<long,2l> v638;
                        long v639;
                        v639 = 0l;
                        while (while_method_4(v639)){
                            bool v641;
                            v641 = 0l <= v639;
                            bool v643;
                            if (v641){
                                bool v642;
                                v642 = v639 < 2l;
                                v643 = v642;
                            } else {
                                v643 = false;
                            }
                            bool v644;
                            v644 = v643 == false;
                            if (v644){
                                assert("The read index needs to be in range for the static array." && v643);
                            } else {
                            }
                            long v645;
                            v645 = v591.v[v639];
                            bool v647;
                            if (v641){
                                bool v646;
                                v646 = v639 < 2l;
                                v647 = v646;
                            } else {
                                v647 = false;
                            }
                            bool v648;
                            v648 = v647 == false;
                            if (v648){
                                assert("The read index needs to be in range for the static array." && v647);
                            } else {
                            }
                            long v649;
                            v649 = v625.v[v639];
                            long v650;
                            v650 = v645 - v649;
                            bool v652;
                            if (v641){
                                bool v651;
                                v651 = v639 < 2l;
                                v652 = v651;
                            } else {
                                v652 = false;
                            }
                            bool v653;
                            v653 = v652 == false;
                            if (v653){
                                assert("The read index needs to be in range for the static array." && v652);
                            } else {
                            }
                            v638.v[v639] = v650;
                            v639 += 1l ;
                        }
                        bool v654;
                        v654 = v579 < 2l;
                        if (v654){
                            long v655;
                            v655 = v575 + 1l;
                            v879 = try_round_12(v572, v573, v625, v655, v638, v577);
                        } else {
                            v879 = go_next_street_14(v572, v573, v625, v575, v638, v577);
                        }
                        break;
                    }
                    case 2: { // A_Fold
                        v879 = US7_1(v572, v573, v574, v575, v576, v577);
                        break;
                    }
                    case 3: { // A_Raise
                        long v659 = v578.v.case3.v0;
                        bool v660;
                        v660 = v572 <= v659;
                        bool v661;
                        v661 = v660 == false;
                        if (v661){
                            assert("The raise amount must match the minimum." && v660);
                        } else {
                        }
                        static_array<long,2l> v662;
                        long v663;
                        v663 = 0l;
                        while (while_method_4(v663)){
                            bool v665;
                            v665 = 0l <= v663;
                            bool v667;
                            if (v665){
                                bool v666;
                                v666 = v663 < 2l;
                                v667 = v666;
                            } else {
                                v667 = false;
                            }
                            bool v668;
                            v668 = v667 == false;
                            if (v668){
                                assert("The read index needs to be in range for the static array." && v667);
                            } else {
                            }
                            long v669;
                            v669 = v576.v[v663];
                            bool v671;
                            if (v665){
                                bool v670;
                                v670 = v663 < 2l;
                                v671 = v670;
                            } else {
                                v671 = false;
                            }
                            bool v672;
                            v672 = v671 == false;
                            if (v672){
                                assert("The read index needs to be in range for the static array." && v671);
                            } else {
                            }
                            long v673;
                            v673 = v574.v[v663];
                            long v674;
                            v674 = v669 + v673;
                            bool v676;
                            if (v665){
                                bool v675;
                                v675 = v663 < 2l;
                                v676 = v675;
                            } else {
                                v676 = false;
                            }
                            bool v677;
                            v677 = v676 == false;
                            if (v677){
                                assert("The read index needs to be in range for the static array." && v676);
                            } else {
                            }
                            v662.v[v663] = v674;
                            v663 += 1l ;
                        }
                        long v678;
                        v678 = v574.v[0l];
                        long v679; long v680;
                        Tuple7 tmp23 = Tuple7(1l, v678);
                        v679 = tmp23.v0; v680 = tmp23.v1;
                        while (while_method_4(v679)){
                            bool v682;
                            v682 = 0l <= v679;
                            bool v684;
                            if (v682){
                                bool v683;
                                v683 = v679 < 2l;
                                v684 = v683;
                            } else {
                                v684 = false;
                            }
                            bool v685;
                            v685 = v684 == false;
                            if (v685){
                                assert("The read index needs to be in range for the static array." && v684);
                            } else {
                            }
                            long v686;
                            v686 = v574.v[v679];
                            bool v687;
                            v687 = v680 >= v686;
                            long v688;
                            if (v687){
                                v688 = v680;
                            } else {
                                v688 = v686;
                            }
                            v680 = v688;
                            v679 += 1l ;
                        }
                        bool v689;
                        v689 = 0l <= v579;
                        bool v691;
                        if (v689){
                            bool v690;
                            v690 = v579 < 2l;
                            v691 = v690;
                        } else {
                            v691 = false;
                        }
                        bool v692;
                        v692 = v691 == false;
                        if (v692){
                            assert("The read index needs to be in range for the static array." && v691);
                        } else {
                        }
                        long v693;
                        v693 = v662.v[v579];
                        bool v694;
                        v694 = v680 < v693;
                        long v695;
                        if (v694){
                            v695 = v680;
                        } else {
                            v695 = v693;
                        }
                        static_array<long,2l> v696;
                        long v697;
                        v697 = 0l;
                        while (while_method_4(v697)){
                            bool v699;
                            v699 = 0l <= v697;
                            bool v701;
                            if (v699){
                                bool v700;
                                v700 = v697 < 2l;
                                v701 = v700;
                            } else {
                                v701 = false;
                            }
                            bool v702;
                            v702 = v701 == false;
                            if (v702){
                                assert("The read index needs to be in range for the static array." && v701);
                            } else {
                            }
                            long v703;
                            v703 = v574.v[v697];
                            bool v704;
                            v704 = v579 == v697;
                            long v705;
                            if (v704){
                                v705 = v695;
                            } else {
                                v705 = v703;
                            }
                            bool v707;
                            if (v699){
                                bool v706;
                                v706 = v697 < 2l;
                                v707 = v706;
                            } else {
                                v707 = false;
                            }
                            bool v708;
                            v708 = v707 == false;
                            if (v708){
                                assert("The read index needs to be in range for the static array." && v707);
                            } else {
                            }
                            v696.v[v697] = v705;
                            v697 += 1l ;
                        }
                        static_array<long,2l> v709;
                        long v710;
                        v710 = 0l;
                        while (while_method_4(v710)){
                            bool v712;
                            v712 = 0l <= v710;
                            bool v714;
                            if (v712){
                                bool v713;
                                v713 = v710 < 2l;
                                v714 = v713;
                            } else {
                                v714 = false;
                            }
                            bool v715;
                            v715 = v714 == false;
                            if (v715){
                                assert("The read index needs to be in range for the static array." && v714);
                            } else {
                            }
                            long v716;
                            v716 = v662.v[v710];
                            bool v718;
                            if (v712){
                                bool v717;
                                v717 = v710 < 2l;
                                v718 = v717;
                            } else {
                                v718 = false;
                            }
                            bool v719;
                            v719 = v718 == false;
                            if (v719){
                                assert("The read index needs to be in range for the static array." && v718);
                            } else {
                            }
                            long v720;
                            v720 = v696.v[v710];
                            long v721;
                            v721 = v716 - v720;
                            bool v723;
                            if (v712){
                                bool v722;
                                v722 = v710 < 2l;
                                v723 = v722;
                            } else {
                                v723 = false;
                            }
                            bool v724;
                            v724 = v723 == false;
                            if (v724){
                                assert("The read index needs to be in range for the static array." && v723);
                            } else {
                            }
                            v709.v[v710] = v721;
                            v710 += 1l ;
                        }
                        bool v726;
                        if (v689){
                            bool v725;
                            v725 = v579 < 2l;
                            v726 = v725;
                        } else {
                            v726 = false;
                        }
                        bool v727;
                        v727 = v726 == false;
                        if (v727){
                            assert("The read index needs to be in range for the static array." && v726);
                        } else {
                        }
                        long v728;
                        v728 = v709.v[v579];
                        bool v729;
                        v729 = v659 < v728;
                        bool v730;
                        v730 = v729 == false;
                        if (v730){
                            assert("The raise amount must be less than the stack size after calling." && v729);
                        } else {
                        }
                        long v731;
                        v731 = v680 + v659;
                        bool v733;
                        if (v689){
                            bool v732;
                            v732 = v579 < 2l;
                            v733 = v732;
                        } else {
                            v733 = false;
                        }
                        bool v734;
                        v734 = v733 == false;
                        if (v734){
                            assert("The read index needs to be in range for the static array." && v733);
                        } else {
                        }
                        long v735;
                        v735 = v662.v[v579];
                        bool v736;
                        v736 = v731 < v735;
                        long v737;
                        if (v736){
                            v737 = v731;
                        } else {
                            v737 = v735;
                        }
                        static_array<long,2l> v738;
                        long v739;
                        v739 = 0l;
                        while (while_method_4(v739)){
                            bool v741;
                            v741 = 0l <= v739;
                            bool v743;
                            if (v741){
                                bool v742;
                                v742 = v739 < 2l;
                                v743 = v742;
                            } else {
                                v743 = false;
                            }
                            bool v744;
                            v744 = v743 == false;
                            if (v744){
                                assert("The read index needs to be in range for the static array." && v743);
                            } else {
                            }
                            long v745;
                            v745 = v574.v[v739];
                            bool v746;
                            v746 = v579 == v739;
                            long v747;
                            if (v746){
                                v747 = v737;
                            } else {
                                v747 = v745;
                            }
                            bool v749;
                            if (v741){
                                bool v748;
                                v748 = v739 < 2l;
                                v749 = v748;
                            } else {
                                v749 = false;
                            }
                            bool v750;
                            v750 = v749 == false;
                            if (v750){
                                assert("The read index needs to be in range for the static array." && v749);
                            } else {
                            }
                            v738.v[v739] = v747;
                            v739 += 1l ;
                        }
                        static_array<long,2l> v751;
                        long v752;
                        v752 = 0l;
                        while (while_method_4(v752)){
                            bool v754;
                            v754 = 0l <= v752;
                            bool v756;
                            if (v754){
                                bool v755;
                                v755 = v752 < 2l;
                                v756 = v755;
                            } else {
                                v756 = false;
                            }
                            bool v757;
                            v757 = v756 == false;
                            if (v757){
                                assert("The read index needs to be in range for the static array." && v756);
                            } else {
                            }
                            long v758;
                            v758 = v662.v[v752];
                            bool v760;
                            if (v754){
                                bool v759;
                                v759 = v752 < 2l;
                                v760 = v759;
                            } else {
                                v760 = false;
                            }
                            bool v761;
                            v761 = v760 == false;
                            if (v761){
                                assert("The read index needs to be in range for the static array." && v760);
                            } else {
                            }
                            long v762;
                            v762 = v738.v[v752];
                            long v763;
                            v763 = v758 - v762;
                            bool v765;
                            if (v754){
                                bool v764;
                                v764 = v752 < 2l;
                                v765 = v764;
                            } else {
                                v765 = false;
                            }
                            bool v766;
                            v766 = v765 == false;
                            if (v766){
                                assert("The read index needs to be in range for the static array." && v765);
                            } else {
                            }
                            v751.v[v752] = v763;
                            v752 += 1l ;
                        }
                        long v767;
                        v767 = v575 + 1l;
                        v879 = try_round_12(v659, v573, v738, v767, v751, v577);
                        break;
                    }
                    default: {
                        assert("Invalid tag." && false);
                    }
                }
                v1059 = true; v1060 = v879;
                break;
            }
            case 6: { // G_Showdown
                long v34 = v8.v.case6.v0; static_array<static_array<unsigned char,2l>,2l> v35 = v8.v.case6.v1; static_array<long,2l> v36 = v8.v.case6.v2; long v37 = v8.v.case6.v3; static_array<long,2l> v38 = v8.v.case6.v4; US8 v39 = v8.v.case6.v5;
                static_array<unsigned char,5l> v42;
                switch (v39.tag) {
                    case 2: { // River
                        static_array<unsigned char,5l> v40 = v39.v.case2.v0;
                        v42 = v40;
                        break;
                    }
                    default: {
                        printf("%s\n", "Invalid street in showdown.");
                        asm("exit;");
                    }
                }
                static_array<unsigned char,2l> v43;
                v43 = v35.v[0l];
                static_array<unsigned char,7l> v44;
                long v45;
                v45 = 0l;
                while (while_method_4(v45)){
                    bool v47;
                    v47 = 0l <= v45;
                    bool v49;
                    if (v47){
                        bool v48;
                        v48 = v45 < 2l;
                        v49 = v48;
                    } else {
                        v49 = false;
                    }
                    bool v50;
                    v50 = v49 == false;
                    if (v50){
                        assert("The read index needs to be in range for the static array." && v49);
                    } else {
                    }
                    unsigned char v51;
                    v51 = v43.v[v45];
                    bool v53;
                    if (v47){
                        bool v52;
                        v52 = v45 < 7l;
                        v53 = v52;
                    } else {
                        v53 = false;
                    }
                    bool v54;
                    v54 = v53 == false;
                    if (v54){
                        assert("The read index needs to be in range for the static array." && v53);
                    } else {
                    }
                    v44.v[v45] = v51;
                    v45 += 1l ;
                }
                long v55;
                v55 = 0l;
                while (while_method_2(v55)){
                    bool v57;
                    v57 = 0l <= v55;
                    bool v59;
                    if (v57){
                        bool v58;
                        v58 = v55 < 5l;
                        v59 = v58;
                    } else {
                        v59 = false;
                    }
                    bool v60;
                    v60 = v59 == false;
                    if (v60){
                        assert("The read index needs to be in range for the static array." && v59);
                    } else {
                    }
                    unsigned char v61;
                    v61 = v42.v[v55];
                    long v62;
                    v62 = 2l + v55;
                    bool v63;
                    v63 = 0l <= v62;
                    bool v65;
                    if (v63){
                        bool v64;
                        v64 = v62 < 7l;
                        v65 = v64;
                    } else {
                        v65 = false;
                    }
                    bool v66;
                    v66 = v65 == false;
                    if (v66){
                        assert("The read index needs to be in range for the static array." && v65);
                    } else {
                    }
                    v44.v[v62] = v61;
                    v55 += 1l ;
                }
                static_array<unsigned char,5l> v67; char v68;
                Tuple1 tmp48 = score_21(v44);
                v67 = tmp48.v0; v68 = tmp48.v1;
                static_array<unsigned char,2l> v69;
                v69 = v35.v[1l];
                static_array<unsigned char,7l> v70;
                long v71;
                v71 = 0l;
                while (while_method_4(v71)){
                    bool v73;
                    v73 = 0l <= v71;
                    bool v75;
                    if (v73){
                        bool v74;
                        v74 = v71 < 2l;
                        v75 = v74;
                    } else {
                        v75 = false;
                    }
                    bool v76;
                    v76 = v75 == false;
                    if (v76){
                        assert("The read index needs to be in range for the static array." && v75);
                    } else {
                    }
                    unsigned char v77;
                    v77 = v69.v[v71];
                    bool v79;
                    if (v73){
                        bool v78;
                        v78 = v71 < 7l;
                        v79 = v78;
                    } else {
                        v79 = false;
                    }
                    bool v80;
                    v80 = v79 == false;
                    if (v80){
                        assert("The read index needs to be in range for the static array." && v79);
                    } else {
                    }
                    v70.v[v71] = v77;
                    v71 += 1l ;
                }
                long v81;
                v81 = 0l;
                while (while_method_2(v81)){
                    bool v83;
                    v83 = 0l <= v81;
                    bool v85;
                    if (v83){
                        bool v84;
                        v84 = v81 < 5l;
                        v85 = v84;
                    } else {
                        v85 = false;
                    }
                    bool v86;
                    v86 = v85 == false;
                    if (v86){
                        assert("The read index needs to be in range for the static array." && v85);
                    } else {
                    }
                    unsigned char v87;
                    v87 = v42.v[v81];
                    long v88;
                    v88 = 2l + v81;
                    bool v89;
                    v89 = 0l <= v88;
                    bool v91;
                    if (v89){
                        bool v90;
                        v90 = v88 < 7l;
                        v91 = v90;
                    } else {
                        v91 = false;
                    }
                    bool v92;
                    v92 = v91 == false;
                    if (v92){
                        assert("The read index needs to be in range for the static array." && v91);
                    } else {
                    }
                    v70.v[v88] = v87;
                    v81 += 1l ;
                }
                static_array<unsigned char,5l> v93; char v94;
                Tuple1 tmp49 = score_21(v70);
                v93 = tmp49.v0; v94 = tmp49.v1;
                long v95;
                v95 = v37 % 2l;
                bool v96;
                v96 = 0l <= v95;
                bool v98;
                if (v96){
                    bool v97;
                    v97 = v95 < 2l;
                    v98 = v97;
                } else {
                    v98 = false;
                }
                bool v99;
                v99 = v98 == false;
                if (v99){
                    assert("The read index needs to be in range for the static array." && v98);
                } else {
                }
                long v100;
                v100 = v36.v[v95];
                bool v101;
                v101 = v68 < v94;
                US10 v107;
                if (v101){
                    v107 = US10_2();
                } else {
                    bool v103;
                    v103 = v68 > v94;
                    if (v103){
                        v107 = US10_1();
                    } else {
                        v107 = US10_0();
                    }
                }
                US10 v129;
                switch (v107.tag) {
                    case 0: { // Eq
                        US10 v108;
                        v108 = US10_0();
                        long v109;
                        v109 = 0l;
                        while (while_method_2(v109)){
                            bool v111;
                            v111 = 0l <= v109;
                            bool v113;
                            if (v111){
                                bool v112;
                                v112 = v109 < 5l;
                                v113 = v112;
                            } else {
                                v113 = false;
                            }
                            bool v114;
                            v114 = v113 == false;
                            if (v114){
                                assert("The read index needs to be in range for the static array." && v113);
                            } else {
                            }
                            unsigned char v115;
                            v115 = v67.v[v109];
                            bool v117;
                            if (v111){
                                bool v116;
                                v116 = v109 < 5l;
                                v117 = v116;
                            } else {
                                v117 = false;
                            }
                            bool v118;
                            v118 = v117 == false;
                            if (v118){
                                assert("The read index needs to be in range for the static array." && v117);
                            } else {
                            }
                            unsigned char v119;
                            v119 = v93.v[v109];
                            bool v120;
                            v120 = v115 < v119;
                            US10 v126;
                            if (v120){
                                v126 = US10_2();
                            } else {
                                bool v122;
                                v122 = v115 > v119;
                                if (v122){
                                    v126 = US10_1();
                                } else {
                                    v126 = US10_0();
                                }
                            }
                            bool v127;
                            switch (v126.tag) {
                                case 0: { // Eq
                                    v127 = true;
                                    break;
                                }
                                default: {
                                    v127 = false;
                                }
                            }
                            bool v128;
                            v128 = v127 == false;
                            if (v128){
                                v108 = v126;
                                break;
                            } else {
                            }
                            v109 += 1l ;
                        }
                        v129 = v108;
                        break;
                    }
                    default: {
                        v129 = v107;
                    }
                }
                long v134; long v135;
                switch (v129.tag) {
                    case 0: { // Eq
                        v134 = 0l; v135 = -1l;
                        break;
                    }
                    case 1: { // Gt
                        v134 = v100; v135 = 0l;
                        break;
                    }
                    case 2: { // Lt
                        v134 = v100; v135 = 1l;
                        break;
                    }
                    default: {
                        assert("Invalid tag." && false);
                    }
                }
                static_array<Tuple1,2l> v136;
                v136.v[0l] = Tuple1(v67, v68);
                v136.v[1l] = Tuple1(v93, v94);
                long v137;
                v137 = v5.length;
                bool v138;
                v138 = v137 < 128l;
                bool v139;
                v139 = v138 == false;
                if (v139){
                    assert("The length has to be less than the maximum length of the array." && v138);
                } else {
                }
                long v140;
                v140 = v137 + 1l;
                v5.length = v140;
                bool v141;
                v141 = 0l <= v137;
                bool v144;
                if (v141){
                    long v142;
                    v142 = v5.length;
                    bool v143;
                    v143 = v137 < v142;
                    v144 = v143;
                } else {
                    v144 = false;
                }
                bool v145;
                v145 = v144 == false;
                if (v145){
                    assert("The set index needs to be in range for the static array list." && v144);
                } else {
                }
                US3 v146;
                v146 = US3_4(v134, v136, v135);
                v5.v[v137] = v146;
                v1059 = false; v1060 = v8;
                break;
            }
            case 7: { // G_Turn
                long v905 = v8.v.case7.v0; static_array<static_array<unsigned char,2l>,2l> v906 = v8.v.case7.v1; static_array<long,2l> v907 = v8.v.case7.v2; long v908 = v8.v.case7.v3; static_array<long,2l> v909 = v8.v.case7.v4; US8 v910 = v8.v.case7.v5;
                static_array<unsigned char,1l> v911; unsigned long long v912;
                Tuple9 tmp50 = draw_cards_16(v2, v6);
                v911 = tmp50.v0; v912 = tmp50.v1;
                v0 = v912;
                static_array_list<unsigned char,5l,long> v913;
                v913 = get_community_cards_17(v910, v911);
                long v914;
                v914 = v5.length;
                bool v915;
                v915 = v914 < 128l;
                bool v916;
                v916 = v915 == false;
                if (v916){
                    assert("The length has to be less than the maximum length of the array." && v915);
                } else {
                }
                long v917;
                v917 = v914 + 1l;
                v5.length = v917;
                bool v918;
                v918 = 0l <= v914;
                bool v921;
                if (v918){
                    long v919;
                    v919 = v5.length;
                    bool v920;
                    v920 = v914 < v919;
                    v921 = v920;
                } else {
                    v921 = false;
                }
                bool v922;
                v922 = v921 == false;
                if (v922){
                    assert("The set index needs to be in range for the static array list." && v921);
                } else {
                }
                US3 v923;
                v923 = US3_0(v913);
                v5.v[v914] = v923;
                US8 v950;
                switch (v910.tag) {
                    case 0: { // Flop
                        static_array<unsigned char,3l> v924 = v910.v.case0.v0;
                        static_array<unsigned char,4l> v925;
                        long v926;
                        v926 = 0l;
                        while (while_method_1(v926)){
                            bool v928;
                            v928 = 0l <= v926;
                            bool v930;
                            if (v928){
                                bool v929;
                                v929 = v926 < 3l;
                                v930 = v929;
                            } else {
                                v930 = false;
                            }
                            bool v931;
                            v931 = v930 == false;
                            if (v931){
                                assert("The read index needs to be in range for the static array." && v930);
                            } else {
                            }
                            unsigned char v932;
                            v932 = v924.v[v926];
                            bool v934;
                            if (v928){
                                bool v933;
                                v933 = v926 < 4l;
                                v934 = v933;
                            } else {
                                v934 = false;
                            }
                            bool v935;
                            v935 = v934 == false;
                            if (v935){
                                assert("The read index needs to be in range for the static array." && v934);
                            } else {
                            }
                            v925.v[v926] = v932;
                            v926 += 1l ;
                        }
                        long v936;
                        v936 = 0l;
                        while (while_method_5(v936)){
                            bool v938;
                            v938 = 0l <= v936;
                            bool v940;
                            if (v938){
                                bool v939;
                                v939 = v936 < 1l;
                                v940 = v939;
                            } else {
                                v940 = false;
                            }
                            bool v941;
                            v941 = v940 == false;
                            if (v941){
                                assert("The read index needs to be in range for the static array." && v940);
                            } else {
                            }
                            unsigned char v942;
                            v942 = v911.v[v936];
                            long v943;
                            v943 = 3l + v936;
                            bool v944;
                            v944 = 0l <= v943;
                            bool v946;
                            if (v944){
                                bool v945;
                                v945 = v943 < 4l;
                                v946 = v945;
                            } else {
                                v946 = false;
                            }
                            bool v947;
                            v947 = v946 == false;
                            if (v947){
                                assert("The read index needs to be in range for the static array." && v946);
                            } else {
                            }
                            v925.v[v943] = v942;
                            v936 += 1l ;
                        }
                        v950 = US8_3(v925);
                        break;
                    }
                    default: {
                        printf("%s\n", "Invalid street in turn.");
                        asm("exit;");
                    }
                }
                long v951;
                v951 = 2l;
                long v952;
                v952 = 0l;
                US7 v953;
                v953 = try_round_12(v951, v906, v907, v952, v909, v950);
                v1059 = true; v1060 = v953;
                break;
            }
            default: {
                assert("Invalid tag." && false);
            }
        }
        v7 = v1059;
        v8 = v1060;
    }
    return v8;
}
__device__ Tuple2 play_loop_6(US6 v0, static_array<US2,2l> v1, US9 v2, unsigned long long & v3, static_array_list<US3,128l,long> & v4, curandStatePhilox4_32_10_t & v5, US7 v6){
    US7 v7;
    v7 = play_loop_inner_7(v3, v4, v5, v1, v6);
    switch (v7.tag) {
        case 1: { // G_Fold
            long v24 = v7.v.case1.v0; static_array<static_array<unsigned char,2l>,2l> v25 = v7.v.case1.v1; static_array<long,2l> v26 = v7.v.case1.v2; long v27 = v7.v.case1.v3; static_array<long,2l> v28 = v7.v.case1.v4; US8 v29 = v7.v.case1.v5;
            US6 v30;
            v30 = US6_0();
            US9 v31;
            v31 = US9_1(v24, v25, v26, v27, v28, v29);
            return Tuple2(v30, v1, v31);
            break;
        }
        case 4: { // G_Round
            long v8 = v7.v.case4.v0; static_array<static_array<unsigned char,2l>,2l> v9 = v7.v.case4.v1; static_array<long,2l> v10 = v7.v.case4.v2; long v11 = v7.v.case4.v3; static_array<long,2l> v12 = v7.v.case4.v4; US8 v13 = v7.v.case4.v5;
            US6 v14;
            v14 = US6_1(v7);
            US9 v15;
            v15 = US9_2(v8, v9, v10, v11, v12, v13);
            return Tuple2(v14, v1, v15);
            break;
        }
        case 6: { // G_Showdown
            long v16 = v7.v.case6.v0; static_array<static_array<unsigned char,2l>,2l> v17 = v7.v.case6.v1; static_array<long,2l> v18 = v7.v.case6.v2; long v19 = v7.v.case6.v3; static_array<long,2l> v20 = v7.v.case6.v4; US8 v21 = v7.v.case6.v5;
            US6 v22;
            v22 = US6_0();
            US9 v23;
            v23 = US9_1(v16, v17, v18, v19, v20, v21);
            return Tuple2(v22, v1, v23);
            break;
        }
        default: {
            printf("%s\n", "Unexpected node received in play_loop.");
            asm("exit;");
        }
    }
}
__device__ void write_23(char v0){
    const char * v1;
    v1 = "%c";
    printf(v1,v0);
    return ;
}
__device__ void write_24(){
    return ;
}
__device__ void write_25(const char * v0){
    const char * v1;
    v1 = "%s";
    printf(v1,v0);
    return ;
}
__device__ void write_29(unsigned long long v0){
    const char * v1;
    v1 = "%u";
    printf(v1,v0);
    return ;
}
__device__ void write_28(unsigned long long v0){
    return write_29(v0);
}
__device__ inline bool while_method_13(long v0, long v1){
    bool v2;
    v2 = v1 < v0;
    return v2;
}
__device__ void write_32(){
    const char * v0;
    v0 = "CommunityCardsAre";
    return write_25(v0);
}
__device__ void write_34(unsigned char v0){
    unsigned char v1;
    v1 = v0 / 4u;
    bool v2;
    v2 = 12u == v1;
    char v27;
    if (v2){
        v27 = 'A';
    } else {
        bool v3;
        v3 = 11u == v1;
        if (v3){
            v27 = 'K';
        } else {
            bool v4;
            v4 = 10u == v1;
            if (v4){
                v27 = 'Q';
            } else {
                bool v5;
                v5 = 9u == v1;
                if (v5){
                    v27 = 'J';
                } else {
                    bool v6;
                    v6 = 8u == v1;
                    if (v6){
                        v27 = 'T';
                    } else {
                        bool v7;
                        v7 = 7u == v1;
                        if (v7){
                            v27 = '9';
                        } else {
                            bool v8;
                            v8 = 6u == v1;
                            if (v8){
                                v27 = '8';
                            } else {
                                bool v9;
                                v9 = 5u == v1;
                                if (v9){
                                    v27 = '7';
                                } else {
                                    bool v10;
                                    v10 = 4u == v1;
                                    if (v10){
                                        v27 = '6';
                                    } else {
                                        bool v11;
                                        v11 = 3u == v1;
                                        if (v11){
                                            v27 = '5';
                                        } else {
                                            bool v12;
                                            v12 = 2u == v1;
                                            if (v12){
                                                v27 = '4';
                                            } else {
                                                bool v13;
                                                v13 = 1u == v1;
                                                if (v13){
                                                    v27 = '3';
                                                } else {
                                                    bool v14;
                                                    v14 = 0u == v1;
                                                    if (v14){
                                                        v27 = '2';
                                                    } else {
                                                        v27 = '?';
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    unsigned char v28;
    v28 = v0 % 4u;
    bool v29;
    v29 = 3u == v28;
    char v36;
    if (v29){
        v36 = 'H';
    } else {
        bool v30;
        v30 = 2u == v28;
        if (v30){
            v36 = 'S';
        } else {
            bool v31;
            v31 = 1u == v28;
            if (v31){
                v36 = 'C';
            } else {
                bool v32;
                v32 = 0u == v28;
                if (v32){
                    v36 = 'D';
                } else {
                    v36 = '?';
                }
            }
        }
    }
    write_23(v27);
    return write_23(v36);
}
__device__ void write_33(static_array_list<unsigned char,5l,long> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = v0.length;
    bool v3;
    v3 = 100l < v2;
    long v4;
    if (v3){
        v4 = 100l;
    } else {
        v4 = v2;
    }
    long v5;
    v5 = 0l;
    while (while_method_13(v4, v5)){
        bool v7;
        v7 = 0l <= v5;
        bool v10;
        if (v7){
            long v8;
            v8 = v0.length;
            bool v9;
            v9 = v5 < v8;
            v10 = v9;
        } else {
            v10 = false;
        }
        bool v11;
        v11 = v10 == false;
        if (v11){
            assert("The read index needs to be in range for the static array list." && v10);
        } else {
        }
        unsigned char v12;
        v12 = v0.v[v5];
        write_34(v12);
        long v13;
        v13 = v5 + 1l;
        long v14;
        v14 = v0.length;
        bool v15;
        v15 = v13 < v14;
        if (v15){
            const char * v16;
            v16 = "; ";
            write_25(v16);
        } else {
        }
        v5 += 1l ;
    }
    long v17;
    v17 = v0.length;
    bool v18;
    v18 = v17 > 100l;
    if (v18){
        const char * v19;
        v19 = "; ...";
        write_25(v19);
    } else {
    }
    const char * v20;
    v20 = "]";
    return write_25(v20);
}
__device__ void write_35(){
    const char * v0;
    v0 = "Fold";
    return write_25(v0);
}
__device__ void write_37(long v0){
    const char * v1;
    v1 = "%d";
    printf(v1,v0);
    return ;
}
__device__ void write_36(long v0, long v1){
    char v2;
    v2 = '{';
    write_23(v2);
    write_24();
    const char * v3;
    v3 = "chips_won";
    write_25(v3);
    const char * v4;
    v4 = " = ";
    write_25(v4);
    write_37(v0);
    const char * v5;
    v5 = "; ";
    write_25(v5);
    const char * v6;
    v6 = "winner_id";
    write_25(v6);
    write_25(v4);
    write_37(v1);
    char v7;
    v7 = '}';
    return write_23(v7);
}
__device__ void write_38(){
    const char * v0;
    v0 = "PlayerAction";
    return write_25(v0);
}
__device__ void write_41(){
    const char * v0;
    v0 = "A_All_In";
    return write_25(v0);
}
__device__ void write_42(){
    const char * v0;
    v0 = "A_Call";
    return write_25(v0);
}
__device__ void write_43(){
    const char * v0;
    v0 = "A_Fold";
    return write_25(v0);
}
__device__ void write_44(){
    const char * v0;
    v0 = "A_Raise";
    return write_25(v0);
}
__device__ void write_40(US4 v0){
    switch (v0.tag) {
        case 0: { // A_All_In
            return write_41();
            break;
        }
        case 1: { // A_Call
            return write_42();
            break;
        }
        case 2: { // A_Fold
            return write_43();
            break;
        }
        case 3: { // A_Raise
            long v1 = v0.v.case3.v0;
            write_44();
            const char * v2;
            v2 = "(";
            write_25(v2);
            write_37(v1);
            const char * v3;
            v3 = ")";
            return write_25(v3);
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ void write_39(long v0, US4 v1){
    write_37(v0);
    const char * v2;
    v2 = ", ";
    write_25(v2);
    return write_40(v1);
}
__device__ void write_45(){
    const char * v0;
    v0 = "PlayerGotCards";
    return write_25(v0);
}
__device__ void write_47(static_array<unsigned char,2l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_4(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 2l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        unsigned char v8;
        v8 = v0.v[v2];
        write_34(v8);
        long v9;
        v9 = v2 + 1l;
        bool v10;
        v10 = v9 < 2l;
        if (v10){
            const char * v11;
            v11 = "; ";
            write_25(v11);
        } else {
        }
        v2 += 1l ;
    }
    const char * v12;
    v12 = "]";
    return write_25(v12);
}
__device__ void write_46(long v0, static_array<unsigned char,2l> v1){
    write_37(v0);
    const char * v2;
    v2 = ", ";
    write_25(v2);
    return write_47(v1);
}
__device__ void write_48(){
    const char * v0;
    v0 = "Showdown";
    return write_25(v0);
}
__device__ void write_60(const char * v0, unsigned char v1){
    write_25(v0);
    const char * v2;
    v2 = ", ";
    write_25(v2);
    return write_34(v1);
}
__device__ void write_59(unsigned char v0, const char * v1, unsigned char v2){
    write_34(v0);
    const char * v3;
    v3 = ", ";
    write_25(v3);
    return write_60(v1, v2);
}
__device__ void write_58(const char * v0, unsigned char v1, unsigned char v2){
    write_25(v0);
    const char * v3;
    v3 = ", ";
    write_25(v3);
    return write_59(v1, v0, v2);
}
__device__ void write_57(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3){
    write_34(v0);
    const char * v4;
    v4 = ", ";
    write_25(v4);
    return write_58(v1, v2, v3);
}
__device__ void write_56(const char * v0, unsigned char v1, unsigned char v2, unsigned char v3){
    write_25(v0);
    const char * v4;
    v4 = ", ";
    write_25(v4);
    return write_57(v1, v0, v2, v3);
}
__device__ void write_55(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3, unsigned char v4){
    write_34(v0);
    const char * v5;
    v5 = ", ";
    write_25(v5);
    return write_56(v1, v2, v3, v4);
}
__device__ void write_54(const char * v0, unsigned char v1, unsigned char v2, unsigned char v3, unsigned char v4){
    write_25(v0);
    const char * v5;
    v5 = ", ";
    write_25(v5);
    return write_55(v1, v0, v2, v3, v4);
}
__device__ void write_53(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3, unsigned char v4, unsigned char v5){
    write_34(v0);
    const char * v6;
    v6 = ", ";
    write_25(v6);
    return write_54(v1, v2, v3, v4, v5);
}
__device__ void write_61(char v0){
    const char * v1;
    v1 = "%d";
    printf(v1,v0);
    return ;
}
__device__ void write_52(unsigned char v0, const char * v1, unsigned char v2, unsigned char v3, unsigned char v4, unsigned char v5, char v6){
    char v7;
    v7 = '{';
    write_23(v7);
    write_24();
    const char * v8;
    v8 = "hand";
    write_25(v8);
    const char * v9;
    v9 = " = ";
    write_25(v9);
    write_53(v0, v1, v2, v3, v4, v5);
    const char * v10;
    v10 = "; ";
    write_25(v10);
    const char * v11;
    v11 = "score";
    write_25(v11);
    write_25(v9);
    write_61(v6);
    char v12;
    v12 = '}';
    return write_23(v12);
}
__device__ void write_51(static_array<unsigned char,5l> v0, char v1){
    unsigned char v2;
    v2 = v0.v[0l];
    unsigned char v3;
    v3 = v0.v[1l];
    unsigned char v4;
    v4 = v0.v[2l];
    unsigned char v5;
    v5 = v0.v[3l];
    unsigned char v6;
    v6 = v0.v[4l];
    const char * v7;
    v7 = ", ";
    return write_52(v2, v7, v3, v4, v5, v6, v1);
}
__device__ void write_50(static_array<Tuple1,2l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_4(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 2l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        static_array<unsigned char,5l> v8; char v9;
        Tuple1 tmp53 = v0.v[v2];
        v8 = tmp53.v0; v9 = tmp53.v1;
        write_51(v8, v9);
        long v10;
        v10 = v2 + 1l;
        bool v11;
        v11 = v10 < 2l;
        if (v11){
            const char * v12;
            v12 = "; ";
            write_25(v12);
        } else {
        }
        v2 += 1l ;
    }
    const char * v13;
    v13 = "]";
    return write_25(v13);
}
__device__ void write_49(long v0, static_array<Tuple1,2l> v1, long v2){
    char v3;
    v3 = '{';
    write_23(v3);
    write_24();
    const char * v4;
    v4 = "chips_won";
    write_25(v4);
    const char * v5;
    v5 = " = ";
    write_25(v5);
    write_37(v0);
    const char * v6;
    v6 = "; ";
    write_25(v6);
    const char * v7;
    v7 = "hands_shown";
    write_25(v7);
    write_25(v5);
    write_50(v1);
    write_25(v6);
    const char * v8;
    v8 = "winner_id";
    write_25(v8);
    write_25(v5);
    write_37(v2);
    char v9;
    v9 = '}';
    return write_23(v9);
}
__device__ void write_31(US3 v0){
    switch (v0.tag) {
        case 0: { // CommunityCardsAre
            static_array_list<unsigned char,5l,long> v1 = v0.v.case0.v0;
            write_32();
            const char * v2;
            v2 = "(";
            write_25(v2);
            write_33(v1);
            const char * v3;
            v3 = ")";
            return write_25(v3);
            break;
        }
        case 1: { // Fold
            long v4 = v0.v.case1.v0; long v5 = v0.v.case1.v1;
            write_35();
            const char * v6;
            v6 = "(";
            write_25(v6);
            write_36(v4, v5);
            const char * v7;
            v7 = ")";
            return write_25(v7);
            break;
        }
        case 2: { // PlayerAction
            long v8 = v0.v.case2.v0; US4 v9 = v0.v.case2.v1;
            write_38();
            const char * v10;
            v10 = "(";
            write_25(v10);
            write_39(v8, v9);
            const char * v11;
            v11 = ")";
            return write_25(v11);
            break;
        }
        case 3: { // PlayerGotCards
            long v12 = v0.v.case3.v0; static_array<unsigned char,2l> v13 = v0.v.case3.v1;
            write_45();
            const char * v14;
            v14 = "(";
            write_25(v14);
            write_46(v12, v13);
            const char * v15;
            v15 = ")";
            return write_25(v15);
            break;
        }
        case 4: { // Showdown
            long v16 = v0.v.case4.v0; static_array<Tuple1,2l> v17 = v0.v.case4.v1; long v18 = v0.v.case4.v2;
            write_48();
            const char * v19;
            v19 = "(";
            write_25(v19);
            write_49(v16, v17, v18);
            const char * v20;
            v20 = ")";
            return write_25(v20);
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ void write_30(static_array_list<US3,128l,long> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = v0.length;
    bool v3;
    v3 = 100l < v2;
    long v4;
    if (v3){
        v4 = 100l;
    } else {
        v4 = v2;
    }
    long v5;
    v5 = 0l;
    while (while_method_13(v4, v5)){
        bool v7;
        v7 = 0l <= v5;
        bool v10;
        if (v7){
            long v8;
            v8 = v0.length;
            bool v9;
            v9 = v5 < v8;
            v10 = v9;
        } else {
            v10 = false;
        }
        bool v11;
        v11 = v10 == false;
        if (v11){
            assert("The read index needs to be in range for the static array list." && v10);
        } else {
        }
        US3 v12;
        v12 = v0.v[v5];
        write_31(v12);
        long v13;
        v13 = v5 + 1l;
        long v14;
        v14 = v0.length;
        bool v15;
        v15 = v13 < v14;
        if (v15){
            const char * v16;
            v16 = "; ";
            write_25(v16);
        } else {
        }
        v5 += 1l ;
    }
    long v17;
    v17 = v0.length;
    bool v18;
    v18 = v17 > 100l;
    if (v18){
        const char * v19;
        v19 = "; ...";
        write_25(v19);
    } else {
    }
    const char * v20;
    v20 = "]";
    return write_25(v20);
}
__device__ void write_27(unsigned long long v0, static_array_list<US3,128l,long> v1){
    char v2;
    v2 = '{';
    write_23(v2);
    write_24();
    const char * v3;
    v3 = "deck";
    write_25(v3);
    const char * v4;
    v4 = " = ";
    write_25(v4);
    write_28(v0);
    const char * v5;
    v5 = "; ";
    write_25(v5);
    const char * v6;
    v6 = "messages";
    write_25(v6);
    write_25(v4);
    write_30(v1);
    char v7;
    v7 = '}';
    return write_23(v7);
}
__device__ void write_64(){
    const char * v0;
    v0 = "None";
    return write_25(v0);
}
__device__ void write_65(){
    const char * v0;
    v0 = "Some";
    return write_25(v0);
}
__device__ void write_67(){
    const char * v0;
    v0 = "G_Flop";
    return write_25(v0);
}
__device__ void write_69(static_array<static_array<unsigned char,2l>,2l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_4(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 2l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        static_array<unsigned char,2l> v8;
        v8 = v0.v[v2];
        write_47(v8);
        long v9;
        v9 = v2 + 1l;
        bool v10;
        v10 = v9 < 2l;
        if (v10){
            const char * v11;
            v11 = "; ";
            write_25(v11);
        } else {
        }
        v2 += 1l ;
    }
    const char * v12;
    v12 = "]";
    return write_25(v12);
}
__device__ void write_70(static_array<long,2l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_4(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 2l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        long v8;
        v8 = v0.v[v2];
        write_37(v8);
        long v9;
        v9 = v2 + 1l;
        bool v10;
        v10 = v9 < 2l;
        if (v10){
            const char * v11;
            v11 = "; ";
            write_25(v11);
        } else {
        }
        v2 += 1l ;
    }
    const char * v12;
    v12 = "]";
    return write_25(v12);
}
__device__ void write_72(){
    const char * v0;
    v0 = "Flop";
    return write_25(v0);
}
__device__ void write_73(static_array<unsigned char,3l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_1(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 3l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        unsigned char v8;
        v8 = v0.v[v2];
        write_34(v8);
        long v9;
        v9 = v2 + 1l;
        bool v10;
        v10 = v9 < 3l;
        if (v10){
            const char * v11;
            v11 = "; ";
            write_25(v11);
        } else {
        }
        v2 += 1l ;
    }
    const char * v12;
    v12 = "]";
    return write_25(v12);
}
__device__ void write_74(){
    const char * v0;
    v0 = "Preflop";
    return write_25(v0);
}
__device__ void write_75(){
    const char * v0;
    v0 = "River";
    return write_25(v0);
}
__device__ void write_76(static_array<unsigned char,5l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_2(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 5l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        unsigned char v8;
        v8 = v0.v[v2];
        write_34(v8);
        long v9;
        v9 = v2 + 1l;
        bool v10;
        v10 = v9 < 5l;
        if (v10){
            const char * v11;
            v11 = "; ";
            write_25(v11);
        } else {
        }
        v2 += 1l ;
    }
    const char * v12;
    v12 = "]";
    return write_25(v12);
}
__device__ void write_77(){
    const char * v0;
    v0 = "Turn";
    return write_25(v0);
}
__device__ void write_78(static_array<unsigned char,4l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_3(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 4l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        unsigned char v8;
        v8 = v0.v[v2];
        write_34(v8);
        long v9;
        v9 = v2 + 1l;
        bool v10;
        v10 = v9 < 4l;
        if (v10){
            const char * v11;
            v11 = "; ";
            write_25(v11);
        } else {
        }
        v2 += 1l ;
    }
    const char * v12;
    v12 = "]";
    return write_25(v12);
}
__device__ void write_71(US8 v0){
    switch (v0.tag) {
        case 0: { // Flop
            static_array<unsigned char,3l> v1 = v0.v.case0.v0;
            write_72();
            const char * v2;
            v2 = "(";
            write_25(v2);
            write_73(v1);
            const char * v3;
            v3 = ")";
            return write_25(v3);
            break;
        }
        case 1: { // Preflop
            return write_74();
            break;
        }
        case 2: { // River
            static_array<unsigned char,5l> v4 = v0.v.case2.v0;
            write_75();
            const char * v5;
            v5 = "(";
            write_25(v5);
            write_76(v4);
            const char * v6;
            v6 = ")";
            return write_25(v6);
            break;
        }
        case 3: { // Turn
            static_array<unsigned char,4l> v7 = v0.v.case3.v0;
            write_77();
            const char * v8;
            v8 = "(";
            write_25(v8);
            write_78(v7);
            const char * v9;
            v9 = ")";
            return write_25(v9);
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ void write_68(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5){
    char v6;
    v6 = '{';
    write_23(v6);
    write_24();
    const char * v7;
    v7 = "min_raise";
    write_25(v7);
    const char * v8;
    v8 = " = ";
    write_25(v8);
    write_37(v0);
    const char * v9;
    v9 = "; ";
    write_25(v9);
    const char * v10;
    v10 = "pl_card";
    write_25(v10);
    write_25(v8);
    write_69(v1);
    write_25(v9);
    const char * v11;
    v11 = "pot";
    write_25(v11);
    write_25(v8);
    write_70(v2);
    write_25(v9);
    const char * v12;
    v12 = "round_turn";
    write_25(v12);
    write_25(v8);
    write_37(v3);
    write_25(v9);
    const char * v13;
    v13 = "stack";
    write_25(v13);
    write_25(v8);
    write_70(v4);
    write_25(v9);
    const char * v14;
    v14 = "street";
    write_25(v14);
    write_25(v8);
    write_71(v5);
    char v15;
    v15 = '}';
    return write_23(v15);
}
__device__ void write_79(){
    const char * v0;
    v0 = "G_Fold";
    return write_25(v0);
}
__device__ void write_80(){
    const char * v0;
    v0 = "G_Preflop";
    return write_25(v0);
}
__device__ void write_81(){
    const char * v0;
    v0 = "G_River";
    return write_25(v0);
}
__device__ void write_82(){
    const char * v0;
    v0 = "G_Round";
    return write_25(v0);
}
__device__ void write_83(){
    const char * v0;
    v0 = "G_Round'";
    return write_25(v0);
}
__device__ void write_84(long v0, static_array<static_array<unsigned char,2l>,2l> v1, static_array<long,2l> v2, long v3, static_array<long,2l> v4, US8 v5, US4 v6){
    write_68(v0, v1, v2, v3, v4, v5);
    const char * v7;
    v7 = ", ";
    write_25(v7);
    return write_40(v6);
}
__device__ void write_85(){
    const char * v0;
    v0 = "G_Showdown";
    return write_25(v0);
}
__device__ void write_86(){
    const char * v0;
    v0 = "G_Turn";
    return write_25(v0);
}
__device__ void write_66(US7 v0){
    switch (v0.tag) {
        case 0: { // G_Flop
            long v1 = v0.v.case0.v0; static_array<static_array<unsigned char,2l>,2l> v2 = v0.v.case0.v1; static_array<long,2l> v3 = v0.v.case0.v2; long v4 = v0.v.case0.v3; static_array<long,2l> v5 = v0.v.case0.v4; US8 v6 = v0.v.case0.v5;
            write_67();
            const char * v7;
            v7 = "(";
            write_25(v7);
            write_68(v1, v2, v3, v4, v5, v6);
            const char * v8;
            v8 = ")";
            return write_25(v8);
            break;
        }
        case 1: { // G_Fold
            long v9 = v0.v.case1.v0; static_array<static_array<unsigned char,2l>,2l> v10 = v0.v.case1.v1; static_array<long,2l> v11 = v0.v.case1.v2; long v12 = v0.v.case1.v3; static_array<long,2l> v13 = v0.v.case1.v4; US8 v14 = v0.v.case1.v5;
            write_79();
            const char * v15;
            v15 = "(";
            write_25(v15);
            write_68(v9, v10, v11, v12, v13, v14);
            const char * v16;
            v16 = ")";
            return write_25(v16);
            break;
        }
        case 2: { // G_Preflop
            return write_80();
            break;
        }
        case 3: { // G_River
            long v17 = v0.v.case3.v0; static_array<static_array<unsigned char,2l>,2l> v18 = v0.v.case3.v1; static_array<long,2l> v19 = v0.v.case3.v2; long v20 = v0.v.case3.v3; static_array<long,2l> v21 = v0.v.case3.v4; US8 v22 = v0.v.case3.v5;
            write_81();
            const char * v23;
            v23 = "(";
            write_25(v23);
            write_68(v17, v18, v19, v20, v21, v22);
            const char * v24;
            v24 = ")";
            return write_25(v24);
            break;
        }
        case 4: { // G_Round
            long v25 = v0.v.case4.v0; static_array<static_array<unsigned char,2l>,2l> v26 = v0.v.case4.v1; static_array<long,2l> v27 = v0.v.case4.v2; long v28 = v0.v.case4.v3; static_array<long,2l> v29 = v0.v.case4.v4; US8 v30 = v0.v.case4.v5;
            write_82();
            const char * v31;
            v31 = "(";
            write_25(v31);
            write_68(v25, v26, v27, v28, v29, v30);
            const char * v32;
            v32 = ")";
            return write_25(v32);
            break;
        }
        case 5: { // G_Round'
            long v33 = v0.v.case5.v0; static_array<static_array<unsigned char,2l>,2l> v34 = v0.v.case5.v1; static_array<long,2l> v35 = v0.v.case5.v2; long v36 = v0.v.case5.v3; static_array<long,2l> v37 = v0.v.case5.v4; US8 v38 = v0.v.case5.v5; US4 v39 = v0.v.case5.v6;
            write_83();
            const char * v40;
            v40 = "(";
            write_25(v40);
            write_84(v33, v34, v35, v36, v37, v38, v39);
            const char * v41;
            v41 = ")";
            return write_25(v41);
            break;
        }
        case 6: { // G_Showdown
            long v42 = v0.v.case6.v0; static_array<static_array<unsigned char,2l>,2l> v43 = v0.v.case6.v1; static_array<long,2l> v44 = v0.v.case6.v2; long v45 = v0.v.case6.v3; static_array<long,2l> v46 = v0.v.case6.v4; US8 v47 = v0.v.case6.v5;
            write_85();
            const char * v48;
            v48 = "(";
            write_25(v48);
            write_68(v42, v43, v44, v45, v46, v47);
            const char * v49;
            v49 = ")";
            return write_25(v49);
            break;
        }
        case 7: { // G_Turn
            long v50 = v0.v.case7.v0; static_array<static_array<unsigned char,2l>,2l> v51 = v0.v.case7.v1; static_array<long,2l> v52 = v0.v.case7.v2; long v53 = v0.v.case7.v3; static_array<long,2l> v54 = v0.v.case7.v4; US8 v55 = v0.v.case7.v5;
            write_86();
            const char * v56;
            v56 = "(";
            write_25(v56);
            write_68(v50, v51, v52, v53, v54, v55);
            const char * v57;
            v57 = ")";
            return write_25(v57);
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ void write_63(US6 v0){
    switch (v0.tag) {
        case 0: { // None
            return write_64();
            break;
        }
        case 1: { // Some
            US7 v1 = v0.v.case1.v0;
            write_65();
            const char * v2;
            v2 = "(";
            write_25(v2);
            write_66(v1);
            const char * v3;
            v3 = ")";
            return write_25(v3);
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ void write_89(){
    const char * v0;
    v0 = "Computer";
    return write_25(v0);
}
__device__ void write_90(){
    const char * v0;
    v0 = "Human";
    return write_25(v0);
}
__device__ void write_88(US2 v0){
    switch (v0.tag) {
        case 0: { // Computer
            return write_89();
            break;
        }
        case 1: { // Human
            return write_90();
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ void write_87(static_array<US2,2l> v0){
    const char * v1;
    v1 = "[";
    write_25(v1);
    long v2;
    v2 = 0l;
    while (while_method_4(v2)){
        bool v4;
        v4 = 0l <= v2;
        bool v6;
        if (v4){
            bool v5;
            v5 = v2 < 2l;
            v6 = v5;
        } else {
            v6 = false;
        }
        bool v7;
        v7 = v6 == false;
        if (v7){
            assert("The read index needs to be in range for the static array." && v6);
        } else {
        }
        US2 v8;
        v8 = v0.v[v2];
        write_88(v8);
        long v9;
        v9 = v2 + 1l;
        bool v10;
        v10 = v9 < 2l;
        if (v10){
            const char * v11;
            v11 = "; ";
            write_25(v11);
        } else {
        }
        v2 += 1l ;
    }
    const char * v12;
    v12 = "]";
    return write_25(v12);
}
__device__ void write_92(){
    const char * v0;
    v0 = "GameNotStarted";
    return write_25(v0);
}
__device__ void write_93(){
    const char * v0;
    v0 = "GameOver";
    return write_25(v0);
}
__device__ void write_94(){
    const char * v0;
    v0 = "WaitingForActionFromPlayerId";
    return write_25(v0);
}
__device__ void write_91(US9 v0){
    switch (v0.tag) {
        case 0: { // GameNotStarted
            return write_92();
            break;
        }
        case 1: { // GameOver
            long v1 = v0.v.case1.v0; static_array<static_array<unsigned char,2l>,2l> v2 = v0.v.case1.v1; static_array<long,2l> v3 = v0.v.case1.v2; long v4 = v0.v.case1.v3; static_array<long,2l> v5 = v0.v.case1.v4; US8 v6 = v0.v.case1.v5;
            write_93();
            const char * v7;
            v7 = "(";
            write_25(v7);
            write_68(v1, v2, v3, v4, v5, v6);
            const char * v8;
            v8 = ")";
            return write_25(v8);
            break;
        }
        case 2: { // WaitingForActionFromPlayerId
            long v9 = v0.v.case2.v0; static_array<static_array<unsigned char,2l>,2l> v10 = v0.v.case2.v1; static_array<long,2l> v11 = v0.v.case2.v2; long v12 = v0.v.case2.v3; static_array<long,2l> v13 = v0.v.case2.v4; US8 v14 = v0.v.case2.v5;
            write_94();
            const char * v15;
            v15 = "(";
            write_25(v15);
            write_68(v9, v10, v11, v12, v13, v14);
            const char * v16;
            v16 = ")";
            return write_25(v16);
            break;
        }
        default: {
            assert("Invalid tag." && false);
        }
    }
}
__device__ void write_62(US6 v0, static_array<US2,2l> v1, US9 v2){
    char v3;
    v3 = '{';
    write_23(v3);
    write_24();
    const char * v4;
    v4 = "game";
    write_25(v4);
    const char * v5;
    v5 = " = ";
    write_25(v5);
    write_63(v0);
    const char * v6;
    v6 = "; ";
    write_25(v6);
    const char * v7;
    v7 = "pl_type";
    write_25(v7);
    write_25(v5);
    write_87(v1);
    write_25(v6);
    const char * v8;
    v8 = "ui_game_state";
    write_25(v8);
    write_25(v5);
    write_91(v2);
    char v9;
    v9 = '}';
    return write_23(v9);
}
__device__ void write_26(unsigned long long v0, static_array_list<US3,128l,long> v1, US6 v2, static_array<US2,2l> v3, US9 v4){
    char v5;
    v5 = '{';
    write_23(v5);
    write_24();
    const char * v6;
    v6 = "large";
    write_25(v6);
    const char * v7;
    v7 = " = ";
    write_25(v7);
    write_27(v0, v1);
    const char * v8;
    v8 = "; ";
    write_25(v8);
    const char * v9;
    v9 = "small";
    write_25(v9);
    write_25(v7);
    write_62(v2, v3, v4);
    char v10;
    v10 = '}';
    return write_23(v10);
}
__device__ void write_22(unsigned long long v0, static_array_list<US3,128l,long> v1, US6 v2, static_array<US2,2l> v3, US9 v4){
    char v5;
    v5 = '{';
    write_23(v5);
    write_24();
    const char * v6;
    v6 = "game_state";
    write_25(v6);
    const char * v7;
    v7 = " = ";
    write_25(v7);
    write_26(v0, v1, v2, v3, v4);
    char v8;
    v8 = '}';
    return write_23(v8);
}
extern "C" __global__ void entry0() {
    long v0;
    v0 = threadIdx.x;
    long v1;
    v1 = blockIdx.x;
    long v2;
    v2 = v1 * 512l;
    long v3;
    v3 = v0 + v2;
    bool v4;
    v4 = v3 == 0l;
    if (v4){
        long v5;
        v5 = clock64() % 52;
        US0 v6; US1 v7;
        Tuple0 tmp0 = card_untag_0(v5);
        v6 = tmp0.v0; v7 = tmp0.v1;
        long v8;
        v8 = card_tag_3(v7, v6);
        static_array<US2,2l> v9;
        US2 v10;
        v10 = US2_0();
        v9.v[0l] = v10;
        US2 v11;
        v11 = US2_1();
        v9.v[1l] = v11;
        static_array_list<US3,128l,long> v12;
        v12.length = 0;
        US5 v13;
        v13 = US5_2();
        unsigned long long v14;
        v14 = 4503599627370495ull;
        US6 v15;
        v15 = US6_0();
        US9 v16;
        v16 = US9_0();
        unsigned long long & v17 = v14;
        static_array_list<US3,128l,long> & v18 = v12;
        unsigned long long v19;
        v19 = clock64();
        long v20;
        v20 = threadIdx.x;
        long v21;
        v21 = blockIdx.x;
        long v22;
        v22 = v21 * 512l;
        long v23;
        v23 = v20 + v22;
        unsigned long long v24;
        v24 = (unsigned long long)v23;
        curandStatePhilox4_32_10_t v25;
        curand_init(v19,v24,0ull,&v25);
        US6 v67; static_array<US2,2l> v68; US9 v69;
        switch (v13.tag) {
            case 0: { // ActionSelected
                US4 v37 = v13.v.case0.v0;
                switch (v15.tag) {
                    case 0: { // None
                        v67 = v15; v68 = v9; v69 = v16;
                        break;
                    }
                    case 1: { // Some
                        US7 v38 = v15.v.case1.v0;
                        switch (v38.tag) {
                            case 4: { // G_Round
                                long v39 = v38.v.case4.v0; static_array<static_array<unsigned char,2l>,2l> v40 = v38.v.case4.v1; static_array<long,2l> v41 = v38.v.case4.v2; long v42 = v38.v.case4.v3; static_array<long,2l> v43 = v38.v.case4.v4; US8 v44 = v38.v.case4.v5;
                                US7 v45;
                                v45 = US7_5(v39, v40, v41, v42, v43, v44, v37);
                                Tuple2 tmp51 = play_loop_6(v15, v9, v16, v17, v18, v25, v45);
                                v67 = tmp51.v0; v68 = tmp51.v1; v69 = tmp51.v2;
                                break;
                            }
                            default: {
                                printf("%s\n", "Unexpected game node in ActionSelected.");
                                asm("exit;");
                            }
                        }
                        break;
                    }
                    default: {
                        assert("Invalid tag." && false);
                    }
                }
                break;
            }
            case 1: { // PlayerChanged
                static_array<US2,2l> v36 = v13.v.case1.v0;
                v67 = v15; v68 = v36; v69 = v16;
                break;
            }
            case 2: { // StartGame
                static_array<US2,2l> v26;
                US2 v27;
                v27 = US2_0();
                v26.v[0l] = v27;
                US2 v28;
                v28 = US2_1();
                v26.v[1l] = v28;
                static_array_list<US3,128l,long> v29;
                v29.length = 0;
                v17 = 4503599627370495ull;
                v18 = v29;
                US6 v30;
                v30 = US6_0();
                US9 v31;
                v31 = US9_0();
                US7 v32;
                v32 = US7_2();
                Tuple2 tmp52 = play_loop_6(v30, v26, v31, v17, v18, v25, v32);
                v67 = tmp52.v0; v68 = tmp52.v1; v69 = tmp52.v2;
                break;
            }
            default: {
                assert("Invalid tag." && false);
            }
        }
        write_22(v14, v12, v67, v68, v69);
        printf("\n");
        return ;
    } else {
        return ;
    }
}
"""
class static_array(list):
    def __init__(self, length):
        for _ in range(length):
            self.append(None)

class static_array_list(static_array):
    def __init__(self, length):
        super().__init__(length)
        self.length = 0
import cupy as cp
from dataclasses import dataclass
from typing import NamedTuple, Union, Callable, Tuple
i8 = i16 = i32 = i64 = u8 = u16 = u32 = u64 = int; f32 = f64 = float; char = string = str

import time
options = []
options.append('--diag-suppress=550,20012')
options.append('--dopt=on')
options.append('--restrict')
options.append('--maxrregcount=128')
raw_module = cp.RawModule(code=kernel, backend='nvrtc', enable_cooperative_groups=True, options=tuple(options))
def method0(v0 : string) -> None:
    print(v0, end="")
    del v0
    return 
def method1(v0 : f64) -> None:
    print("{:.6f}".format(v0), end="")
    del v0
    return 
def main():
    v0 = "Going to run the kernel."
    method0(v0)
    del v0
    print()
    v1 = time.perf_counter()
    v2 = 0
    v3 = raw_module.get_function(f"entry{v2}")
    del v2
    v3.max_dynamic_shared_size_bytes = 0 
    v3((1,),(512,),(),shared_mem=0)
    del v3
    v4 = time.perf_counter()
    v5 = "The time it took to run the kernel (in seconds) is: "
    method0(v5)
    del v5
    v6 = v4 - v1
    del v1, v4
    method1(v6)
    del v6
    print()
    return 

if __name__ == '__main__': print(main())
