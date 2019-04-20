n,m = map(int,input().split())
store = []
can_num = m
cost = 0

for i in range(n):
    store.append(tuple(map(int,input().split())))

store.sort()

while can_num > 0:
    lowest_store = store.pop(0)
    buy_num = lowest_store[1] if lowest_store[1] < can_num else can_num
    cost += buy_num * lowest_store[0]
    can_num -= buy_num

print(cost)

