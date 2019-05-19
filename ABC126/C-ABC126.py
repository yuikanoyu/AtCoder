N , K = map(int,input().split())


times = 0
total = 1
while total < K:
    total *= 2
    times += 1

bo = N * (2 ** times)    


#num = 2**(times-1)-1
num = 0
num2 = 1
for i in range(times-1):
    num += num2
    num2 *= 2

#print(times)
#print(num)
#print(bo)

print(num/bo)

