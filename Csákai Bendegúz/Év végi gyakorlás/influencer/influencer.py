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
    
poszt_februarban = 0
for i in honap:
    if i == 2:
        poszt_februarban += 1
print(f'Februári posztok száma: {poszt_februarban}')