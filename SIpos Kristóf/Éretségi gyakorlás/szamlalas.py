össz_adatok=[36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]

print('2.Feladat')
adatok=[]
for i in range(len(össz_adatok)):
    if össz_adatok[i] == -1:
        össz_adatok[i]=0
    adatok.append(össz_adatok[i])
össz=sum(adatok)
print(f'Összesen {össz} kerékpárost számoltak.\n')
print('3.Feladat')
hat_óra=[]
hét_óra=[]
nyolc_óra=[]
kilenc_óra=[]
for i in range(len(adatok)):
    if i <= 3:
        hat_óra.append(adatok[i])
    elif i <=7 and i >3:
        hét_óra.append(adatok[i])
    elif i <=11 and i >7:
        nyolc_óra.append(adatok[i])
    elif i <=15 and i >11:
        kilenc_óra.append(adatok[i])
print(f'Óránkénti mérések:\n 6 órától {sum(hat_óra)} kerékpáros\n 7 órától {sum(hét_óra)} kerékpáros\n 8 órától {sum(nyolc_óra)} kerékpáros\n 9 órától {sum(kilenc_óra)} kerékpáros\n')
print('4.Feladat')
óra=6
perc=0
legtöbb_biciklis=0
for i in range(len(adatok)):
    if adatok[i]> legtöbb_biciklis:
        legtöbb_biciklis=adatok[i]

for i in range(len(adatok)):
    if adatok[i] == legtöbb_biciklis:
        perc +=15
        break
    elif perc ==45:
        perc=0
        óra+=1
    elif i > i-1:
        perc+=15
print(f'Az áthaladók maximális száma: {legtöbb_biciklis}; a rögzítés időpontja: {óra}:{perc}.')


