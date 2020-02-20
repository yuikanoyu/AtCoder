N, L = map(int,input().split())

p = []
pi = []
pi_s = []


for i in range(L,L+N):
    p.append(i)

all_t = sum(p)

for i in range(N):
    pi.append(all_t - p[i])
    pi_s.append(abs(all_t - pi[i]))

# print(p, pi,pi_s)
min_abs = pi_s[0]
ans = 0

for i in range(1,N):
    if min_abs > pi_s[i]:
        min_abs = pi_s[i]
        ans = i

# print(ans,pi[ans],pi_s[ans])

print(pi[ans])