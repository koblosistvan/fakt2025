forras = open('Roboz Hunor\\python\\labirintus.txt',mode='r',encoding='utf-8')
adat = forras.readline().split()
magasság,szélesseg = int(adat[0]),int(adat[1])

labirintus = []

for _ in range(magasság):
    labirintus.append(forras.readline().strip())

print('\n'.join(labirintus))

graf = {}
szomszédok = [
    (-1,0),
    (0,-1),
    (0,1),
    (1,0)
]


def uj_el(a,b):
    if a in graf:
        graf[a].append(b)
    else:
        graf[a] = [b]



for sor in range(1, magasság-1):
    for oszlop in range (1, szélesseg-1):
        for sz in szomszédok:
            én = labirintus [sor][oszlop]
            szomszed = labirintus [sor+sz[0]][oszlop+sz[1]]
            if én == '.' and szomszed == '.':
                uj_el(sor*10+oszlop,(sor+sz[0])*10 +oszlop +sz[1])


print(graf)