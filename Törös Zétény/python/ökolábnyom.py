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

print(f"Ennyi adatsort tartalmaz a fájl: {sorok}")

hany = 0

for i in range(sorok):
    if ev[i] == 2024:
        hany += 1

print(f"Ennyi adat van 2014-ből: {hany}")
print(f"Az adatok {min(ev)}-től {max(ev)}-ig vannak mérve.")

legn_kap = 0
legn_kap_index = 0

for i in range(sorok):
    if kapacitas[i] > legn_kap:
        legn_kap = kapacitas[i]
        legn_kap_index = i

print(f"A legnagyobb kapacitása {orszag[legn_kap_index]}-nak van és a kapacitása: {kapacitas[legn_kap_index]}")

legk_gdp = 0
legk_gdp_index = 0

for i in range(sorok):
    if legk_gdp < gdp[i]:
        legk_gdp = gdp[i]
        legk_gdp_index = i

print(f"Egy főre jutó legkisebb gdp-je {orszag[legk_gdp_index]}-ban/ben volt és ez {ev[legk_gdp_index]}-ban/ben történt.")

kap2000 = 0 
fel2000 = 0
kap2014 = 0
fel2014 = 0
for i in range(sorok):
    if ev[i] == 2000:
        kap2000 += kapacitas[i]
        fel2000 += felhasznalas[i]
    if ev[i] == 2014:
        kap2014 += kapacitas[i]
        fel2014 += felhasznalas[i]

print(f"2000-ben a kapacitás: {kap2000} volt és a felhasználás: {fel2000} 2014-ben a kapacitás: {kap2014} és a felhasználás: {fel2014}.")