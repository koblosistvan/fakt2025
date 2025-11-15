forras = open('fakt2025\\Csákai Bendegúz\\Python\\6b-forgalom.txt', mode = 'r', encoding = 'utf-8')
forras.readline()

hely = []
meres_ora = []
meres_perc = []
ido = []

for sor in forras:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    meres_ora.append(int(adat[1]))
    meres_perc.append(int(adat[2]))
    ido.append(int(adat[1])*60 + int(adat[2]))
forras.close

leghosz = ido[1] - ido[0]
leghosz_index = 0
meresek = len(hely)
for i in range(meresek-1):
    if ido[i] - ido[i-1] > leghosz:
        leghosz = ido[i] - ido[i-1]
        leghosz_index = i
    kezdodott = f'{meres_ora[leghosz_index-1]:0>2d}:{meres_perc[leghosz_index-1]:0>2d}'
    vegzodott = f'{meres_ora[leghosz_index]:0>2d}:{meres_perc[leghosz_index]:0>2d}'
print(f'{leghosz} volt a legnagyobb eltérés, ami {kezdodott}-kor kezdődött és {vegzodott}-kor végződött')

otvenes = 0
for i in range(meresek-1):
    if hely[i] == 50:
        otvenes += 1
print(f'{otvenes} érték tartozik az 50-es zónához')

idopont_ora = int(input('Add meg a keresett időpont óráját: '))
idopont_perc = int(input('Add meg a keresett időpont percét: '))
for i in range(meresek-1):
    if meres_ora[i] == idopont_ora and meres_perc[i] == idopont_perc:
        print(f'Van {idopont_ora:0>2d}:{idopont_perc:0>2d}-kor mérési eredmény')
        break
else:
    print('Nincs ilyenkor mérési eredmény')
for i in range(meresek-1):
    if meres_ora[i] == meres_ora[i+1] and meres_perc[i] == meres_perc[i+1]:
        print('Van ilyen időpont')
        break
else:
    print('Nincs ilyen időpont')

meresek_szama = [0]*101
for i in range(meresek):
    meresek_szama[hely[i]] += 1
print(meresek_szama)
print(meresek_szama.index(max(meresek_szama)))