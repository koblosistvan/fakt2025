import random

dobasok = []

for i in range (100):
    dobasok.append(random.randint(1, 6))

print(dobasok)

hat = 0

for i in range (100):
    if dobasok[i] == 6:
        hat += 1

print(f'A dobások között {hat} hatos volt')
if hat > 26:
    print('új rekord')