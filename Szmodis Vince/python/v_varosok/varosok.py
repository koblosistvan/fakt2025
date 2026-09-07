forras = open('Szmodis Vince\\python\\v_varosok\\varosok_gps_format_d.txt', mode='r', encoding='utf-8')
adatok_szama = int(forras.readline())

nev = []
lakosok_szama = []
hosszusag = []
szelesseg = []
rang_ideje = []


for sor in forras:
    adat=sor.strip().split(';')
    nev.append(adat[0])
    lakosok_szama.append(int(adat[1]))
    hosszusag.append(float(adat[2]))
    szelesseg.append(float(adat[3]))
    rang_ideje.append(int(adat[4]))

def f(n):
    print(f'\n{n}. feladat')

f(1)

szazezer_tobb_lista=[]
for i in range(adatok_szama):
    if lakosok_szama[i]>100000:
        szazezer_tobb_lista.append(f'{nev[i]} - {lakosok_szama[i]:_}')
        
print(szazezer_tobb_lista)
        
f(2)
legkeletibb = ' '
legkeletibb_fok=0
for i in range(adatok_szama):
    if hosszusag[i]>legkeletibb_fok:
        legkeletibb_fok=hosszusag[i]
        legkeletibb=nev[i]

print(f'{legkeletibb} van legkeletebbre.')

f(3)
legregebbi=rang_ideje[0]
legregebbi_index=0
for i in range(adatok_szama):
    if legregebbi>rang_ideje[i]:
        legregebbi=rang_ideje[i]
        legregebbi_index=i

print(f'{nev[legregebbi_index]} a legrégebbi városunk')

f(4)
osszlakossag=0
szazezer_tobb_lakos=0
for i in range(adatok_szama):
    osszlakossag+=lakosok_szama[i]
    if lakosok_szama[i]>100000:
        szazezer_tobb_lakos+=lakosok_szama[i]
print(f'{(szazezer_tobb_lakos/osszlakossag*100)} % él nagy városokban')

f(5)
varban=[]
var='var'
for i in range(adatok_szama):
    if var in nev[i]:
        varban.append(nev[i])
print(varban) 