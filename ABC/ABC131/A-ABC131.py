S = list(input())

flag = True

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        flag = False
        break



"""
for i in range(len(S)):
    for j in range(i+1,len(S)):
        if S[i] == S[j]:
            flag = False
            break
    else:
        continue
    break
    
"""
if flag:
    print('Good')
else:
    print('Bad')