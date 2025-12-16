forras = open('fakt2025\\Csákai Bendegúz\\Python\\Cooper\\cooper.txt', mode='r', encoding='utf-8')
forras.readline()
def f(n):
    print(f'\n{n}. Feladat:')

f(1)
nev = []
tavaly = []
idei = []
for sor in forras:
    adat = sor.strip().split('\t')
    nev.append(str(adat[0]))
    tavaly.append(int(adat[1]))
    idei.append(int(adat[2]))
forras.close()
f(2)
print(f'A teszten {len(nev)} diák vett részt.')
f(3)
futott = 0
for i in range(len(idei)):
    if idei[i] >= 3000:
        futott += 1
if futott > 0:
    print(f'Idén {futott} diák futott legalább 3000 m-t.')
else:
    print(f'Idén senki nem futott legalább 3000 m-t.')
f(4)
index = 0
idei_leg = idei[0]
for i in range(len(nev)):
    if idei[i] > idei_leg:
        idei_leg = idei[i]
        index = i
print(f'Az idei legjobb eredményt {nev[index]} érte el {idei_leg} m-es távval.')
f(5)
legj_jav = idei[0] - tavaly[0]
legj_jav_ind = 0
for i in range(len(idei)):
    if idei[i] - tavaly[i] > legj_jav:
        legj_jav = idei[i] - tavaly[i]
        legj_jav_ind = i
        tavalyi = tavaly[i]
        iden = idei[i]
print(f'A legtöbbet {nev[legj_jav_ind]} javított, ő tavaly {tavalyi} m-t futott, idén {iden} m-t, így {legj_jav} m-t javított az eredményén.')