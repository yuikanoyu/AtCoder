a,b = map(int, input().split())
coin = 0

if a == b:
    coin = a*2
else:
    if a > b:
        coin = a*2-1
    else:
        coin = b*2-1

print (coin)