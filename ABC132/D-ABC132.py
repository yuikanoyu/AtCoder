# 1. 赤ボールを並べる
# 2. 青ボールを置く位置のパターン数を求める
#    置ける場所は赤ボールの両端とボールの間

# 3. 青ボールの個数をどのように分けるかのパターン数を求める
#    青ボールの個数を分ける線の数を求める

# from scipy.special import comb # atcoderでエラーになる

from operator import mul
from functools import reduce
def cmb(n, r):
    if r > n:
        return 0
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under

N, K = map(int, input().split())

r_cnt = N - K
b_cnt = K

for i in range(1, K+1):
    print(( cmb( r_cnt+1, i ) * cmb( b_cnt-1, i-1 )) % (10**9+7))
    # print(( comb( r_cnt+1, i, exact = True ) * comb( b_cnt-1, i-1, exact = True )) % (10**9+7))