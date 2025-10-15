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
    kezdodott = f'{meres_ora[leghosz_index-1]}:{meres_perc[leghosz_index-1]:0>2d}'
    vegzodott = f'{meres_ora[leghosz_index]}:{meres_perc[leghosz_index]:0>2d}'
print(f'{leghosz} volt a legnagyobb eltérés, ami {kezdodott}-kor kezdődött és {vegzodott}-kor végződött')

otvenes = 0
for i in range(meresek-1):
    if hely[i] == 50:
        otvenes += 1
print(f'{otvenes} érték tartozik az 50-es zónához')

idopont = input('Add meg melyik időponthoz tartozó mérést keressem meg: ')