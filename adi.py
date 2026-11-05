import random as r
n = 4
otp = ''
for i in range(n):
    dig = r.randint(0,9)
    sdig = str(dig)
    otp = otp + sdig
print(otp)
