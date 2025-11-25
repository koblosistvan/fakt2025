forras = open("_Feladatok\\python\\CS\\cs.csv", mode="r", encoding="utf-8")
idopont = []
palya = []
csapat = []
pont = []
pont_kulonbseg = []
eredmeny = []
forras.readline()
for sor in forras:
    adat = sor.strip().split(";")
    idopont.append(adat[0])
    palya.append(adat[1])
    csapat.append(adat[2])
    pont.append(int(adat[3]))
    pont_kulonbseg.append(int(adat[4]))
    eredmeny.append(adat[5])
forras.close()
print(f"{len(csapat) / 2:.0f} meccs adatai vannak az állományban")

for a in idopont:vvv
    b = a.strip().split(" ")