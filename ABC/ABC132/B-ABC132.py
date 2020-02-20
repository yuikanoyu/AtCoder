n = int(input())
p = list(map(int,input().split()))
cnt = 0

for i in range(1,n-1):
    x = [ p[i-1], p[i], p[i+1] ]
    x.sort()
    if x[1] == p[i]:
        cnt +=1

print(cnt)