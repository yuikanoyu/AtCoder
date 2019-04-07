time = 0
order_list = []

for i in range(5):
    order_list.append(int(input()))

for i in range(4):
    next_order = order_list[i+1] % 10 if order_list[i+1] % 10 != 0 else 10
    if order_list[i] % 10 < next_order:
        buff = order_list[i]
        order_list[i] = order_list[i+1]
        order_list[i+1] = buff

for i in range(5):
    wait = 10 - order_list[i] % 10
    if wait == 10 or i == 4:
        wait = 0
    time += order_list[i] + wait

print(time)