N = int(input())
S = list(input())

sharp_num =[]
dot_num = []

init_search = S[0]
search = init_search

count = 0

for c in S:
    print('c:{},se:{}'.format(c,search))
    if search == '#':
        if c == search:
            count += 1
        else:
            sharp_num.append(count)
            count = 1
            search = '.'
    else:
        if c == search:
            count += 1
        else:
            dot_num.append(count)
            count = 1
            search = '#'
if init_search == '#':
    sharp_num.append(count)
else:
    dot_num.append(count)

if len(sharp_num) > len(dot_num):
    dot_num.append(0)
elif len(sharp_num) < len(dot_num):
    sharp_num.append(0)
else:
    pass


total = 0
for i in range(len(sharp_num)):
    total += min(sharp_num[i],dot_num[i])

print(total)