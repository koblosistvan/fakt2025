FAL = '#'
UT = ' '

forras = open('_Megoldások\\Szakkör\\Labirintus\\labirintus-42-41x41.txt', mode='r', encoding='utf-8')
adat = forras.readline().strip().split()
magassag, szelesseg = int(adat[0]), int(adat[1])

adat = forras.readline().strip().split()
kijarat = ( int(adat[0]), int(adat[1]) )

adat = forras.readline().strip().split()
start = ( int(adat[0]), int(adat[1]) )

labirintus = []
for _ in range(magassag):
    labirintus.append(forras.readline().strip())

print('\n'.join(labirintus))

'''
graf = {
    '1': [2, 3, 4],
    '2': [1, 4, 7]
}
'''
kesz=[]
graf = {}
szomszedok = [
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, 0),
]


def uj_el(a, b):
    if a not in graf:
        graf[a] = []
    graf[a].append(b)
    

for sor in range(1, magassag-1):
    for oszlop in range(1, szelesseg-1):
        # végigmegyünk a szomszédokon
        for sz in szomszedok:
            én = labirintus[sor][oszlop]
            szomszed = labirintus[sor + sz[0]][oszlop + sz[1]]
            # én is UT vagyok és a szomszéd is, akkor élt találtam
            if én == UT and szomszed == UT:
                uj_el((sor, oszlop), (sor + sz[0], oszlop + sz[1])) 

#print(graf)

tavolsag ={csucs:1000 for csucs in graf}
elozo={csucs: None for csucs in graf}
sor=[start]
tavolsag[start]=0

while len(sor)>0:
    akt_csucs= sor[0]
    akt_tav=tavolsag[akt_csucs]
    for csucs in sor:
        if tavolsag[csucs] < tavolsag[akt_csucs]:
            akt_csucs=csucs
            akt_tav= tavolsag[csucs]
    
    sor.remove(akt_csucs)
    kesz.append(akt_csucs)
    for szomszed in graf[akt_csucs]:
        tav =tavolsag[akt_csucs]+1
        if tav<tavolsag[szomszed]:
            tavolsag[szomszed]=tav
            elozo[szomszed]=akt_csucs
        if szomszed not in kesz:
            sor = sor+[szomszed]
ut=[]
akt_csucs=kijarat
while akt_csucs != start:
    ut=ut+[akt_csucs]
    akt_csucs=elozo[akt_csucs]
ut=[akt_csucs]+ut
print(ut)

utvonal=open('_Megoldások\\Szakkör\\Labirintus\\utvonal_vince.txt', mode='w', encoding='utf-8')
for sor in range(magassag):
   print('\n  ',end='', file=utvonal)
   for oszlop in range(szelesseg):
        if (sor,oszlop) in ut:
            print('o',end='', file=utvonal)
        
        else:
            print (labirintus[sor][oszlop], end='', file=utvonal)
utvonal.close()