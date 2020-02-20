N , K = map(int,input().split())
x = 0

for i in range(1,N+1):
    y = 0
    while(i < K):
        i *= 2
        y += 1
    x += (1/2) ** y

print((1/N) * x)

