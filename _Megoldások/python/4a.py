import random

dobasok = []
for i in range(100):
    dobas = random.randint(1, 6)
    dobasok.append(dobas)

print(dobasok)

hatosok_szama = 0
for i in range(len(dobasok)):
    if dobasok[i] == 6:
        hatosok_szama += 1

print(f'A dobások között {hatosok_szama} hatos volt.')

hatosok_szama = 0
for dobas in dobasok:
    if dobas == 6:
        hatosok_szama += 1

print(f'A dobások között {hatosok_szama} hatos volt.')
print(f'A dobások között {dobasok.count(6)} hatos volt.')

parosok_szama = 0
paratlan_szama = 0
for i in range(len(dobasok)):
    if dobasok[i] % 2 == 0:
        parosok_szama += 1
    else:
        paratlan_szama += 1

print(f'{parosok_szama} páros és {paratlan_szama} páratlan dobás volt.')

primek_szama = 0
primszamok = [2, 3, 5]
for i in range(len(dobasok)):
    if dobasok[i] in primszamok:
        primek_szama += 1

print(f'{primek_szama} prímszámot találtam.')


egyketto_szama = 0
for i in range(len(dobasok) - 1):
    if dobasok[i] == 1 and dobasok[i+1] == 2:
        egyketto_szama += 1
print(f'{egyketto_szama} esetben jött 1 után 2.')

nagyobbak_szama = 0
for i in range(len(dobasok) - 1):
    if dobasok[i] > dobasok[i+1]:
        nagyobbak_szama += 1
print(f'{nagyobbak_szama} esetben jött nagyobb.')

szamlalok = [0, 0, 0, 0, 0, 0]
for i in range(len(dobasok)):
    szamlalok[dobasok[i] - 1] += 1
print('Dobások:')
for i in range(6):
    print(f'\t{i+1}\t{szamlalok[i]} darab')
