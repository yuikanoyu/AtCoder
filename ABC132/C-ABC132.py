N = int(input())

d = list(map(int, input().split()))

d.sort()

d_ma = d[(N//2)]
d_mi = d[(N//2)-1]

cnt = 0
for i in range(d_mi,d_ma):
    cnt += 1

print( cnt )