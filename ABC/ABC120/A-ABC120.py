A,B,C = map(int,input().split())
cost = B
ans = 0

for _ in range(C):
    if cost - A >= 0:
        cost -= A
        ans +=1
    else:
        break

print(ans)