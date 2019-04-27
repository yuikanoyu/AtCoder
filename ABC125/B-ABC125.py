N = int(input())
V = tuple(map(int,list(input().split())))
C = tuple(map(int,list(input().split())))

tmp_c = 0
tmp_v = 0

for i in range(N):
    if V[i] > C[i]:
        tmp_v += V[i]
        tmp_c += C[i]

print(tmp_v-tmp_c)