forras= open('Szmodis Vince\\Erettsegi\\2026 okt\\meres.txt', mode='r', encoding='utf-8')

adatok=[]
for dat in forras:
    adat=dat.strip().split(',')
    for i in range(len(adat)):
        adatok.append(int(adat[i]))


print('2. feladat')
osszes=0
for i in range(len(adatok)):
    if adatok[i]>-1:
        osszes+=adatok[i]
print(f'Összesen {osszes} kerékpárost számoltak. ')

print('\n3. feladat')
semmi=0
szamlalo=0
hatos=0
hetes=0
nyolcas=0
kilences=0

for i in range(len(adatok)):
    szamlalo+=1
    if adatok[i]==-1:
        semmi+=1
    elif szamlalo<=3:
        hatos+=adatok[i]
    elif 3<szamlalo<=7:
        hetes+=adatok[i]
    elif 7<szamlalo<=11:
        nyolcas+=adatok[i]
    else:
        kilences+=adatok[i]

print(F'6 órától {hatos} kerékpáros ')
print(F'7 órától {hetes} kerékpáros ')
print(F'8 órától {nyolcas} kerékpáros ')
print(F'9 órától {kilences} kerékpáros ')

print()
print('4. feladat')

idopontok=['6:15', '6:30', '6:45', '7:00', '7:15', '7:30', '7:45', '8:00', '8:15', '8:30', '8:45', '9:00', '9:15', '9:30', '9:45', '10:00']

max=adatok[0]
max_index=0

for i in range(len(adatok)):
    if max<adatok[i]:
        max=adatok[i]
        max_index=i
print(f'Az áthaladók maximális száma: {max}; a rögzítés időpontja: {idopontok[max_index]}. ')