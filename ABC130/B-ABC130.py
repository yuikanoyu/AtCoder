N, X = map(int,input().split())
L = list(map(int,input().split()))

cnt = 0
total = 0

for i in range(N):
    if total <= X:
        cnt += 1
        total += L[i]
    else:
        break
else:
    if total <= X:
        cnt += 1


print(cnt)






"""
i = 0

while total <= X:
    cnt += 1
    total += L[i]
    i += 1
    if i >= N:
        cnt = N + 1
        break
print(cnt)
"""
