forras = open('Roboz Hunor\\python\\futar.txt',mode='r',encoding='utf-8')
megtett_ut = int(forras.readline())

nap,ut_szam,km = [],[],[]

for sor in forras:
    adat = sor.strip().split()
    nap.append(int(adat[0]))
    ut_szam.append(int(adat[1]))
    km.append(int(adat[2]))
forras.close()

print(f'Adatok beolvasása...\nA futar.txt fájlból beolvastam {megtett_ut} sort.')


def f(n):
    print(f'{n}. feladat')


f(1)


leg_hosszabb_tav,leg_hosszabb_nap,leg_hosszabb_ut = km[0],nap[0],ut_szam[0]

for i in range(megtett_ut):
    if km[i] > leg_hosszabb_tav:
        leg_hosszabb_tav,leg_hosszabb_nap,leg_hosszabb_ut = km[i],nap[i],ut_szam[i]

print(f'A leghosszabb út: {leg_hosszabb_nap}. nap, {leg_hosszabb_ut}. fuvar - {leg_hosszabb_tav} km.')


f(2)


össz_ut_3 = 0

for i in range(megtett_ut):
      if nap[i] == 3:
        össz_ut_3 += km[i]

print(f'A harmadik napon összesen {össz_ut_3} km-t tett meg.')


f(3)


db_fuvar_4 = 0

for i in range(megtett_ut):
    if nap[i] == 4:
        db_fuvar_4 += 1

print(f'A negyedik napon {db_fuvar_4} fuvart teljesített.')


f(4)


for i in range(megtett_ut):
    if km[i] > 20:
        print(F'A futárnak volt 20 km-nél hosszabb útja.')
        break
else: print(f'A futárnak nem volt 20 km-nél hosszabb útja.')


kim = open('Roboz Hunor\\python\\futar-kimenet',mode='w',encoding='utf-8')

for i in range (megtett_ut):
    if ut_szam[i] == 1:
        print(f'{nap[i]}. nap\t{km[i]} km',file=kim)


kim_2 = open('Roboz Hunor\\python\\futar-rendezett',mode='w',encoding='utf-8')

for i in range(megtett_ut):
    for k in range(megtett_ut-i-1):
        if km[k] < km[k+1]:
            nap[k],nap[k+1],ut_szam[k],ut_szam[k+1],km[k],km[k+1] = nap[k+1], nap[k],ut_szam[k+1],ut_szam[k],km[k+1],km[k]
        elif km[k] == km[k+1]:
            if nap[k] > nap[k+1]:
                nap[k],nap[k+1],ut_szam[k],ut_szam[k+1],km[k],km[k+1] = nap[k+1], nap[k],ut_szam[k+1],ut_szam[k],km[k+1],km[k]
            elif nap[k]  == nap[k+1]:
                if ut_szam[k] > ut_szam[k+1]:
                    nap[k],nap[k+1],ut_szam[k],ut_szam[k+1],km[k],km[k+1] = nap[k+1], nap[k],ut_szam[k+1],ut_szam[k],km[k+1],km[k]


print(megtett_ut,file=kim_2)
for i in range(megtett_ut):
    print(f'{nap[i]} {ut_szam[i]} {km[i]}',file=kim_2)