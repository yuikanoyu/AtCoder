N = int(input())
W = list(map(int,input().split()))

Z = []

rX = []
rY = []
for i in range(N):
    rX.append(0)
    rY.append(0)
    Z.append(0)

rX[0] = W[0]
rY[0] = W[N-1]

for i in range(1,N):
    rX[i] = rX[i-1] + W[i]
    rY[i] = rY[i-1] + W[N-1-i]



rX.insert(0,0)
rY.reverse()
rY.append(0)
Z.append(0)

for i in range(N+1):
    Z[i] = abs(rX[i] - rY[i])

print(min(Z))