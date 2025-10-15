forrás = open(
    '_Megoldások\\python\\6b-forgalom.txt', 
    mode='r', 
    encoding='utf-8')
a = forrás.readline
első_sor = a()

# Írj programot,amely megadja, hogy mi a leghosszabb idő-intervallum 
# kezdete és vége, amikor a két időpont között sehol sem haladt át 
# jármű!(min/max)
hely = []
ora = []
perc = []
ido = []
for sor in forrás:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1])*60 + int(adat[2]))
forrás.close()
meresek_szama = len(hely)

legh = ido[1] - ido[0]
legh_index = 0
for i in range(meresek_szama - 1):
    if ido[i+1] - ido[i] > legh:
        legh = ido[i+1] - ido[i]
        legh_index = i
kezdete = f'{ora[legh_index]:0>2d}:{perc[legh_index]:0>2d}'
vege = f'{ora[legh_index+1]:0>2d}:{perc[legh_index+1]:0>2d}'
print(f'A leghosszabb idő-intervallum kezdete {kezdete}, a vége: {vege}.')

# Oldd meg a feladatot úgy is, hogy az egyes mérési pontokat külön vizsgáljuk,
# tehát pl. az 1-es pont időintervallumába nem számítjuk bele, ha a 2-es ponton
# haladt át jármű!(min/max)
legh_kezdete = []
legh_vege = []
legh_ido = []

for pont in set(hely):
    pont_ora = [ora[i] for i in range(meresek_szama) if hely[i] == pont]
    pont_perc = [perc[i] for i in range(meresek_szama) if hely[i] == pont]
    pont_ido = [ido[i] for i in range(meresek_szama) if hely[i] == pont]

    legh = pont_ido[1] - pont_ido[0]
    legh_index = 0
    for i in range(len(pont_ora) - 1):
        if pont_ido[i+1] - pont_ido[i] > legh:
            legh = pont_ido[i+1] - pont_ido[i]
            legh_index = i

    legh_kezdete.append(
        f'{pont_ora[legh_index]:0>2d}:{pont_perc[legh_index]:0>2d}')
    legh_vege.append(
        f'{pont_ora[legh_index+1]:0>2d}:{pont_perc[legh_index+1]:0>2d}')
    legh_ido.append(legh)
legh_index = legh_ido.index(max(legh_ido))
print(
    f'A leghosszabb idő-intervallum kezdete ' +
    '{leghosszabb_kezdete[leghosszabb_index]}, ' +
    'a vége: {leghosszabb_vege[leghosszabb_index]}.')


szamlalok = [0] * 101
for i in range(meresek_szama):
    szamlalok[hely[i]] += 1
print(szamlalok)
