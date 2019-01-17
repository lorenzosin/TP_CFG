/* IPET system */
max: 2 e4_5_bsort_return + 5 e2_4_bsort_return + 5 e3_4_bsort_return + 9 e2_3_bsort_return + 4 e1_2_bsort_return + 4 e4_2_bsort_return + 7 e0_1_bsort_return;
-99 e1_2_bsort_return + 1 e4_2_bsort_return <= 0;	/* 0-execution for total loop constraint for BB2/bsort_return*/
1 e4_2_bsort_return <= 99;	/* total loop constraint for BB2/bsort_return*/
-99 e1_2_bsort_return + 1 e4_2_bsort_return <= 0;	/* loop constraint on BB2/bsort_return*/
1 x0_bsort_return = 1;	/* program entry constraint*/
-1 e5_6_bsort_return + 1 x6_bsort_return = 0;	/* structural input constraint of BB6/bsort_return*/
-1 e5_6_bsort_return + 1 x5_bsort_return = 0;	/* structural output constraint of BB5/bsort_return*/
-1 e4_5_bsort_return + 1 x5_bsort_return = 0;	/* structural input constraint of BB5/bsort_return*/
-1 e4_2_bsort_return + -1 e4_5_bsort_return + 1 x4_bsort_return = 0;	/* structural output constraint of BB4/bsort_return*/
-1 e2_4_bsort_return + -1 e3_4_bsort_return + 1 x4_bsort_return = 0;	/* structural input constraint of BB4/bsort_return*/
-1 e3_4_bsort_return + 1 x3_bsort_return = 0;	/* structural output constraint of BB3/bsort_return*/
-1 e2_3_bsort_return + 1 x3_bsort_return = 0;	/* structural input constraint of BB3/bsort_return*/
-1 e2_4_bsort_return + -1 e2_3_bsort_return + 1 x2_bsort_return = 0;	/* structural output constraint of BB2/bsort_return*/
-1 e1_2_bsort_return + -1 e4_2_bsort_return + 1 x2_bsort_return = 0;	/* structural input constraint of BB2/bsort_return*/
-1 e1_2_bsort_return + 1 x1_bsort_return = 0;	/* structural output constraint of BB1/bsort_return*/
-1 e0_1_bsort_return + 1 x1_bsort_return = 0;	/* structural input constraint of BB1/bsort_return*/
-1 e0_1_bsort_return + 1 x0_bsort_return = 0;	/* structural output constraint of BB0/bsort_return*/
int x0_bsort_return;
int e5_6_bsort_return;
int e3_4_bsort_return;
int x6_bsort_return;
int e0_1_bsort_return;
int x5_bsort_return;
int x2_bsort_return;
int x1_bsort_return;
int e4_2_bsort_return;
int e2_3_bsort_return;
int x4_bsort_return;
int e1_2_bsort_return;
int x3_bsort_return;
int e4_5_bsort_return;
int e2_4_bsort_return;
