import random
szelvény=[]
for i in range(1,5):
    szám_1=random.randint(1,90)
    szelvény.append(szám_1)
    szám_2=random.randint(1,90)
    if szám_2 in szelvény:
        break
    else:
        szelvény.append(szám_2)
    szám_3=random.randint(1,90)
    if szám_3 in szelvény:
        break
    else:
        szelvény.append(szám_3)
    szám_4=random.randint(1,90)
    if szám_4 in szelvény:
        break
    else:
        szelvény.append(szám_4)
    szám_5=random.randint(1,90)
    if szám_5 in szelvény:
        break
    else:
        szelvény.append(szám_5)




