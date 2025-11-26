forras = open('Dobai Balint\\python\\cs.csv', mode ='r', encoding='utf-8')
forras.readline()
idopont = []
palya = []
csapat = []
pont = []
pont_kul = []
eredmeny = []

for sor in forras:
    adat = sor.strip().split(';')
    idopont.append(str(adat[0]))
    palya.append(str(adat[1]))
    csapat.append(str(adat[2]))
    pont.append(int(adat[3]))
    pont_kul.append(int(adat[4]))
    eredmeny.append(str(adat[5]))
    if len(idopont) == 1000:
        break
forras.close()


adatok_szama = len(csapat)
adat2 = len(csapat) / 2
print(f'az allomany ban {adat2:.0f} meccs adatai vannak')
print(f'az elso meccs {min(idopont)} -kor volt')

for i in range(adatok_szama-1):
    print(f'{i/adatok_szama*100:.2f}%')
    for j in range(adatok_szama-1-i):
        if pont[j] < pont[j+1]:
            pont[j], pont[j+1] = pont[j+1] , pont[j]
            csapat[j], csapat[j+1] = csapat[j+1] , csapat[j]
print('pont szerint a toplista :')
for i in range(5):
    print(f' {i+1} : {csapat[i]} {pont[i]} ponttal')

palyak = []
for i in range(adatok_szama):
    if palya[i] not in palyak:
        palyak.append(palya[i])
print(f'Ezeken a palyakon jatszottak : {palyak}')

es_meccs = 0
es_nyert = 0
es_vesztett = 0
es_dontetlen = 0 
for i in range(adatok_szama):
    if csapat[i] == 'Extra Salt':
        es_meccs +=1
        if eredmeny[i] == 'győzelem':
            es_nyert +=1
        if eredmeny[i] == 'vereség':
            es_vesztett +=1
        if eredmeny[i] == 'döntetlen':
            es_dontetlen +=1
print(f'Az Extra Salt csapat {es_meccs} db meccset jatszott, melybol {es_nyert} db gyozelem, {es_vesztett} vereseg es {es_dontetlen} dontetlen volt')

for i in range(adatok_szama):
    if csapat[i] == 'Extra Salt':
        print(f'A csapat legnagyobb pontkulonbsege : {max(pont_kul)}, a legkisebb pedig {min(pont_kul)}')
        break


for i in range(adatok_szama):
    if csapat[i] == 'Extra Salt':
        pk_osszeg = sum(pont_kul)
        pk_atlag = pk_osszeg / len(pont_kul)    
print(f'{pk_atlag*10.:.1f}')













