def digit_sum(num):
    total_num = 0
    while num > 0:
        total_num += num % 10
        num //= 10
    return total_num

num_list= []
n, a, b = map(int, input().split())

for i in range(1,n+1):
    num = digit_sum(i)
    if num >= a and num <= b:
        num_list.append(i)

print(sum(num_list))

