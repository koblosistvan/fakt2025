forras = open('fakt2025\\Csákai Bendegúz\\Python\\imdb.txt', mode='r', encoding='utf-8')
forras.readline()
ev = []
hossz = []
ertek = []
rendez = []
bevet = []
cim = []
for sor in forras:
    adat = sor.strip().split('\t')
    ev.append(int(adat[0]))
    hossz.append(int(adat[1]))
    ertek.append(float(adat[2]))
    rendez.append(adat[3])
    bevet.append(int(adat[4]))
    cim.append(adat[5])
forras.close()
db = len(ev)
print('\n')
print(f'Összesen {db} filmmel rendelkezem.')
print(f'Az első film ekkor jelent meg: {min(ev)}')
kettonel_hosszabb=0
for i in range(db):
    if hossz[i] > 120:
        kettonel_hosszabb += 1
if kettonel_hosszabb == 0:
    print('Nincs 2 óránál hosszabb film.')
else:
    print(f'{kettonel_hosszabb} film hosszabb, mint 2 óra.')
for i in range(db):
    if ertek[i] > 9:
        print('Van olyan film ami 9-es értékelésnél nagyobbat kapott.')
        break
else:
    print('Nincs olyan film ami 9-es értékelésnél nagyobbat kapott.')
print(f'A legmagasabb értékelés: {max(ertek)}')

rang = min(ertek)
rang_max = max(ertek)
bef = False
while not bef:
    szamlalo = 0
    for i in ertek:
        if i == rang:
            szamlalo += 1
        if szamlalo > 0:
            print(f'{rang}:\t{szamlalo} darab film')
        if rang == rang_max:
            bef = True
        rang = (rang*10+1)/10

legjobb = ertek[0]
rendezo = rendez[0]
for i in range(db):
    if ertek[i] > legjobb:
        legjobb = ertek[i]
        rendezo = rendez[i]
print(f'A legjobb filmet {rendezo} rendezte és {legjobb} pontos értékelést kapott')

us_rend = input('Adj meg egy rendezőt: ')
vezeteknev = []
for nevvagas in us_rend:
    fullnev = us_rend.strip().split()
vezeteknev = fullnev[-1].lower()
kimenet = open(f'fakt2025\\Csákai Bendegúz\\Python\\{vezeteknev}.txt', mode='w', encoding='utf-8')
for i in range(db):
    if rendez[i] == us_rend:
        print(f'{cim[i]} ({ev[i]}) - {hossz[i]} perc', file=kimenet)
kimenet.close()
print('9.feladat')

print(f'Az átlagos bevétel a filmeknél {sum(bevet)/db:,.0f} Ft')
print('11.feladat')
n = len(bevet)
for i in range(n-1):
  for j in range(n-i-1):
    if bevet[j] > bevet[j+1]:
      cim[j], cim[j+1] = cim[j+1], cim[j]

for i in range(1,11):
    print(f'\t{i}. {cim[-i]} ({bevet[-i]:,} Ft)')
print('12.feladat')