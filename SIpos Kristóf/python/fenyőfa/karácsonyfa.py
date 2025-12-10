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
for sor in range(sorok_szama):
    for oszlop in range(oszlopok_szama):
        if 'b' in pixelek[sor][oszlop]: 
            break
print(f'A törzs a {sor}. sorban kezdődik.')

#Feladat 4
print('Feladat 4')

#Feladat 5
print('Feladat 5')
nem_disz='hzbf'
szinek_szama = {}
for sor in range(sorok_szama):
    for oszlop in range(oszlopok_szama):
        if pixel[sor][oszlop] not in nem_disz:
            if pixel[sor][oszlop] in szinek_szama:

            else:
                pixel[sor][oszlop].append(szinek_szama)

#Feladat 6
print('Feladat 6')