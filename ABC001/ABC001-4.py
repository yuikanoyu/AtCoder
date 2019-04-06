rain_list = []
N = int(input())
for i in range(N):
    rain_list.append(list(map(str,input().split('-'))))

for i in range(N):
    for j in range(2):
        fix_value = int(rain_list[i][j][2:]) % 5
        if j == 1 and fix_value != 0:
            fix_value = -(5 - fix_value)
        rain_list[i][j] = int(rain_list[i][j]) - fix_value

print(rain_list)


