forras = open("Törös Zétény\python\ökolábnyom.csv", mode="r", encoding="utf-8")

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
    kod.append(int(adat[0]))
    orszag.append(int(adat[1]))
    regio.append(int(adat[2]))
    ev.append(int(adat[3]))
    felhasznalas.append(int(adat[4]))
    kapacitas.append(int(adat[5]))
    lakossag.append(int(adat[6]))
    gdp.append(int(adat[7]))
forras.close()

print()