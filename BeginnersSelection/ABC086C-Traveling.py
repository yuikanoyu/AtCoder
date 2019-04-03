pos_x = pos_y = 0
n = int(input())
plans = []
time = 0
result = 'Yes'

for i in range(n):
	plans.append(list(map(int, input().split(' '))))

for plan in plans:
	time = plan[0] - time
	for i in range(time):
		if abs(pos_x - plan[1]) > abs(pos_y - plan[2]):
            pos_x += 1 if pos_x <= plan[1] else -1
#			if pos_x < plan[1]:
#				pos_x += 1
#			else:
#				pos_x -= 1
        else:
            pos_y += 1 if pos_y <= plan[2] else -1
#			if pos_y < plan[2]:
#				pos_y += 1
#			else:
#				pos_y -= 1
		#print('x:{}, y:{}'.format(pos_x,pos_y))
	if pos_x != plan[1] or pos_y != plan[2]:
		result = 'No'
		break
print(result)