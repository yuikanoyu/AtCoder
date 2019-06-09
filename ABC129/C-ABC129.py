from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

ans = 0
N, M = map(int,input().split())
a = []
for _ in range(M):
    a.append(int(input()))

print(N,M,a)

a = N
b = 0
total = 0

while( a >= b ):
    total += cmb(a,b)
    a -= 1
    b += 1

print(total)

# 突破できず



