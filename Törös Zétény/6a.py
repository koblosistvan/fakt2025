forras = open('Törös Zétény\\6a-hallgatok.txt', mode='r', encoding='utf-8')

szul_ev = []
szul_ho = []
szul_nap = []
kezdes_ev = []
vegzes_ev = []

adatok_szama = int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    szul_ev.append(int(adat[0]))
    szul_ho.append(int(adat[1]))
    szul_nap.append(int(adat[2]))
    kezdes_ev.append(int(adat[3]))
    vegzes_ev.append(int(adat[4]))

elet_kor = int(input('Add meg az életkorod: '))
for i in range(adatok_szama):
    kor = vegzes_ev[i] - szul_ev[i]
    if kor < elet_kor:
        print(f'Van {elet_kor} nél fiatalabb végzet')
        break
else:
    print('Bocsi de nincs ilyen ember')

ho = int(input('Add meg hogy melyik hónapban születtél: '))
nap = int(input('Add meg hogy melyik napon születtél: '))

for i in range(adatok_szama):
    if  ho == szul_ho[i] and nap == szul_nap[i]:
        print('Van olyan ember akinek akkor van a szülinapja mint neked.')
        break
else:
     print('Nincs olyan ember akinek akkor van a szülinaplya mint neked.')

szul_eretsegi = vegzes_ev[0]-szul_ev[0]
szul_eretsegi_index = 0
for i in range(adatok_szama):
    if vegzes_ev[i] - szul_ev[i] <szul_eretsegi:
        szul_eretsegi = vegzes_ev[i] - szul_ev[i]
        szul_eretsegi_index = i

print(f'A legfiatalabban leéretségiző ember születési éve: {szul_ev[szul_eretsegi_index]}, és {vegzes_ev[szul_eretsegi_index]}')

vegzok_szama = 0
for i in range(adatok_szama):
    if vegzes_ev[i] == 2016:
        vegzok_szama += 1
print(f'A 2016-ban végzők száma: {vegzok_szama}')

eletkorok_osszege = 0
eletkorok_osszege_darab = 0

for i in range(adatok_szama):
    if kezdes_ev[i] <= 2014 <= vegzes_ev[i]: 
        eletkorok_osszege += 2014-szul_ev[i]
        eletkorok_osszege_darab += 1

print(f'A 2014-ben tanulók átlag életkora: {eletkorok_osszege/eletkorok_osszege_darab:.2f}')