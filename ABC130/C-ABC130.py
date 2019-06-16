W, H, x, y = map(int,input().split())

a = W*H/2
b = 0

if W/2 == x and H/2 == y:
    b = 1

print(a,b)