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

for i in range(meresek):
    if hely[i] == 50:
        otven += 1
print(f'Az ötvenes mérési pontnál: {otven}-meres volt')

a_ora = int(input('Add meg hogy hány órakkor szeretnéd megnézni: '))
a_perc = int(input('Add meg hogy hány perckor szeretnéd megnézni: '))

for i in range(meresek):
    if ora[i] == a_ora and perc[i] == a_perc:
        print('Ekkor volt mérés.')
        break
else:
     print('Ekkor nem volt mérés.')

for i in range(meresek):
    if (ora[i] and perc[i]) == (ora[i+1] and perc[i+1]):
        print('Van olyan hogy 2 mérés történik 1 időpontban.')
        break

helyek =[0]*100
for i in range(meresek):
    helyek[hely[i]-1] += 1

legtobb_meres = helyek[0]

for i in range(len(helyek)):
    if helyek[i] > legtobb_meres:
        legtobb_meres = helyek[i]
print(f'A legtöbb mérés a {legtobb_meres+1}-edik mérési ponton történt.')