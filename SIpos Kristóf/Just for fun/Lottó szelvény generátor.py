import random
szelvény=[]
while len(szelvény) != 5:
    szám=random.randint(1,90)
    if szám in szelvény:
        break
    else:
        szelvény.append(szám)
print(szelvény)
