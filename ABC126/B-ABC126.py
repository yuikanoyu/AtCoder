S = input()
S_1 = int(S[:2])
S_2 = int(S[2:])

YM_Flag = False
MY_Flag = False

if S_1 >= 1 and S_1 <= 12:
    MY_Flag = True

if S_2 >= 1 and S_2 <= 12:
    YM_Flag = True

if MY_Flag and YM_Flag:
    print('AMBIGUOUS')
elif MY_Flag:
    print('MMYY')
elif YM_Flag:
    print('YYMM')
else:
    print('NA')

