forras = open('fakt2025\\Csákai Bendegúz\\Év végi gyakorlás\\influencer\\influencer_format_a.txt', mode='r', encoding='utf-8')
db = int(forras.readline())
datum = []
ev = []
honap = []
nap = []
poszt = []
megt_db = []
kedv_db =  []
oszt_db = []
hozzsz_db = []
for sor in forras:
    adat = sor.strip().split('\t')
    datum.append(adat[0])
    poszt.append(adat[1])
    megt_db.append(int(adat[2]))
    kedv_db.append(int(adat[3]))
    oszt_db.append(int(adat[4]))
    hozzsz_db.append(int(adat[5]))
for d in datum:
    adat = d.strip().split('-')
    ev.append(int(adat[0]))
    honap.append(int(adat[1]))
    nap.append(int(adat[2]))
forras.close()
def f(n):
    print(f'\n{n}. feladat \n')
f(1)
print('Az adatokat sikeresen beolvastam')    
f(2)
poszt_februarban = 0
for i in honap:
    if i == 2:
        poszt_februarban += 1
print(f'Februári posztok száma: {poszt_februarban}')
f(3)
'''for i in range(len(nap)):
'''
f(4)
telj_arany = sum(kedv_db)/sum(hozzsz_db)
febr_kedv = []
febr_hozz = []
for i in range(len(honap)):
    if honap[i] == 2:
        febr_kedv.append(kedv_db[i])
        febr_hozz.append(hozzsz_db[i])
febr_arany = sum(febr_kedv)/sum(febr_hozz)
print(f'A teljes időszakra az arány: {telj_arany}')
print(f'A februári időszakra az arány:{febr_arany}')
f(5)
max_mego = oszt_db[0]
max_mego_ind = 0
for i in range(len(oszt_db)):
    if oszt_db[i] > max_mego:
        max_mego = oszt_db[i]
        max_mego_ind = i
print(f'A legtöbb megosztással rendelkező bejegyzés a(z) {poszt[max_mego_ind]} volt {datum[max_mego_ind]} dátummal')
'''
f(6)
d1 = input('Add meg az 1. dátumot (kötőjellel elválasztva pl.: 1999-01-01): ')
d2 = input('Add meg az 2. dátumot (kötőjellel elválasztva pl.: 1999-01-01): ')
ad = d1.strip().split('-')
ad2 = d2.strip().split('-')
d1ev,d1ho,d1nap = ad[0], ad[1], ad[2]
d2ev, d2ho, d2nap = ad2[0], ad2[1], ad2[2]
datum = str()
print(f'')
'''
f(7)
f(8)
for i in range(db):
    if megt_db[i] > 100000 and oszt_db[i] < 1000:
        print('Volt ilyen eset')
        break
else:
    print('Nem volt ilyen eset')
f(9)
for i in range(db):
    for j in range(db-i-1):
        if megt_db[i] < megt_db[i+1]:
            megt_db[i], megt_db[i+1] = megt_db[i+1], megt_db[i]
            oszt_db[i], oszt_db[i+1] = oszt_db[i+1], oszt_db[i]
            datum[i], datum[i+1] = datum[i+1], datum[i]
            poszt[i], poszt[i+1] = poszt[i+1], poszt[i]
            kedv_db[i], kedv_db[i+1] = kedv_db[i+1], kedv_db[i]
            hozzsz_db[i], hozzsz_db[i+1] = hozzsz_db[i+1], hozzsz_db[i]
kimenet = forras = open('fakt2025\\Csákai Bendegúz\\Év végi gyakorlás\\influencer\\indluencer-kimenet.txt', mode='w', encoding='utf-8')
for i in range(10):
    print(f'{i+1}. {poszt[i]}', file=kimenet)