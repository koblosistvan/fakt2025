forrás = open('_Megoldások\\python\\6b-forgalom.txt', mode='r', encoding='utf-8')
a = forrás.readline
első_sor = a()

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

leghosszabb = ido[1] - ido[0]
leghosszabb_index = 0
for i in range(meresek_szama - 1):
    if ido[i+1] - ido[i] > leghosszabb:
        leghosszabb = ido[i+1] - ido[i]
        leghosszabb_index = i
kezdete = f'{ora[leghosszabb_index]:0>2d}:{perc[leghosszabb_index]:0>2d}'
vege = f'{ora[leghosszabb_index+1]:0>2d}:{perc[leghosszabb_index+1]:0>2d}'
print(f'A leghosszabb idő-intervallum kezdete {kezdete}, a vége: {vege}.')