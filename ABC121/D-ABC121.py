a,b = map(int,input().split())

if a % 2 != 0:
    st = a
    if b % 2 != 0:
        ed = 0
        bl = (b-(a+0))//2
    else:
        ed = b
        bl = (b-(a+1))//2
else:
    st = 0
    if b % 2 != 0:
        ed = 0
        bl = (b-(a-1))//2
    else:
        ed = b
        bl = (b-(a-0))//2

print(st^ed^(1 if bl%2!=0 else 0))

#print('a:{},st:{},b:{},ed{},bl:{}'.format(a,st,b,ed,bl))

