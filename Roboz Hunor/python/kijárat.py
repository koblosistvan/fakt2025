forras = open('_Megoldások\\Szakkör\\Labirintus\\labirintus.txt',mode='r',encoding='utf-8')
adat = forras.readline().split()
magasság,szélesseg = int(adat[0]),int(adat[1])

labirintus = []

for _ in range(magasság):
    labirintus.append(forras.readline().strip())

print('\n'.join(labirintus))

