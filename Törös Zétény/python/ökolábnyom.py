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