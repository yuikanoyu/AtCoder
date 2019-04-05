km = int(input()) / 1000

vv = 0

if km < 0.1:
    vv = 0
elif km <= 5:
    vv = km * 10
elif km < 6:
    pass
elif km <= 30:
    vv = km + 50
elif km < 35:
    pass
elif km <= 70:
    vv = (km - 30) / 5 + 80
else:
    vv = 89

print(str(int(vv)).zfill(2))