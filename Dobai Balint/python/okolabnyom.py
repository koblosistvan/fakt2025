forras = open('Dobai Balint\\python\\ökolábnyom.csv', mode ='r', encoding='utf-8')
forras.readline()

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
    felhaszn.append(float(adat[4]))
    kapac.append(float(adat[5]))
    lakossag.append(float(adat[6]))
    if adat[7] == 'None':
        gdp.append(None)
    else:
        gdp.append((adat[7]))
forras.close()

adatsor = len(kod)
print(f'{adatsor} db sort tartalmaz')

adott = 0
for i in range(len(kod)):
    if ev[i] == 2014:
        adott 

print(adott)

elso = min(ev)
utols = max(ev)
print(f'az adatok {elso} és {utols} közöttről vannak')


gdp_legtobb = gdp[0]
gdp_legtobb_index = orszag[0]
for i in range(len(orszag)):
    if gdp[i] > gdp_legtobb:
        gdp_legtobb = gdp[i]
        gdp_legtobb_index = orszag[i]

print(f'a legnagyobb kapacitasu orszag {gdp_legtobb_index}, melynek a kapacitasa {gdp_legtobb}')



