forras = open('fakt2025\\Roboz Hunor\\python\ökolábnyom.csv', mode='r', encoding='utf-8')
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


EV1, EV2 = 2000, 2014
t_kap_2000 = 0
t_felh_2000=0
t_kap_2014 = 0
t_felh_2014=0
for  i in range(len(év)):
    if év[i] == EV1:
        t_kap_2000+=kapacitás[i]
        t_felh_2000+=felh[i]
    elif év[i] == EV2:
        t_kap_2014+=kapacitás[i]
        t_felh_2014+=felh[i]
print(f'A kapacitás {EV1}-től {EV2}-ig {t_kap_2000:,.0f}-ről {t_kap_2014:,.0f}-re változott, míg a felhasználás {t_felh_2000:,.0f}-ről {t_felh_2014:,.0f}-re.')

a = t_kap_2000/t_felh_2000*100
b = t_felh_2014/t_kap_2014*100

if a > b :
    c = 'csökkent'
else: c = 'nőtt'
print(f'A két érték aránya {a:.0f}%-ről {b:.0f}%-ra {c}.')
/
+*-
t_fő_2000 = 0
t_fő_2014 = 0

for  i in range(len(év)):
    if év[i] == 2000:
        t_fő_2000+=lakosság[i]
    elif év[i] == 2014:
        t_fő_2014+=lakosság[i]
     
a = t_felh_2000/t_fő_2000*100
b = t_felh_2014/t_fő_2014*100
c = ''
if a<b:
    c = 'növekedést'

else: 
    c = 'csökkenést'
    a,b = t_felh_2014/t_fő_2014,t_felh_2000/t_fő_2000



print(f'Az egy főre jutó átlagos felhasználás {EV1}-ben {t_felh_2000/t_fő_2000:.3f} hektár volt, {EV2}-re {t_felh_2014/t_fő_2014:.3f}-re változott, ami {(b/a)*100-100:.0f}%-os {c} jelent')

a = t_kap_2000/t_fő_2000*100
b = t_kap_2014/t_fő_2014*100
c = ''
if a<b:
    c = 'növekedést'

else: 
    c = 'csökkenést'
    a,b = t_kap_2014/t_fő_2014,t_kap_2000/t_fő_2000

print(f'Az egy főre jutó átlagos kapacitás {EV1}-ben {t_kap_2000/t_fő_2000:.3f} hektár volt, {EV2}-re {t_kap_2014/t_fő_2014:.3f}-re változott, ami {(b/a)*100-100:.0f}%-os {c} jelent.')



érték = float(input('Add meg az értéket: '))
s = ''
for  i in range(len(év)):
    if érték < felh[i]/lakosság[i]:
        s += f'{ország[i]} - {év[i]}: {felh[i]/lakosság[i]:.3f} hektár\n'
print('Az alábbi országokban volt az egy főre jutó felhasználás 15 hektár fölötti:')
print(s)

db_orszag = set()
for  i in range(len(év)):
    db_orszag.add(ország[i])
print(f'Az adatok {len(db_orszag)} ország adatait tartalmazzák.')


legkisebb = 0
leg_o,leg_é = ország[0],év[0]


for  i in range(len(év)-1):
    if felh[i+1]-felh[i] > legkisebb and kód[i] == kód[i+1]:
        legkisebb= felh[i+1]-felh[i]
        a,b,leg_o,leg_é = felh[i], felh[i+1],ország[i],év[i]
print(f'A legnagyobb növekedés a felhasználás értékében {leg_o}-ban {leg_é}-ben történt: {a:,.0f} => {b:,.0f}.')

cs_o, cs_é= ország[0], év[0]
for  i in range(len(év)):
    if felh[i] > felh[i+1]:
        cs_o,cs_é = ország[i], év[i]
        break
print(f'{cs_o} felhasználása csökkent {cs_é} évről {cs_é+1} évre.')


