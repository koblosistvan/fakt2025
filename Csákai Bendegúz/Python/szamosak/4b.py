a = 96
eretsegizok = 100
import random
pontok = []

for i in range(eretsegizok):
    pontok.append(random.randint(0,120))
print(pontok)

jeles = 0
for i in range(len(pontok)):
    if pontok[i] >= a:
        jeles += 1
print(f'Jelesek száma:{jeles}')

majdnem = 0
for i in range(len(pontok)):
    if pontok[i] == a and pontok[i] >= a-3:
        majdnem += 1
print(f'3 vagy annál kevesebb ponttal lemaradóak száma: {majdnem}')

maxim = 0
for i in range(len(pontok)):
    if pontok[i] == 120:
        maxim += 1
print(f'Max pontosak száma: {maxim}')

for i in range(len(pontok)):
    atlag = sum(pontok) // eretsegizok
print(f' Az érettségik összesített átlaga: {atlag}')

sav = [0] * 10
for i in(pontok):
    