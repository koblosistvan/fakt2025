forras = open('Dobai Balint\\python\\ökolábnyom.csv', mode ='r', encoding='utf-8')

kod = []
orszag = []
regio = []
ev = []
felhaszn = []
kapac = []
lakossag = []
gdp = []

for sor in forras:
    adat = sor.strip().split(',')
    kod.append(adat[0])
    orszag.append(adat[1])
    regio.append(adat[2])
    ev.append((adat[3]))
    felhaszn.append((adat[4]))
    kapac.append((adat[5]))
    lakossag.append((adat[6]))
    gdp.append((adat[7]))

print(orszag)
