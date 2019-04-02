mochi_list = []
n = int(input())
for i in range(n):
    mochi_list.append(input())

print(len(list((set(mochi_list)))))