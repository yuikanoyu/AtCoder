N, K = map(int,input().split())
a = list(map(int,input().split()))

total = 0
ans = 0
r = 0

for l in range(N):
    while total < K:

        if r >= N:
            break

        else:
            total += a[r]
            r += 1

    if total < K:
        break

    ans += N-r+1
    total -= a[l]

print(ans)