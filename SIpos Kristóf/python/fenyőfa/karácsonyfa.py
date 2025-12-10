#Feladat 1
print('Feladat 1')
forras=open('Sipos Kristóf\\python\\fenyőfa\\fenyofa.txt',mode='r',encoding='utf-8')

adat= forras.readline().strip().split(' ')
sorok_szama,oszlopok_szama=int(adat[0]),int(adat[1])

pixelek=[]
for i in range(sorok_szama):
    pixel=forras.readline()[:oszlopok_szama]
    pixelek.append(pixel)
forras.close
print('Az adatok belettek olvasva.')
#Feladat 2
print('Feladat 2')
snow=0
for sor in range(sorok_szama):
    for oszlop in range(oszlopok_szama):
        if pixelek[sor][oszlop] == 'f':
            snow += 1
print(f'A hópihék száma az {snow}.')
#Feladat 3
print('Feladat 3')
torzs_magassaga=[]
for sor in range(sorok_szama):
    for oszlop in range(oszlopok_szama):
        if pixelek[sor][oszlop]== 'b': 
            torzs_magassaga.append(sor)
print(f'A törzs a {min(torzs_magassaga)}. sorban kezdődik.')

#Feladat 4
print('Feladat 4')
torzs_kezdete=min(torzs_magassaga)
torzs_vege=max(torzs_magassaga)
print(f'A törzs {torzs_vege} és a törzs {torzs_vege-torzs_kezdete} magas.')
#Feladat 5
print('Feladat 5')
diszek_szama=0
for sor in range(sorok_szama):
    for oszlop in range(oszlopok_szama):
        if  sor > 5:
            if pixelek[sor][oszlop] in 'skp':
                diszek_szama += 1
print(f'{diszek_szama} dísz van.')
#Feladat 6
print('Feladat 6')
nem_disz='hzbf'
szinek_szama = {}
for sor in range(sorok_szama):
    for oszlop in range(oszlopok_szama):
        pixel_szin = pixelek[sor][oszlop]
        if pixel_szin not in nem_disz:
            if pixel_szin in szinek_szama:
                szinek_szama[pixel_szin] += 1
            else:
                szinek_szama[pixel_szin] = 1
print(szinek_szama)