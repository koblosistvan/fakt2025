forras = open('Csákai Bendegúz\\Python\\covid.txt', mode='r', encoding='utf-8')
datum = []
napi_fert_szama = []
halalozasok_szama = []
for sor in forras:
    adat = sor.strip().split(';')
    datum.append(adat[0])
    napi_fert_szama.append(int(adat[1]))
    halalozasok_szama.append(int(adat[2]))
forras.close()
print('1. feladat')
print(f'Az állomány {len(datum)} nap adatait tartalmazza.''\n')
print('2. feladat')
print(f'A két év alatt összesen {sum(napi_fert_szama):,} fertőzöttet és {sum(halalozasok_szama):,} halottat regisztráltak.''\n')
print('3. feladat')
szaze_alatt = 0
for i in range(len(datum)):
    if napi_fert_szama[i] < 100000:
        szaze_alatt += 1
print(f'A fertőzöttek száma {szaze_alatt} napon volt 100e alatt.''\n')
print('4. feladat')
halott_legt = 0
datuma = 0
fert_ez = 0
for i in range(len(datum)):
    if halalozasok_szama[i] > halott_legt:
        halott_legt = halalozasok_szama[i]
        datuma = datum[i]
        fert_ez = napi_fert_szama[i]
print(f'Legtöbben {datuma} napon haltak meg:''\n''\t'f'{fert_ez:,} fertőzött''\n''\t'f'{halott_legt:,} halott')
print('5. feladat')
arany_fert_dat = []
arany = 0
for i in range(len(datum)):
    if napi_fert_szama[i]/napi_fert_szama[i] > arany:
        arany_fert_dat = datum[i]
        arany = napi_fert_szama[i]/napi_fert_szama[i-1]
print(f'A legnagyobb arányú növekedés {arany_fert_dat} napon volt, amikor az előző napi adat {arany:.2f}-szorosa volt a fertőzöttek száma.''\n')
print('6. feladat')
csokk = 0
nott = 0
for i in range(len(datum)):
    if halalozasok_szama[i] > halalozasok_szama[i-1]:
        nott+=1
    elif halalozasok_szama[i] < halalozasok_szama[i-1]:
        csokk+=1
print(f'A halálozások száma {csokk-1} napon csökkent és {nott} napon nőtt az előzőhöz képest.''\n')
print('7. feladat')
print(f'A napi halálozások átlagos száma {sum(halalozasok_szama)/len(halalozasok_szama):,.1f}')