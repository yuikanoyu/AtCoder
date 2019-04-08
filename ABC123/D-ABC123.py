great_list = []
x,y,z,k = map(int,input().split(' '))
a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))
c = list(map(int,input().split(' ')))

a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

for i in range(min(k,len(a)))[:k]:
	for j in range(min(k // (i+1),len(b)))[:k]:
		for l in range(min(k // ((i+1) * (j+1)),len(c)))[:k]:
			great_list.append(a[i] + b[j] + c[l])

great_list.sort(reverse=True)
for i in great_list[:k]:
    print(i)
