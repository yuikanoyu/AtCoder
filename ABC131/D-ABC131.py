N = int(input())
X = []
for _ in range(N):
    buffX = list(map(int, input().split()))
    X.append(buffX)

X.sort(key=lambda x: x[1])

result = True
time = 0
for i in range(N):
    time += X[i][0]
    if time > X[i][1]:
        result = False
        break

print( 'Yes' if result else 'No' )
