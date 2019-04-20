N,M,C = map(int,input().split())
B = tuple(map(int,input().split()))
count = 0
for i in range(N):
    tmp = 0
    A = tuple(map(int,input().split()))
    for j in range(M):
        tmp += A[j]*B[j]
    if tmp + C > 0:
        count+=1
print(count)
