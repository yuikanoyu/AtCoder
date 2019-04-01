def divided(num):
    return num / 2

def can_divided(num):
    return num % 2 == 0

_n = int(input())
num_list = list(map(int, input().split()))
run_count = 0
end_flag = False

can_list = list(map(can_divided, num_list))
while not False in can_list:
    run_count += 1
    num_list = list(map(divided, num_list))
    can_list = list(map(can_divided, num_list))
    # print(num_list)

print(run_count)

