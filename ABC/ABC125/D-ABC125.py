N = int(input())
A = list(map(int,input().split()))
total = 0
X = [0]*N
flag = False
subcount = 0

for i in range(N):
    if A[i] == 0:
        flag = True
    elif A[i] < 0:
        subcount += 1
    X[i] = abs(A[i])
    total += X[i]

if flag or (subcount % 2 == 0):
    print(total)
else:
    print(total-2*min(X))
