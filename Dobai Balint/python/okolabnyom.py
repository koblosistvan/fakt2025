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
    ev.append(int(adat[3]))
    felhaszn.append(float(adat[4]))
    kapac.append(float(adat[5]))
    lakossag.append(float(adat[6]))
    if adat[7] == 'NoneType':
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


kapac_legtobb = kapac[0]
kapac_legtobb_index = orszag[0]
for i in range(len(orszag)):
    if kapac[i] > kapac_legtobb:
        kapac_legtobb = kapac[i]
        kapac_legtobb_index = orszag[i]

print(f'a legnagyobb kapacitasu orszag {kapac_legtobb_index}, melynek a kapacitasa {kapac_legtobb}')


gdp_legkisebb = gdp[0]
gdp_legkisebb_index = orszag[0]
gdp_legkisebb_eve = ev[0]
for i in range(len(orszag)):
    if gdp[i] < gdp_legkisebb:
        gdp_legkisebb = gdp[i]
        gdp_legkisebb_index = orszag[i]
        gdp_legkisebb_eve = ev[i]

print(f'a legkisebb egy fore juto gdp orszaga {gdp_legkisebb_index} {gdp_legkisebb_eve}-ben, melynek {gdp_legkisebb}')

ossz_kapac1 = 0
ossz_kapac2 = 0

ossz_felhasz1 = 0
ossz_felhasz2 = 0

ossz_lakos1 = 0
ossz_lakos2 = 0

for i in range(len(orszag)):
    if ev[i] == 2000:
        ossz_kapac1 += kapac[i]
        ossz_felhasz1 += felhaszn[i]
        ossz_lakos1 += lakossag[i]
    elif ev[i] == 2014:
        ossz_kapac2 += kapac[i]
        ossz_felhasz2 += felhaszn[i]
        ossz_lakos2 += lakossag[i]

print(f'2000-ben a kapacitas osszege {ossz_kapac1:,.3f}')
print(f'2014-ben a kapacitas osszege {ossz_kapac2:,.3f}')


kapac_arany = ossz_felhasz2 / ossz_kapac2
felhaszn_arany = ossz_felhasz1 / ossz_kapac1
egyfore_felhasznalas_arany = (ossz_felhasz1 / ossz_lakos1) / (ossz_felhasz2 / ossz_lakos2)
print(f'A ket ertek aranya {felhaszn_arany*100:.0f}%-rol {kapac_arany*100:.0f}%-ra nott')
print(f'Az egy fore juto felhasznalas 2000-ben {ossz_felhasz1 / ossz_lakos1:.3f} hektar, 2014-re {ossz_felhasz2 / ossz_lakos2:.3f} hektar lett')
print(f'Az egy fore juto kapacitas 2000-ben {ossz_kapac1 / ossz_lakos1}, 2014-ben {ossz_kapac2 / ossz_lakos2}')



