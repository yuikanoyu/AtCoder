S = input()

s1 = S[0]
s2 = S[1]
s3 = S[2]
s4 = S[3]

if s1 == s2 and s1 == s3 and s1 == s4:
    print('No')
elif s1 == s2 and s3 == s4:
    print('Yes')
elif s1 == s3 and s2 == s4:
    print('Yes')
elif s1 == s4 and s2 == s3:
    print('Yes')
else:
    print('No')