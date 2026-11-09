forras = open('Dobai Balint\\python\\szakkör\\labirintus.txt', mode ='r', encoding='utf-8')
adat = forras.readline().strip().split()
magassag ,  szelesseg = int(adat[0]) , int(adat[1])

lab = []

for _ in range(magassag):
    lab.append(forras.readline().strip())

print('\n'.join(lab))

graf = {}
szomszedok =[
    (-1,0),
    (0,-1),
    (0,1),
    (1,0),
]

def uj_el(a,b):
    if a in graf:
        graf[a].append(b)
    else:
        graf[a] = [b]

for sor in range(1,magassag-1):
    for oszlop in range(1,szelesseg-1):
        for sz in szomszedok:
            en = lab[sor][oszlop]
            szomszed = lab[sor+sz[0]][oszlop+sz[1]]
            if en =='.' and szomszed =='.':
                uj_el(sor*10+ oszlop, (sor+sz[0])*10 +oszlop +sz[1])

print(graf)