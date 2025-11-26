forras = open("Ódor Artúr\\python\\imdb.txt", mode="r", encoding="utf-8")
forras.readline()
ev = []
idotartam = []
ertekeles = []
rendezo = []
bevetel = []
cim = []
for sor in forras:
    adat= sor.strip().split("\t")
    ev.append(int(adat[0]))
    idotartam.append(int(adat[1]))
    ertekeles.append(float(adat[2]))
    rendezo.append(adat[3])
    bevetel.append(int(adat[4]))
    cim.append(adat[5])
forras.close()
print()

allomany = len(ev)
print(f"{allomany} film van az állományban")
print(f"Az első film {min(ev)}-ben jelent meg")

ket_o_sz = 0
for i in idotartam:
    if i >= 120:
        ket_o_sz += 1
if ket_o_sz == 0:
    print("Nincs 2 óránál hosszabb film")
else:
    print(f"{ket_o_sz} darab 2 óránál hosszabb film van.")
    
for i in ertekeles:
    if i > 9:
        print("Van olyan film ami 9-es értékelésnél jobbat kapott.")
    break
else:
    print("Nincs olyan film ami 9-esnél jobb értékelést kapott")
print(f"A legmagasabb értékelés: {max(ertekeles)}")

rang = min(ertekeles)
rang_max = max(ertekeles)
befejezve = False
while not befejezve:
    szamlalo = 0
    for i in ertekeles:
        if i == rang:
            szamlalo += 1
    if szamlalo > 0:
        print(f"{rang}:\t{szamlalo} darab film")
    if rang == rang_max:
        befejezve = True
    rang = (rang*10+1)/10
    
k_rendezo = input("Keresett rendező: ")

forras = open(f"Ódor Artúr\\python\\{k_rendezo}.txt", mode= "w", encoding="utf-8")
for i in range(allomany):
    if k_rendezo == rendezo[i]:
        print(cim[i], file=forras)
forras.close()