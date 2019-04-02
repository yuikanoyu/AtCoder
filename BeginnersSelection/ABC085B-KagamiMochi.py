mochi_list = []
n = int(input())
for i in range(n):
    mochi_list.append(input())
    print('i{}'.format(i))

unique_mochi_count=len(list((set(mochi_list))))
print(unique_mochi_count)