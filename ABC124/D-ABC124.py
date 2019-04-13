n,k = map(int,input().split())
s = tuple(input())
tmp = 0
most_tmp = 0

for i in range(n):
    if s[i] == '0':
        tmp += 1
    else:
        tmp = 0

    if most_tmp < tmp:
        most_tmp = tmp
    print('{}-{}'.format(most_tmp,tmp))

print(most_tmp)
