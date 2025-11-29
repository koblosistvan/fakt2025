forras = open("_Feladatok\\python\\CS\\cs.csv", mode="r", encoding="utf-8")
print()
import time
ido_s = time.time()
idopont = []
palya = []
csapat = []
pont = []
pont_kulonbseg = []
eredmeny = []
forras.readline()
for sor in forras:
    if len(idopont) == 1000:
        break
    adat = sor.strip().split(";")
    idopont.append(adat[0])
    palya.append(adat[1])
    csapat.append(adat[2])
    pont.append(int(adat[3]))
    pont_kulonbseg.append(int(adat[4]))
    eredmeny.append(adat[5])
forras.close()
print(f"{len(csapat) / 2:.0f} meccs adatai vannak az állományban")

print(f"Az első meccs ekkor volt: {min(idopont)}")

"""for i in range(len(pont_kulonbseg)):
    for n in range(len(pont_kulonbseg)-i-1):
        if pont_kulonbseg[n] < pont_kulonbseg[n+1]:
            pont_kulonbseg[n], pont_kulonbseg[n+1] = pont_kulonbseg[n+1], pont_kulonbseg[n]
            idopont[n], idopont[n+1] = idopont[n+1], idopont[n]
            palya[n], palya[n+1] = palya[n+1], palya[n]
            csapat[n], csapat[n+1] = csapat[n+1], csapat[n]
            pont[n], pont[n+1] = pont[n+1], pont[n]
            eredmeny[n], eredmeny[n+1]=eredmeny[n+1], eredmeny[n]"""

kezd = 0
bef = len(pont_kulonbseg) - 1

while kezd < bef:
    for n in range(kezd, bef):
        if pont_kulonbseg[n] > pont_kulonbseg[n + 1]:
            pont_kulonbseg[n], pont_kulonbseg[n+1] = pont_kulonbseg[n+1], pont_kulonbseg[n]
            idopont[n], idopont[n+1] = idopont[n+1], idopont[n]
            palya[n], palya[n+1] = palya[n+1], palya[n]
            csapat[n], csapat[n+1] = csapat[n+1], csapat[n]
            pont[n], pont[n+1] = pont[n+1], pont[n]
            eredmeny[n], eredmeny[n+1]=eredmeny[n+1], eredmeny[n]
    bef -= 1

    for n in range(bef, kezd, -1):
        if pont_kulonbseg[n] < pont_kulonbseg[n - 1]:
            pont_kulonbseg[n], pont_kulonbseg[n-1] = pont_kulonbseg[n-1], pont_kulonbseg[n]
            idopont[n], idopont[n-1] = idopont[n-1], idopont[n]
            palya[n], palya[n-1] = palya[n-1], palya[n]
            csapat[n], csapat[n-1] = csapat[n-1], csapat[n]
            pont[n], pont[n-1] = pont[n-1], pont[n]
            eredmeny[n], eredmeny[n-1]=eredmeny[n-1], eredmeny[n]
    kezd += 1



      
print(f"Összesen: {len(set(palya))} pálya van")

sz_meccs = 0
w = 0
l = 0
d = 0
max_pontk = 0
min_pontk = max(pont_kulonbseg)
atlag = 0
for i in range(len(idopont)):
    if csapat[i] == "Extra Salt":
        sz_meccs += 1
        if eredmeny[i] == "vereség":
            l += 1
        elif eredmeny[i] == "döntetlen":
            d += 1
        elif eredmeny[i] == "győzelem":
            w += 1
        if max_pontk < abs(pont_kulonbseg[i]):
            max_pontk = pont_kulonbseg[i]
        if abs(pont_kulonbseg[i]) < min_pontk:
            min_pontk = pont_kulonbseg[i]
        atlag += pont_kulonbseg[i]
print(f"{sz_meccs} meccset játszott az Extra Salt")
print(f"{w} alkalommal nyert\n{l} alkalommal vesztett\n{d} alkalommal játszott döntetlent")
print(f"A legnagyobb pontkülönbségük {max_pontk} pont volt\nA legkissebb pontkülönbségük {min_pontk} pont volt")
print(f"A pontkülönbség átlag {atlag/sz_meccs:.2f}")

vege = time.time()
print(vege-ido_s)