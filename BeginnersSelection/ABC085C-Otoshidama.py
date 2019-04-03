N, Y = map(int, input().split(' '))
x = y = z = -1
for i in reversed(range(N+1)):
	for j in reversed(range(N+1-i)):
		k = N - i - j
		if Y == i * 10000 + j * 5000 + k * 1000:
			x,y,z = i,j,k
			break
	else:
		continue
	break

print('{} {} {}'.format(x,y,z))
