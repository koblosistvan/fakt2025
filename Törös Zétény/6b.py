forras = open('H:\\Törös Zétény\\GIT\\fakt2025\\Törös Zétény\\6b-forgalom.txt', mode='r', encoding='utf-8')
forras.readline()

hely = []
ora = []
perc = []
ido = []
for sor in forras:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1])*60 + int(adat[2]))
forras.close()
meresek = len(hely)

leghosszabb = ido[0]-ido[1]
leghosszabb_index = 0

for i in range(meresek-1):
    if ido[i]-ido[i-1] > leghosszabb:
        leghosszabb = ido[i]-ido[i-1]
        leghosszabb_index = i

kezdete = f'{ora[leghosszabb_index-1]:0>2d}:{perc[leghosszabb_index-1]:0>2d}'
vege = f'{ora[leghosszabb_index]:0>2d}:{perc[leghosszabb_index]:0>2d}'
print(f'A leghosszabb nyugalom {kezdete}-kor kezdődött, és {vege}-kor végzőfött.')

otven = 0

for i in range(meresek-1):
    if hely[i] == 50:
        otven += 1
print(f'{otven}')