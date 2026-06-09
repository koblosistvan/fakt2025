forras = open('Roboz Hunor\\python\\influencer_format_a.txt')
hossz = int(forras.readline().strip())
év,honap,nap,cím,megtekintések_száma,kedvelések_száma,megosztások_száma,hozzászólások_száma = [],[],[],[],[],[],[],[]

datum = []

for sor in forras:
    adat = sor.strip().split('\t')
    datum.append(adat[0])
    cím.append(adat[1])
    megtekintések_száma.append(int(adat[2]))
    kedvelések_száma.append(int(adat[3]))
    megosztások_száma.append(int(adat[4]))
    hozzászólások_száma.append(int(adat[5]))

for sor in datum:
    adat = sor.split('-')
    év.append(int(adat[0]))
    honap.append(int(adat[1]))
    nap.append(int(adat[2]))

febr_25 = ''

for i in range(hossz):
    if év[i] == 2025:
        if honap[i] == 2:
            febr_25 += f'{datum[i]}\n'


print(febr_25)


