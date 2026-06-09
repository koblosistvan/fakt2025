forras = open('Szmodis Vince\\python\\influencer_format_a.txt', mode='r', encoding='utf-8')
forras.readline()

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
    adat=sor.strip().split('\t')
    datum.append(adat[0])
    cim.append(adat[1])
    megtekintes.append(adat[2])
    kedveles.append(adat[3])
    megosztas.append(adat[4])
    hozzaszolas.append(adat[5])
    dat = adat[0].strip().split('-')
    ev.append(dat[0])
    honap.append(dat[1])
    nap.append(dat[2])

forras.close()


