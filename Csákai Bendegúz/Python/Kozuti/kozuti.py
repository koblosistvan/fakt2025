forras = open('fakt2025\\Csákai Bendegúz\\Python\\Kozuti\\kozut.txt', mode='r', encoding='utf-8')
ossz_auto = int(forras.readline().strip())
ora = []
perc = []
masodperc = []
sebesseg = []
rendszam = []
for sor in forras:
    adat = sor.strip().split(' ')
    ora.append(int(adat[0]))
    perc.append(int(adat[1]))
    masodperc.append(int(adat[2]))
    sebesseg.append(int(adat[3]))
    rendszam.append(str(adat[4]))
forras.close()
print(f'Beolvastam {ossz_auto} adatot.')
def f(n):
    print(f'\n{n}. feladat')


f(1)
otvennel = 0
for i in range(ossz_auto):
    if sebesseg[i] > 50:
        otvennel += 1
print(f'{otvennel} autó volt gyorsabb a megengedett 50 km/h-nál.')
f(2)
for i in range(ossz_auto):
    if sebesseg[i] > 55:
        print('Volt 55 km/h-nál gyorsabb autó')
        break
else:
    print('Nem volt 55 km/h-nálgyorsabb autó')
f(3)
index = 0
leggy = sebesseg[0]
for i in range(ossz_auto):
    if sebesseg[i] > leggy:
        leggy = sebesseg[i]
        index = i
print(f'A leggyorsabb autó rendszáma: {rendszam[index]}, {leggy} km/h sebességgel ment.')
f(4)
print(f'Az áthaladó autók átlagsebessége {sum(sebesseg)/len(sebesseg):.2f} km/h volt.')
f(5)
kimenet = open('fakt2025\\Csákai Bendegúz\\Python\\Kozuti\\kozut-kimenet.txt', mode='w', encoding='utf-8')
for i in range(ossz_auto):
    if sebesseg[i] < 30:
        print(f'{ora[i]}:{perc[i]}:{masodperc[i]} - {rendszam[i]} - {sebesseg[i]} km/h', file=kimenet)
kimenet.close()
f(6)
kimenet2 = open('fakt2025\\Csákai Bendegúz\\Python\\Kozuti\\kozut-rendezett.txt', mode='w', encoding='utf-8')
for i in range(ossz_auto):
    for j in range(ossz_auto-i-1):
        if rendszam[j] > rendszam[j+1]:
            rendszam[j], rendszam[j+1] = rendszam[j+1], rendszam[j]
            ora[j], ora[j+1] = ora[j+1], ora[j]
            perc[j], perc[j+1] = perc[j+1], perc[j]
            masodperc[j], masodperc[j+1] = masodperc[j+1], masodperc[j]
            sebesseg[j], sebesseg[j+1] =  sebesseg[j+1], sebesseg[j]
for i in range(ossz_auto):
    if sebesseg[i] > 50:print(f'{ora[i]}:{perc[i]}:{masodperc[i]} - {rendszam[i]} - {sebesseg[i]} km/h', file=kimenet2)
kimenet2.close()
f(7)
for i in range(ossz_auto):
    for j in range(ossz_auto-i-1):
        if (ora[j], perc[j], masodperc[j]) > (ora[j+1], perc[j+1], masodperc[j+1]):
            rendszam[j], rendszam[j+1] = rendszam[j+1], rendszam[j]
            ora[j], ora[j+1] = ora[j+1], ora[j]
            perc[j], perc[j+1] = perc[j+1], perc[j]
            masodperc[j], masodperc[j+1] = masodperc[j+1], masodperc[j]
            sebesseg[j], sebesseg[j+1] =  sebesseg[j+1], sebesseg[j]
for i in range(ossz_auto):
    if sebesseg[i] > 90 and sebesseg[i+1] > 90:
        print(f'Volt utcai verseny.')
        break
else:
    print(f'Nem volt utcai verseny.')
f(8)
'''for i in range(ossz_auto):
    for j in range(ossz_auto-i-1):
        if rendszam[j] > rendszam[j+1]:
            rendszam[j], rendszam[j+1] = rendszam[j+1], rendszam[j]
            ora[j], ora[j+1] = ora[j+1], ora[j]
            perc[j], perc[j+1] = perc[j+1], perc[j]
            masodperc[j], masodperc[j+1] = masodperc[j+1], masodperc[j]
            sebesseg[j], sebesseg[j+1] =  sebesseg[j+1], sebesseg[j]
for i in range(ossz_auto-1):
    if rendszam [i] == rendszam[i+1]:
        print(f'{ora[i+1]}:{perc[i+1]}:{masodperc[i+1]} - {rendszam[i+1]}')
    elif rendszam [i] != rendszam [i+1] and rendszam[i] == rendszam[i+1]:
        print(f'{ora[i]}:{perc[i]}:{masodperc[i]} - {rendszam[i]}')'''
'''mar_athaladt = []
tobb = 0
for i in range(ossz_auto):
    if rendszam[i] not in mar_athaladt:
        mar_athaladt.append(rendszam[i])
    else:
        print(f'{ora[i]}:{perc[i]}:{masodperc[i]} - {rendszam[i]}')
        tobb += 1
print(tobb)'''