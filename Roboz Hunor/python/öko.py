forras = open('Roboz Hunor\\python\\ökolábnyom.csv', mode='r', encoding='utf-8')
forras.readline()
kód = []
ország=[]
régió = []
év= []
felh=[]
kapacitás = []
lakosság = []
gdp=[]
for sor in forras:
    adat = sor.strip().split(',')
    kód.append(adat[0])
    ország.append(adat[1])
    régió.append(adat[2])
    év.append(int(adat[3]))
    felh.append(float(adat[4]))
    kapacitás.append(float(adat[5]))
    lakosság.append(int(adat[6]))
    if adat[7] == 'None':
        gdp.append(adat[7])
    else: gdp.append(float(adat[7]))

print(f'Az adatforrás {len(év)} sort tartalmaz.')
kettoezertizennegy = 0
for i in range(len(év)):
    if év[i] == 2014:
        kettoezertizennegy +=1
print(f'2014-ről {kettoezertizennegy} sort tartalmaz.')
print(f'Az adatok {min(év)}-{max(év)} közötti évekere vonatkoznak.')

orszag = ország[0]
kap = 0
for  i in range(len(év)):
    if kapacitás[i] > kap:
        kap = kapacitás[i]
        orszag = ország[i]
print(f'A legnagyobb kapacitású ország {orszag}, melynek kapacitása {kap:,.0f} hektár.')

g = 0
for i in range(len(év)):
    if gdp[i] == 'None':
        continue
    else:
        if g < gdp[i] :
            g = gdp[i]
o = ország[0]
é = 0
for i in range(len(év)):
    if gdp[i] == 'None':
        continue
    else:
        if gdp[i] < g:
            g = gdp[i]
            o = ország[i]
            é = év[i]
print(f'A legkisebb egy főre jutó GDP-je {o}-nak volt {é} évben: {g:.0f} USD/fő.')


t_kap_2000 = 0
t_felh_2000=0
t_kap_2014 = 0
t_felh_2014=0
for  i in range(len(év)):
    if év[i] == 2000:
        t_kap_2000+=kapacitás[i]
        t_felh_2000+=felh[i]
    elif év[i] == 2014:
        t_kap_2014+=kapacitás[i]
        t_felh_2014+=felh[i]
print(f'A kapacitás 2000-től 2014-ig {t_kap_2000:,.0f}-ről {t_kap_2014:,.0f}-re változott, míg a felhasználás {t_felh_2000:,.0f}-ről {t_felh_2014:,.0f}-re.')

a = t_kap_2000/t_felh_2000*100
b = t_felh_2014/t_kap_2014*100

if a > b :
    c = 'csökkent'
else: c = 'nőtt'
print(f'A két érték aránya {a:.0f}%-ről {b:.0f}%-ra nőtt.')

