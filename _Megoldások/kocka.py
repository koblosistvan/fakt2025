import random

dobasok = []
for i in range(100):
    dobasok.append(random.randint(1, 6))
print(dobasok)

hatosok = 0
for i in range(100):
    if dobasok[i] == 6:
        hatosok += 1

for dobas in dobasok:
    if dobas == 6:
        hatosok += 1

print(hatosok)

egyreketto = 0
for i in range(99):
    if dobasok[i] == 1 and dobasok[i+1] == 2:
        egyreketto += 1
print(f'{egyreketto} esetben jött 2-es az 1-es után.')