import random
dobasok_szama=random.randint(100,120)
dobasok=[]
for i in range(dobasok_szama):
    dobott_szam=random.randint(1,6)
    dobasok.append(dobott_szam)


#Feladat 1
print(dobasok_szama)

#Feladat 2
for i in range(dobasok_szama):                      # ez így nem jó
    osszeg=(dobott_szam[i-1]+dobott_szam[i])
print(osszeg)

#Feladat 3
atlag=osszeg/dobasok_szama
print(f'A dobasok átlaga az {atlag}.')              # ez jó lenne, ha az összeg jó lenne
#Feladat 4
for i in range(dobasok_szama):                      # ez így tökéletes
    if dobasok[i]==6:
        print('Van benne 6-os.')
        break
else:
    print('nincs benne 6-os.')

#Feladat 5
szam_index=[]
szam=int(input('Írj 1 és 6 között egy számot: '))
for i in range(dobasok_szama):
    if szam==i:                                     # a szam egy szám 1 és 6 között, az i pedig egy index, ezek nem hasonlíthatók össze
        szam_index.append(i)
print(f'A számod ezeken a helyeken fordult elő {szam_index}.')

#Feladat 6
prim_szamok_osszeg=0
otosok_szama=0
for i in range(dobasok_szama):                      # itt is elcsúszott, az i egy index, nem a dobott szám
    if i==5:
        otosok_szama+=1
    elif i==1 or 2 or 3 or 5:                       # ez így nem írható, beszéljünk róla órán
        prim_szamok_osszeg+=1
print(f'A számok {prim_szamok_osszeg} szor volt prím.')
print(f'Az ötös szám {otosok_szama} szor fordult elő.')
#Feladat 7
legnagyobb=0
legkisebb=9999999999999
for i in range(dobasok_szama):
    if dobott_szam[i]>legnagyobb:                   # na ez az!!! Pontosan így kell használni az i-t. a dobott_szam[i] hasonlítod az értékekhez
        legnagyobb=dobott_szam[i]
    elif dobott_szam[i]<legkisebb:
        legkisebb=dobott_szam[i]
print(f'A legnagyobb szám a {legnagyobb} és a legkisebb a {legkisebb}.')
