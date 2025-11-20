forras = open("Törös Zétény\python\ökolábnyom.csv", mode="r", encoding="utf-8")
forras.readline()
kod = []
orszag = []
regio = []
ev = []
felhasznalas = []
kapacitas = []
lakossag = []
gdp = []
sorok = 0

for sor in forras:
    adat = sor.strip().split(',')
    sorok += 1
    kod.append(adat[0])
    orszag.append(adat[1])
    regio.append(adat[2])
    ev.append(int(adat[3]))
    felhasznalas.append(float(adat[4]))
    kapacitas.append(float(adat[5]))
    lakossag.append(int(adat[6]))
    if adat[7] == "None":
        gdp.append(0)
    else:
        gdp.append(float(adat[7]))
forras.close()
#1.feladat:
print("Az adatforrás {sorok} sort tartalmaz.")

#2.feladat:
adat2014 = 0

for i in range(sorok):
    if ev[i] == 2014:
        adat2014 += 1
print(f"2014-ről {adat2014} sort tartalmaz.")

#3.feladat:
print(f"Az adatok {min(ev)-max(ev)} közötti évekre vonatkoznak.")

#4.feladat:
legn_kap = 0
legn_kap_index = 0

for i in range(sorok):
    if kapacitas[i] > legn_kap:
        legn_kap = kapacitas[i]
        legn_kap_index = i
print(f"A legnagyobb kapacitású ország{orszag[legn_kap_index]}, melynek kapacitása: {legn_kap:.2f} hektár.")

#5.feladat:
legk_gdp = 999999999999999999999999999
legk_gdp_index = 0

for i in range(sorok):
    if gdp[i] != 0 and lakossag[i]/gdp[i] < legk_gdp:
        legk_gdp = lakossag[i]/gdp[i]
        legk_gdp_index = i

print(f"A legkisebb egy főre jutó GDP-je {orszag[legk_gdp_index+1]}-nak volt {ev[legk_gdp_index+1]} évben: {legk_gdp:.2f} USD/fő.")

#6.feladat:
fel2000 = 0
kap2000 = 0
lak2000 = 0
fel2014 = 0
kap2014 = 0
lak2014 = 0
index2000 = 0
index2014 = 0

for i in range(sorok):
    if ev[i] == 2000:
        fel2000 += felhasznalas[i]
        kap2000 += kapacitas[i]
        lak2000 += lakossag[i]
        index2000 += 1
    if ev[i] == 2014:
        fel2014 += felhasznalas[i]
        kap2014 += kapacitas[i]
        lak2014 += lakossag[i]
        index2014 += 1

print(f"A kapacitás 2000-től 2014-ig {kap2000}-ről {kap2014}-re változott, míg a felhasználás {fel2000}-ről {fel2014}-re")

#7.feladat:
ar2000 = fel2000/kap2000
ar2014 = fel2014/kap2014

if ar2000 < ar2014:
    print(f"A két érté aránya {ar2000*100:.0f}%-ról {ar2014*100:.0f}%-ra nőt.")
else:
    print(f"A két érté aránya {ar2000*100:.0f}%-ról {ar2014*100:.0f}%-ra csökkent.")

#8.feladat:
perfofel2000 = fel2000/lak2000
perfofel2014 = fel2014/lak2014

if perfofel2000 < perfofel2014:
    print(f"Az egy főre jutó átlagos felhasználás 2000-ben {perfofel2000:.2f} hektár volt, 2014-ra {perfofel2014:.2f}-re változott ami {(perfofel2014-perfofel2000)/perfofel2000:.2f}%-os növekedés")
if perfofel2000 > perfofel2014:
    print(f"Az egy főre jutó átlagos felhasználás 2000-ben {perfofel2000:.2f} hektár volt, 2014-re {perfofel2014:.2f}-re változott ami {(perfofel2000-perfofel2014)/perfofel2014:.2f}%-os csökkenés")

#9.feladat:
perfokap2000 = kap2000/lak2000
perfokap2014 = kap2014/lak2014

if perfokap2000 < perfokap2014:
    print(f"Az egy főre jutó átlagos kapacitás 2000-ben {perfokap2000:.2f} hektár volt, 2014-ra {perfokap2014:.2f}-re változott ami {(perfokap2014-perfokap2000)/perfokap2000:.2f}%-os növekedés")
if perfokap2000 > perfokap2014:
    print(f"Az egy főre jutó átlagos kapacitás 2000-ben {perfokap2000:.2f} hektár volt, 2014-re {perfokap2014:.2f}-re változott ami {(perfokap2000-perfofel2014)/perfokap2014:.2f}%-os csökkenés")
