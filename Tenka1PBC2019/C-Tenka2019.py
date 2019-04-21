N = int(input())
S = input()
dot_count = S.count('.')
ans = dot_count

for i in range(N):
    dot_count += 1 if S[i] == '#' else -1
    ans = min(dot_count,ans)

print(ans)