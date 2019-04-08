import math

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count = math.ceil(n/min(a,b,c,d,e))
print(count+len('ABCDE')-1)