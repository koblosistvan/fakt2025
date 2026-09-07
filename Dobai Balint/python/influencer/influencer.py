forras=open("Dobai Balint\\python\\influencer\\influencer_format_a.txt", mode='r', encoding='utf-8')
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

for sor in forras:
    adat = sor.strip().split('\t')
    ev.append(str(adat[0].split('-')[0]))
    honap.append(str(adat[0].split('-')[1]))
    nap.append(str(adat[0].split('-')[2]))
    cim.append(str(adat[1]))
    megtekintes.append(int(adat[2]))
    kedveles.append(int(adat[3]))
    megosztas.append(int(adat[4]))
    hozzaszolas.append(int(adat[5]))

posztok_februarban = 0
for i in range(adatok_szama):
    if honap[i] =="02":
        posztok_februarban +=1
print(posztok_februarban)

teljes_kedveles = sum(kedveles)
print(f"A teljes kedvelesek szama:{teljes_kedveles}")

februar_kedveles = 0
for i in range(adatok_szama):
    if honap[i] == "02":
        februar_kedveles +=kedveles[i]

print(f"A februari kedvelesek szama:{februar_kedveles}")




