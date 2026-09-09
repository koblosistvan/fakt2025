adatok = [36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]
def f(n):
    print(f'\n{n}. feladat')
f(1)
print('Az adatokat eltároltam')
f(2)

ossz_kerekparos = 0
for i in adatok:
    if i > 0:
        ossz_kerekparos += i
    else:
        ossz_kerekparos += 0

print(f'Összesen {ossz_kerekparos} kerékpárost számoltak.')

f(3)
ido = 6
osszesen = 0
szam = 1
for i in range(len(adatok)):
    if szam == 4: 
        if adatok[i] > 0:
            osszesen += adatok[i]
        print(f'{ido} órától {osszesen} kerékpáros.')
        szam = 1
        ido += 1
        osszesen = 0
    else:
        if adatok[i] > 0:
            osszesen += adatok[i]
        szam += 1
f(4)
o = 6
p = 15
idopontok = []
for i in range(len(adatok)):
    if p < 60: 
        if p == 0:
            idopontok.append(f"{o}:{p}{p}")
        else:
            idopontok.append(f"{o}:{p}")    
        p += 15
    else:
        p = 0
        o += 1
        if p == 0:
            idopontok.append(f"{o}:{p}{p}")
        else:
            idopontok.append(f"{o}:{p}")
        p += 15
legn = adatok[0]
legni = idopontok[0]
for i in range(len(adatok)):
    if adatok[i] > legn:
        legn = adatok[i]
        legni = idopontok[i]
print(f'Az áthaladók maximális száma: {legn}; a rögzítés időpontja: {legni}.')