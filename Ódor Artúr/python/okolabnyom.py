forras = open("Ódor Artúr\\python\\ökolábnyom.csv", mode="r", encoding="utf-8")
forras.readline()

kod = []
orszag = []
regio = []
ev = []
felhaszn = []
kapacitas = []
lakossag = []
gdp = []

for sor in forras:
    adat = sor.strip().split(",")
    kod.append(adat[0])
    orszag.append(adat[1])
    regio