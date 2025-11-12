forras = open ('Szmodis Vince\\python\\covid.txt', mode='r', encoding='utf-8')

datum=[]
fertozott=[]
halaleset=[]


for sor in forras:
    adat=sor.strip().split(';')
    datum.append(adat[0])
    fertozott.append(int(adat[1]))
    halaleset.append(int(adat[2]))

print('1. feladat')
print(f'Az állomány {len(fertozott)} nap adatait tartalmazza.')
print()

osszfertozott=0
osszhalaleset=0

for i in range(len(fertozott)):
    osszfertozott+=fertozott[i]
    osszhalaleset+=halaleset[i]

print('2. feladat')
print(f'A két év alatt összesen {osszfertozott} fertőzöttet és {osszhalaleset} halottat regisztráltak.')
print()

szazezer_alatt=0
for i in range(len(fertozott)):
    if fertozott[i]<100000:
        szazezer_alatt+=1
print('3. feladat')
print(f'A fertőzöttek száma {szazezer_alatt} napon volt 100e fő alatt.')
print()

maxhalal=halaleset[0]
maxhalal_index=0
for i in range(len(fertozott)):
    if maxhalal<halaleset[i]:
        maxhalal=halaleset[i]
        maxhalal_index=i
print('4. feladat')
print(f'Legtöbben {datum[maxhalal_index]} napon haltak meg:\n\t{fertozott[maxhalal_index]}\tfertőzött\n\t{halaleset[maxhalal_index]}\thalott')
print()

legnagyobb_novekedes_index=0
legnagyobb_novekedes=fertozott[1]/fertozott[0]
for i in range(len(fertozott)):
    if fertozott[i+1]/fertozott[i]:
        legnagyobb_novekedes=fertozott[i+1]/fertozott[i]
        legnagyobb_novekedes_index=i
print('5. feladat')
print(f'A legnagyobb arányú növekedés {datum[legnagyobb_novekedes_index]} napon volt, amikor az előző \nnapi adat {legnagyobb_novekedes}-szorosa volt a fertőzöttek száma.')
