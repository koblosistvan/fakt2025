import random
letszam=random.randint(15,20)
osztalyzatok=[]
for i in range(letszam):
    osztalyzat=random.randint(1,5)
    osztalyzatok.append(osztalyzat)

print(osztalyzatok)
#feladat_1
    print(i+1)

for i in range(letszam):
    osszeg=
#feladat_2 
    print(f'Az ostályzatok összege {osszeg}.')
#feladat_3
    print(f'Az osztályzatok átlaga {osszeg/letszam}')

#feladat_4
for i in range(letszam):
    if osztalyzat[i]< 2:
        print('Lett elégtelen osztályzat')
        break
    else:
        print('Nem lett elégtelen.')
#feladat_5
osztalyzat_index=[]
bekert_osztalyzat=int(input('Adj meg egy tetszőleges osztályzatot: '))
for i in range(letszam):
    if bekert_osztalyzat == osztalyzat[i]:
        osztalyzat_index.append(i)
        print(f'Az adott osztályzat a {osztalyzat_index}. helyeken fordul elő.')
#feladat_6
harmasnal_nagyobb=0
szam_elofordulasa=0
for i in range(letszam):
    if osztalyzat[i]==5:
        szam_elofordulasa += 1
    elif osztalyzat[i]>3:
        harmasnal_nagyobb += 1
print(f'Az 5-ös {szam_elofordulasa}-szor fordult elő és {harmasnal_nagyobb} jegy volt nagyobb 3-nál')
#feladat_7
legnagyobb_osztalyzat=[0]
legkisebb_osztalyzat=[0]
for i in range(letszam):
    if osztalyzat[i] > legnagyobb_osztalyzat:
        legnagyobb_osztalyzat=i
    elif osztalyzat[i] < legkisebb_osztalyzat:
        legkisebb_osztalyzat=i
print(f'A legnygobb osztályzat a {legnagyobb_osztalyzat} volt, a legkisebb meg a {legkisebb_osztalyzat} volt.')