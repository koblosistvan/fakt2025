import random

dobasok = []
dobasok_szama = []
for i in range(random.randint(100,120)):
    dobasok.append(random.randint(1,6))
print(dobasok)

for i in range(len(dobasok)):
    osszeg = len(dobasok)
print(f'{osszeg} db dobas volt')

for i in range(len(dobasok)):
    dobas_ossz = sum(dobasok)

print(f'{dobas_ossz} a dobasok osszege')

atlag = dobas_ossz / len(dobasok)
print(f'a dobasok atlaga: {atlag:.1f}')

hatos = dobasok[0]
for i in range(len(dobasok)):
    if dobasok[i] == 6:
        print('van hatos dobas')
        break
else:
    print('nincs hatos dobas')

kettes = dobasok[0]
kettes_index = 0

for i in range(len(dobasok)):
    if dobasok[i] == 2:
        kettes_index += 1

keresett = int(input('adj meg egy szamot'))

db = dobasok.count(keresett)
print(f'a {keresett} szam {db}-szor fordult elo')


negyes = dobasok[0]
negyes_index = 0

for i in range(len(dobasok)):
    if dobasok[i] == 4:
        negyes_index += 1

print(f' a negyes szam {negyes_index}-szer fordult elo')


primek_szama = 0 
primszamok = [2,3,5]
for i in range(len(dobasok)):
    if dobasok[i] in primszamok:
        primek_szama += 1 

print(f' a primek szama {primek_szama}')

primek_atlaga = primek_szama / len(dobasok)

print(f'{primek_atlaga*100:.1f} % volt a primek aranya')

print(f' a legrosszabb dobas {min(dobasok)}, a legjobb pedig {max(dobasok)}')