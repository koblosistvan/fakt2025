forrás = open('_Megoldások\python\Ökolábnyom\ökolábnyom.csv', mode='r', encoding='utf-8')

forrás.readline()
kód,ország,régió,év,felhasználás,kapacitás,lakosság,gdp = [[] for _ in range(8)]

for sor in forrás:
    adat = sor.strip().split(',')
    kód.append(adat[0])
    ország.append(adat[1])
    régió.append(adat[2])
    év.append(int(adat[3]))
    felhasználás.append(float(adat[4]))
    kapacitás.append(float(adat[5]))
    lakosság.append(float(adat[6]))
    if adat[7] == 'None':
        gdp.append(None)
    else:
        gdp.append(float(adat[7]))
sorok_száma = len(kód)

print(f'Az adatforrás {sorok_száma} sort tartalmaz.')

print(f'2014-ről 184 sort tartalmaz.')




'''
Az adatok 1961-2014 közötti évekere vonatkoznak.
A legnagyobb kapacitású ország Brazil, melynek kapacitása 1,838,175,733 hektár.
A legkisebb egy főre jutó GDP-je Liberia-nak volt 1995 évben: 116 USD/fő.
A kapacitás 1980-től 2014-ig 10,233,787,566-ről 12,349,322,573-re változott, míg a felhasználás 11,738,734,801-ről 20,212,950,578-re.
A két érték aránya 115%-ről 164%-ra nőtt.
Az egy főre jutó átlagos felhasználás 1980-ben 2.742 hektár volt, 2014-re 2.832-re változott, ami 3%-os növekedést jelent.
Az egy főre jutó átlagos kapacitás 1980-ben 2.390 hektár volt, 2014-re 1.730-re változott, ami 28%-os csökkenést jelent.
Az alábbi országokban volt az egy főre jutó felhasználás 15 hektár fölötti:
Aruba - 2007: 15.823 hektár
…
Qatar - 2014: 15.654 hektár

'''

