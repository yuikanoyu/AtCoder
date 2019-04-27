A,B,T = map(int,input().split())
time = 0
biscuit = 0
end = False

while not end:
    time += A
    if  time <= T:
        biscuit += B
    else:
        end = True

print(biscuit)
