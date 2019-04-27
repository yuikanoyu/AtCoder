def GCD(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0:
        return b
    elif b == 0:
        return a

    while a % b != 0:
        r = a % b
        a, b = b, r
    return b

ans = 0
N = int(input())
A = tuple(map(int,input().split()))

X = [0]*N
Y = [0]*N

for i in range(1,N):
    X[i] = GCD(X[i-1],A[i-1])
for i in range(N-1)[::-1]:
    Y[i] = GCD(Y[i+1],A[i+1])

for i in range(N):
    ans = max(ans,GCD(X[i],Y[i]))

print(ans)
