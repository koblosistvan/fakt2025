forras = open('Dobai Balint\\python\\covid.txt', mode ='r', encoding='utf-8')

datum = []
fertozott = []
halalozas = []

for sor in forras:
    adat= sor.strip().split(';')
    datum.append(str(adat[0]))
    fertozott.append(int(adat[1]))
    halalozas.append(int(adat[2]))

adatok_szama = len(datum)
print(f'{adatok_szama} nap adatai talalhatoak')

fertozott_osszeg = sum(fertozott)
print(f'a ket ev alatt fertozottek szama: {fertozott_osszeg}')
halalozas_osszeg = sum(halalozas)
print(f'a ket ev alatt elhunytak szama: {halalozas_osszeg}')

szazalatt = fertozott[0]
szazalatt_index = 0

for i in range(adatok_szama):
    if fertozott[i] < 100000:
        szazalatt_index +=1
print(f'{szazalatt_index}-szer volt ennyi alatt a fertozottek szama')

max_halal = halalozas[0]
max_halal_index = datum[0]
for i in range(adatok_szama):
    if halalozas[i] > max_halal:
        max_halal = halalozas[i]
        max_halal_index = datum[i]
print(f'a {max_halal_index}-adikai napon volt a legtobb elhunyt : {max_halal}')   

gyors = fertozott[0] / fertozott[0]
gyors_index = 0
for i in range(adatok_szama -1):
    if fertozott[i] / fertozott[i] > gyors:
        gyors = fertozott[i] / fertozott[i]
        gyors_index = i+1

print(f'a leggyorsabban a {gyors_index}-edik napon terjedt')


for i in range(adatok_szama - 1):
    for j in range(adatok_szama - 1-i):
        if fertozott[j] < fertozott[j+1]:
            datum[j] ,datum[j+1] = datum[j+1] , datum[j]
            fertozott[j] ,fertozott[j+1] = fertozott[j+1] , fertozott[j]
            halalozas[j] ,halalozas[j+1] = halalozas[j+1] , halalozas[j]

print(f'a megbetegedesi toplista:')
for i in range(5):
    print(f' {i+1} {datum[i]} : {fertozott[i]}') 
