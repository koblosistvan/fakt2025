import random

dobasok = []

for i in range (100):
    dobasok.append(random.randint(1, 6))

print(dobasok)

hat = 0

for i in range (100):
    if dobasok[i] == 6:
        hat += 1

paros = 0
print(f'A dobások között {hat} hatos volt')

for i in range (len(dobasok)):
    if dobasok[i] % 2 == 0:
        paros += 1
print(f'Párs dobásk száma: {paros}.  Páratlan dobások száma: {100-paros}')

primek_mennisege = 0
primszamok = [2, 3, 5]
for i in range (len(dobasok)):
    if dobasok [i] % 2 == 0:
        primek_mennisege += 1

print(f'Ennyi prímszám van: {primek_mennisege}')

egy_kettoszam = 0
for i in range(len(dobasok)-1):
    if dobasok[i] == 1 and dobasok[i+1] == 2:
        egy_kettoszam += 1
print(f'Ennyi esetben jön az egy a kettő után: {egy_kettoszam}')

nagyobb = 0
for i in range(len(dobasok)-1):
    if dobasok[i] < dobasok[i+1]:
        nagyobb += 1

print(f'Ennyi nagyobb dobás van az előzőnél: {nagyobb}')

szamok = [0, 0, 0, 0, 0, 0]
for i in range(len(dobasok)):
    szamok[dobasok[i] -1] += 1
print(szamok)

egy = 0
kettő = 0
három = 0
négy = 0
öt = 0
hat = 0


for i in range(len(dobasok)):
    if dobasok[i] == 1:
        egy += 1
    elif dobasok[i] == 2:
        kettő += 1
    elif dobasok[i] == 3:
        három += 1
    elif dobasok[i] == 4:
        négy += 1
    elif dobasok[i] == 5:
        öt += 1
    else:
        hat += 1

print(f'Egyesek száma: {egy} Kettesek száma: {kettő} Hármask száma: {három} Négyesek száma: {négy} Ötösök száma: {öt} Hatosok száma: {hat}')

