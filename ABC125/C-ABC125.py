def GCD(a, b):
    while a % b != 0:
        r = a % b
        a, b = b, r
    return b

ans = 0
N = int(input())
A = tuple(map(int,input().split()))

A2 = tuple(set(A))

if len(A2) <= 2:
    A2 = (A2[0],A2[0])

for S in range(len(A2)):
    Af = 0
    for i in range(len(A2)):
        if S != i:
            Af = GCD(Af,A[i])
    ans = max(ans,Af)

print(ans)
print(A2)