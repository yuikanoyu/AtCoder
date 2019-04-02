def digit_sum(num):
    total_num = 0
    while num > 0:
        total_num += num % 10
        num //= 10
    return total_num

def digit_sum2(num):
    total = 0
    for digit in str(num):
        print('num:{},digit:{}'.format(num,digit))
        total += int(digit)
    return total

num_list= []
n, a, b = map(int, input().split())

for i in range(1,n+1):
    num = digit_sum2(i)
    if num >= a and num <= b:
        num_list.append(i)

print(sum(num_list))


