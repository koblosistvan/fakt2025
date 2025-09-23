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

for dobas in dobasok:
    if dobas == 6:
        hatosok_szama += 1

print(f'A dobások között {hatosok_szama} hatos volt.')