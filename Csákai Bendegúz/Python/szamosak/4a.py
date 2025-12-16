import random

dobasok = []
for i in range(100):
    dobasok.append(random.randint(1,6))
print(dobasok)

hatosok_szama = 0
for i in range(len(dobasok)):
    if dobasok[i] == 6:
        hatosok_szama += 1

print(f'A dobások között {hatosok_szama} hatos van')
print(f'A dobások között {dobasok.count(6)} hatos van')

paros = 0
paratlan = 0
for i in range(len(dobasok)):
    if dobasok[i] % 2 == 0:
        paros += 1
    else:
        paratlan += 1
print(f'A párosok száma: {paros}')
print(f'A páratlanok száma: {paratlan}')

primek = [2,3,5]
prim = 0
for i in range(len(dobasok)):
    if dobasok[i] in primek:
        prim += 1
print(f'A prímek száma: {prim}')

egymajdketto = 0
for i in range (len(dobasok)-1):
    if dobasok[i] == 1 and dobasok[i+1] == 2:
        egymajdketto += 1
print(f'Egy után kettő {egymajdketto} alkalommal van')

nagyobb = 0
for i in range(len(dobasok)):
    if dobasok[i] > dobasok[i-1]:
        nagyobb += 1
print(f'{nagyobb} esetben volt nagyobb a következő szám az előzőnél')

szamlalok = [0,0,0,0,0,0]
for i in range(len(dobasok)):
    szamlalok[dobasok[i]-1] += 1
print(szamlalok)

print('Dobások:')
for i in range(len(dobasok)):
    print(f'\n\t {i+1} \t {szamlalok[i]}')