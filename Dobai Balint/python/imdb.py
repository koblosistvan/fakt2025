forras = open('Dobai Balint\\python\\imdb.txt', mode ='r', encoding='utf-8')
forras.readline()

ev = []
idotartam = []
ertekeles = []
rendezo = []
bevetel = []
cim =[]

for sor in forras:
    adat = sor.strip().split('\t')
    ev.append(int(adat[0]))
    idotartam.append(int(adat[1]))
    ertekeles.append(float(adat[2]))
    rendezo.append((adat[3]))
    bevetel.append(int(adat[4]))
    cim.append((adat[5]))
forras.close()

filmek_szama = len(ev)
print(f'a filmek szama a tartomanyban : {filmek_szama}')

legregebbi = ev[0]
legjobb_ertekeles = ertekeles[0]
tobb_ketora = 0
jobbmint_kilenc = 0
for i in range(filmek_szama):
    if ev[i] < legregebbi:
        legregebbi = ev[i]
    if idotartam[i] > 120:
        tobb_ketora +=1
    if ertekeles[i] > 9:
        jobbmint_kilenc +=1
    if ertekeles[i] > legjobb_ertekeles:
        legjobb_ertekeles = ertekeles[i]

print(f'az elso film {legregebbi}-ban jelent meg')
print(f'{tobb_ketora} db film van ami 2 oranal hosszabb')
print(f'{jobbmint_kilenc} db olyan film van ami kilencnel jobb ertekelest kapott')
print(f'a legmagasabbra ertekelt film : {legjobb_ertekeles}')


