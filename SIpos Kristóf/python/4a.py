import random
rolls = []
for i in range(100):
    rolls.append(random.randint(1,6))
print(rolls)

rolled_6=0
for i in range (len(rolls)):
    if rolls[i] == 6:
        rolled_6 +=1
print(f'a dobások között {rolled_6} hatos volt. ')

paros=0
odd=0
prim=[2,3,5]
prim_szam=0

for i in range(len(rolls)):
    if rolls[i] % 2 == 0:
        paros += 1
    else:
        odd += 1
for i in range(len(rolls)):
    if rolls[i] in prim:
        prim_szam +=1
print(f'{paros} páros dobás volt')
print(f'{odd} páratlan dobások száma.')
print(f'{prim_szam} ennyi prím szám volt benne.')

egymas_mellet=0
for i in range(len(rolls)-1):
    if rolls[i] == 1 and rolls [i+1] == 2:
        egymas_mellet +=1
print(f'{egymas_mellet} enyiszer volt 1 után 2')

nagyobb = 0


szamlalok = [0,0,0,0,0,0]
for i in range(len(rolls)):
    szamlalok[rolls[i] - 1] += 1
print(szamlalok)

print(f'Dobosáok:\n\t 1\t {szamlalok[0]}\n\t 2\t {szamlalok[1]}\n\t 3\t {szamlalok[2]}\n\t 4\t {szamlalok[3]}\n\t 5\t {szamlalok[4]}\n\t 6\t {szamlalok[5]}\n\t  ')

