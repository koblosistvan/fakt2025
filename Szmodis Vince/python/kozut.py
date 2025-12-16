forras=open('Szmodis Vince\\python\\kozut.txt', mode='r', encoding='utf-8')
adatok_szama=int(forras.readline())
ora=[]
perc=[]
masodperc=[]
sebesseg=[]
rendszam=[]

def f(n):
    print(f'\n{n}. feladat')

for sor in forras:
    adat=sor.strip().split(' ')
    ora.append(int(adat[0]))
    perc.append(int(adat[1]))
    masodperc.append(int(adat[2]))
    sebesseg.append(int(adat[3]))
    rendszam.append(adat[4])

atlepte=0
for i in range(adatok_szama):
    if sebesseg[i]>50:
        atlepte+=1
f(1)
print(f'{atlepte} autó volt gyorsabb a megengedett 50 km/h-nál.')

f(2)
for i in range(adatok_szama):
    if sebesseg[i]>55:
        print('Volt 55 km/h-nál gyorsabb autó.')
        break
    else:
        print('Nem volt 55 km/h-nál gyorsabb autó.')

max_sebesseg=sebesseg[0]
max_sebesseg_index=0
for i in range(adatok_szama):
    if max_sebesseg<sebesseg[i]:
        max_sebesseg=sebesseg[i]
        max_sebesseg_index=i
f(3)
print(f'A leggyorsabb autó rendszáma: {rendszam[max_sebesseg_index]}, {max_sebesseg} km/h sebességgel ment.')

f(4)
ossz=0
for i in range(adatok_szama):
    ossz+=sebesseg[i]
print(f'Az áthaladó autók átlagsebessége {round(ossz/adatok_szama,2)} km/h volt.')

    