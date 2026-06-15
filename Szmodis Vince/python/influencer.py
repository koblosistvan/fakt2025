forras = open('Szmodis Vince\\python\\influencer_format_a.txt', mode='r', encoding='utf-8')
adatok_szama=int(forras.readline())

datum=[]
cim=[]
megtekintes=[]
kedveles=[]
megosztas=[]
hozzaszolas=[]
ev=[]
honap=[]
nap=[]
cimtipus=[]

for sor in forras:
    adat=sor.strip().split('\t')
    datum.append(adat[0])
    cim.append(adat[1])
    megtekintes.append(int(adat[2]))
    kedveles.append(int(adat[3]))
    megosztas.append(int(adat[4]))
    hozzaszolas.append(int(adat[5]))
    dat = adat[0].strip().split('-')
    ev.append(int(dat[0]))
    honap.append(int(dat[1]))
    nap.append(int(dat[2]))
    tipus = adat[1].strip().split('_')
    cimtipus.append(tipus[0])

forras.close()

def f(n):
    print(f'\n{n}. feladat')

f(1)

febr_25=0
for i in range(adatok_szama):
    if ev[i]=='2025' and honap[i]=='02':
        febr_25+=1
print(f'{febr_25} poszt jelent meg 2025 februárjában')


f(2)
evhonapjai=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for _ in range(adatok_szama):
    atlag=((sum(evhonapjai[:honap[adatok_szama-1]])+nap[adatok_szama-1])-(sum(evhonapjai[:honap[0]])+nap[0]))/adatok_szama
    break
print(f'Két poszt között átlagosan {atlag:.2f} nap telik el')


f(3)

osszkedveles=0
febrkedveles=0
osszhozzaszolas=0
febrhozzaszolas=0

for i in range(adatok_szama):
    osszkedveles+=kedveles[i]
    osszhozzaszolas+=hozzaszolas[i]
    if honap[i]==2:
        febrkedveles+=kedveles[i]
        febrhozzaszolas+=hozzaszolas[i]

print(f'{osszkedveles/osszhozzaszolas:.3f} volt a teljes időszakra, \n{febrkedveles/febrhozzaszolas:.3f} volt februárra a kedvelések és hozzászólások aránya')

f(4)

maxmegosztas=0
maxindex=0

for i in range(adatok_szama):
    if maxmegosztas<megosztas[i]:
        maxmegosztas=megosztas[i]
        maxindex=i

print(f'A legtöbbet megosztott videó címe: {cim[maxindex]} aminek a megjelenési dátuma: {datum[maxindex]}')

f(5)

evhonapjai=[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
datho=int(input('And meg egy hónapot: '))
datnap=int(input('And meg egy napot: '))
datho2=int(input('And meg egy másik hónapot: '))
datnap2=int(input('And meg egy másik napot: '))

for _ in range(adatok_szama):
    if datho<1 or datho>12 or datho2<1 or datho2>12:
        break
    elif 0 != 2:
        print(f'A két dátum között {(sum(evhonapjai[:datho2])+datnap2)-(sum(evhonapjai[:datho])+datnap)} nap telik el')
        break

f(6)

maxtetlenseg=0
maxtetlenseg_index=0
for i in range(adatok_szama-1):
    if maxtetlenseg<(sum(evhonapjai[:honap[i+1]])+nap[i+1])-(sum(evhonapjai[:honap[i]])+nap[i]):
        maxtetlenseg =(sum(evhonapjai[:honap[i+1]])+nap[i+1])-(sum(evhonapjai[:honap[i]])+nap[i])
        maxtetlenseg_index=i
print(f'{maxtetlenseg} nap volt a maximális idő, amíg nem került fel poszt\nEz {datum[maxtetlenseg_index]} és {datum[maxtetlenseg_index+1]} között volt')

f(7)

for i in range(adatok_szama):
    if megtekintes[i]>100000 and megosztas[i]<1000:
        print('Volt olyan poszt, ami amely 100e-nél több megtekintést kapott, mégis 1000-nél kevesebb megosztást')
        break
else:
    print('Nem volt olyan poszt, ami amely 100e-nél több megtekintést kapott, mégis 1000-nél kevesebb megosztást')

f(9)

unboxing=0
osszmegtekintes=0
for i in range(adatok_szama):
    osszmegtekintes+=megtekintes[i]
    if cimtipus[i]== 'Unboxing':
        unboxing+=1
print(f'Összesen {unboxing*50000+osszmegtekintes*3.14} Ft-ot keresett az influencer')
