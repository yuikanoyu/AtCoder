s = tuple(input())
n = len(s)
count_0start = 0
count_1start = 0

for i in range(n)[::2]:
    if s[i] == '0':
        count_0start += 1
    else:
        count_1start += 1
    
for i in range(n)[1::2]:
    if s[i] == '1':
        count_0start +=1
    else:
        count_1start += 1

print(count_0start if count_0start < count_1start else count_1start)
