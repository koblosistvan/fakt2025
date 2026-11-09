import random
dobas_szam=random.randint(100,120)

ertek=[]
szam=[]
for i in range(dobas_szam):
    szam=random.randint(1,6)
    ertek.append(szam)

print(f'A szimuláció során {dobas_szam} dobás történt')

osszeg=0
for i in range(dobas_szam):
    osszeg+=i
print(f'A dobott számok összege {osszeg}')

atlag=osszeg/dobas_szam
print(f'A dobott számok átlaga {atlag}')

for i in range(dobas_szam):
    if ertek[i]==6:
        print('Volt hatos dobás')
else:
    print('A listában nem volt hatos dobás')

bekert_szam=int(input('Adj meg egy számot:'))
elofordulas=[]
for i in range(dobas_szam):
    if ertek[i]==bekert_szam:
        elofordulas.append[i]
print(f'A dobások között a(z) {bekert_szam} előfordulása: {elofordulas}')

szamlalo=0
for i in range(dobas_szam):
    if ertek[i]==4:
        szamlalo+=1
print(f'A dobások között {szamlalo} alkalommal fordult elő, hogy a dobott szám 4 volt')

legnagyobb=ertek[0]
legkisebb=ertek[0]
for i in range(dobas_szam):
    if legnagyobb<ertek[i]:
        legnagyobb=ertek[i]

    elif legkisebb>ertek[i]:
        legkisebb=ertek[i]
print(f'A legkisebb dobott szám a(z) {legkisebb}, a legnagyobb a(z) {legnagyobb}')

