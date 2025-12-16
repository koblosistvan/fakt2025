def fe(n):
    print(f"\n{n}. feladat")

ora = []
perc = []
mp = []
ido = []
seb = []
rendszam = []
with open(r"Ódor Artúr\python\kozut\kozut.txt", mode="r", encoding="utf-8") as f:
    adatok_sz = int(f.readline())
    for sor in f:
        adat = sor.strip().split(" ")
        ora.append(int(adat[0]))
        perc.append(int(adat[1]))
        mp.append(int(adat[2]))
        ido.append(int(adat[0])*3600 + int(adat[1])*60 + int(adat[2]))
        seb.append(int(adat[3]))
        rendszam.append(adat[4])

fe(1)
gyorsh = 0
for a in seb:
    if a>50:
        gyorsh +=1
print(f"{gyorsh} autós hajtott gyorsabban a megengedetnél.")

fe(2)
for a in seb:
    if a > 50:
        print("Volt olyan autó ami gyorsabban ment, mint 55 km/h")
        break
else:
    print("Nem volt olyan autó ami gyorsabban ment volna, mint 55 km/h")
    
fe(3)
leggy_rendszam = 0
leggy_seb = 0
for i in range(adatok_sz):
    if seb[i] > leggy_seb:
        leggy_seb = seb[i]
        leggy_rendszam = rendszam[i]
print(f"A leggyorsabban hajtó autórendszáma: {leggy_rendszam} \tés sebessége: {leggy_seb}")

fe(4)
print(f"Az áthaladó autók átlagsebessége: {sum(seb) / adatok_sz:.2f} km/h")

fe(5)
fajl_nev = "kozut-kimenet"
with open(fr"Ódor Artúr\python\kozut\{fajl_nev}.txt", mode="w", encoding="utf-8") as f:
    for i in range(adatok_sz):
        if seb[i] < 30:
            print(f"{ora[i]}:{perc[i]}:{mp[i]}\t{rendszam[i]}\t{seb[i]}", file= f)
print(f"A 30 km/h-nál lassabb autók adatai eltárolva a {fajl_nev} fájlban")

fe(7)
for i in range(adatok_sz-1):
    if seb[i] > 90 and seb[i+1] > 90:
        print("Volt olyan hogy egymásután többen 90-nél többel mentek.")
        break
else:
    print("Nem volt olyan hogy egymásután többen 90-nél többel mentek volna")


fe(6)
fajl_nev="kozut-rendezett"
with open(fr"Ódor Artúr\python\kozut\{fajl_nev}.txt", mode="w", encoding="utf-8") as f:
    kezd =0
    bef = adatok_sz-1
    while kezd < bef:
        for i in range(kezd, bef):
            if rendszam[i] > rendszam[i+1]:
                rendszam[i], rendszam[i+1]=rendszam[i+1], rendszam[i]
                ora[i], ora[i+1]=ora[i+1], ora[i]
                perc[i],perc[i+1]=perc[i+1], perc[i]
                mp[i], mp[i+1]=mp[i+1], mp[i]
                seb[i], seb[i+1]=seb[i+1],seb[i]
        bef-=1    
        for i in range(bef, kezd, -1):
            if rendszam[i] < rendszam[i-1]:
                rendszam[i], rendszam[i-1] = rendszam[i-1], rendszam[i]
                ora[i], ora[i-1]=ora[i-1], ora[i]
                perc[i],perc[i-1]=perc[i-1], perc[i]
                mp[i], mp[i-1]=mp[i-1], mp[i]
                seb[i], seb[i-1]=seb[i-1],seb[i]
        kezd += 1
    for i in range(adatok_sz):
        if seb[i] > 50:
            print(f"{ora[i]}:{perc[i]}:{mp[i]}\t{rendszam[i]}\t{seb[i]}", file= f)

print(f"Az 50 km/h-nál gyorsabb autók adatai eltárolva a {fajl_nev} fájlban")


fe(8)
tobbszor_ath = []
ilyen_ido = []
for i in range(adatok_sz):
    if rendszam[i] not in tobbszor_ath:
        for n in range(i+1, adatok_sz):
            if rendszam[i] == rendszam[n]:
                tobbszor_ath.append(rendszam[i])
                break
for i in range(len(tobbszor_ath)):
    print(f"Rendszám {tobbszor_ath[i]}\nIdőpontok:")
    for n in range(adatok_sz):
        if tobbszor_ath[i] == rendszam[n]:
            print(f"{ora[n]}:{perc[n]}:{mp[n]}\t",end="")
    print("\n")
    
fe(9)

fe(10)
for a in rendszam:
    if len(a)== 9:
        print("Van új rendszám formátumú autó az adatokban")
        break
else:
    print("nincs új rendszám formátumú autó az adatokban.")