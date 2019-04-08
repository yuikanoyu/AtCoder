def trans(i):
	if nums[i] <= 0:
		return
	val = nums[i] - caps[i]
	if val <= 0:
		nums[i+1] += nums[i] 
		nums[i] = 0
	else:
		nums[i+1] += caps[i] 
		nums[i] -= caps[i]

time = 0
nums = [0]*6
N = nums[0] = int(input())
caps = []
for i in range(5):
	caps.append(int(input()))
print('{}-{}'.format(nums,caps))

while nums[5] != N:
	time += 1
	for i in range(4,-1,-1):
		trans(i)
	print('num:{}-time:{}'.format(nums,time))
