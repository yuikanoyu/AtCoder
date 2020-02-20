'''
n,q = map(int,input().split())
s = input()
for _ in range(q):
    l,r = map(int,input().split())
    print(s[l-1:r].count('AC'))
'''
n,q = map(int,input().split())
s = input()
t = [0]*(n+1)
for i in range(n):
    t[i+1] = t[i] + (1 if s[i:i+2] == 'AC' else 0)
# print(t)
for i in range(q):
    l,r = map(int,input().split())
    print(t[r-1]-t[l-1])