N, K = map(int,input().split())
a = list(map(int,input().split()))

x = 0
cnt = 0

for i in range(N):
    x = a[i]

    if x >= K:
        cnt += 1

    for j in range(N-i-1):
        x += a[1+i+j]
        if x >= K:
            cnt += 1

    
print(cnt)