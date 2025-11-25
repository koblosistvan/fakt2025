forras = open('Roboz Hunor\\python\\covid.txt', mode='r', encoding='utf-8')
nap = []
regisztrált = []
halott = []
for sor in forras:
    adat = sor.strip().split(';')
    nap.append(adat[0])
    regisztrált.append(int(adat[1]))
    halott.append(int(adat[2]))
forras.close()
adatok_szama = len(regisztrált)

for i in range(adatok_szama - 1):       # i = ennyi rekrod van már fent a víz tetején
    for j in range(adatok_szama - 1 - i):
        if regisztrált[j] < regisztrált[j+1]:
            nap[j], nap[j+1] = nap[j+1], nap[j]
            regisztrált[j], regisztrált[j+1] = regisztrált[j+1], regisztrált[j]
            halott[j], halott[j+1] = halott[j+1], halott[j]

print(f'Megbetegedési toplist:')
for i in range(5):
    print(f'{i+1}. {nap[i]}: {regisztrált[i]}')
