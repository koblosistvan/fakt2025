import math
forras = open('Szmodis Vince\\Erettsegi\\2026 maj\\nyomas.txt', mode='r', encoding='utf-8')
sor=forras.readline()
adatok=[]
adat=sor.strip().split(',')
for i in range(len(adat)):
    adatok.append(int(adat[i]))

print('2. feladat')

min_adat=adatok[0]
min_adat_index=0

for i in range(len(adatok)):
    if min_adat>adatok[i]:
        min_adat=adatok[i]
        min_adat_index=i
print(f'A legkisebb mért érték: {min_adat} ')
print(f'A legkisebb mérési adat sorszáma: {min_adat_index} ')
print()
print('3. feladat')
hatar=int(input('Minél kisebb értékeket keres? (egész szám) '))
alattszamlalo=0
for i in range (len(adatok)):
    if hatar>adatok[i]:
        alattszamlalo+=1
print(f'{hatar} alatti mérések száma: {alattszamlalo} ')
print()
print('4. feladat')
max_csokkenes=0
for i in range(len(adatok)-1):
    if abs(adatok[i]-adatok[i+1])>max_csokkenes:
        max_csokkenes=abs(adatok[i]-adatok[i+1])
print(f'A két mérés közötti legnagyobb csökkenés: {max_csokkenes} ')