n,k = map(int,input().split())
s = tuple(input())

now = 1 # 今見ている数
cnt = 0 # nowがいくつ並んでいるか
nums =[]

for i in range(n):
    if s[i] == str(now):
        cnt += 1
    else:
        nums.append(cnt)
        now ^= 1    #見る値の切り替え
        cnt = 1

if cnt != 0:
    nums.append(cnt)

if len(nums) % 2 == 0:
    nums.append(0)

add = 2 * k + 1
ans = 0
left = 0
right = 0
tmp = 0

for i in range(len(nums))[::2]:
    next_left = i
    next_right = min(i+add, len(nums))
    # 尺取法
    while next_left > left:
        tmp -= nums[left]
        left += 1
    while next_right > right:
        tmp += nums[right]
        right += 1
    ans = max(tmp,ans)

print(ans)
