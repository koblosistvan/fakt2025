import random

dobasok = []
dobasok_szama = []                              # ezt utána használhatnád is :) - de akkor egész szám kéne legyen, nem lista
for i in range(random.randint(100,120)):
    dobasok.append(random.randint(1,6))
print(dobasok)

for i in range(len(dobasok)):                   # ezt felesleges ciklusba szervezni, lényegében a len(dobasok) megadja a választ
    osszeg = len(dobasok)
print(f'{osszeg} db dobas volt')

for i in range(len(dobasok)):                   # erre ugyanaz igaz, mint az előzőre
    dobas_ossz = sum(dobasok)                   # jó lenne, ha a megszámlálás algoritmust is látnám a kódban

print(f'{dobas_ossz} a dobasok osszege')

atlag = dobas_ossz / len(dobasok)
print(f'a dobasok atlaga: {atlag:.1f}')

hatos = dobasok[0]                              # ezt nem használod sehol
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
        kettes_index += 1                       # ez így nem jó, nem a sorszámát, hanem a kettesek darabszámát adod vissza

keresett = int(input('adj meg egy szamot'))

db = dobasok.count(keresett)
print(f'a {keresett} szam {db}-szor fordult elo')   # itt is csak a beépített függvényt látom, az algoritmust nem


negyes = dobasok[0]
negyes_index = 0

for i in range(len(dobasok)):
    if dobasok[i] == 4:
        negyes_index += 1

print(f' a negyes szam {negyes_index}-szer fordult elo')    # na, ez végre király!!!
                                                            # egy apró dolog: az xxx_index arra utal, hogy ez egy indexet (sorszámot) tároló változó
                                                            # pedig ez a darabszámot tárolja
                                                            # szerencsésebb lenne negyes_darabszam-nak nevezni

primek_szama = 0 
primszamok = [2,3,5]
for i in range(len(dobasok)):
    if dobasok[i] in primszamok:
        primek_szama += 1                                   # ez végre már szép és átlátható :)

print(f' a primek szama {primek_szama}')

primek_atlaga = primek_szama / len(dobasok)                 # a számolás jó, de a változónév megint félrevezető (aránya != átlaga) (!= jelentése nem egyenlő)

print(f'{primek_atlaga*100:.1f} % volt a primek aranya')

print(f' a legrosszabb dobas {min(dobasok)}, a legjobb pedig {max(dobasok)}')