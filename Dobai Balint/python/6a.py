forras = open('Dobai Balint\\python\\6a-hallgatok.txt', mode = 'r', encoding='utf-8')

szul_ev = []
szul_honap = []
szul_nap = []
kezdes_eve = []
vegzes_eve = []
adatok_szama =int(forras .readline())

diakok_szama = len(szul_ev)


for sor in forras:
    adat = sor.strip().split(' ')
    szul_ev.append(int(adat[0]))
    szul_honap.append(int(adat[1]))
    szul_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    vegzes_eve.append(int(adat[4]))

eletkor = int(input('adj meg egy eletkort'))
for i in range(adatok_szama):
    kor = vegzes_eve[i] - szul_ev[i]
    if kor < eletkor:
        print(f'Van {eletkor} evnel fiatalabban vegzet')
        break
else:
    print('nincs ilyen ember')

bek_ev = int(input('melyik evben szulettel?'))
bek_honap = int(input('even belul melyik honapban szulettel?'))
bek_nap = int(input('melyik napon szulettel?'))


for i in range(adatok_szama):
    if bek_ev == szul_ev[i] and bek_honap == szul_honap[i] and bek_nap == szul_nap[i]:
        print('van a tieddel megegyezo szulinap')
        break
else:
    print('nincs ilyen szulinap')


legfiatalabb = vegzes_eve[0] - szul_ev[0]
legfigatalabb_index = 0

# for i in range(adatok_szama):
#     if legfiatalabb > vegzes_eve[i] - szul_ev[i]:
#          legfiatalabb = vegzes_eve[i] - kezdes_eve[i]
#          legfigatalabb_index = i

# print(f'a legfiatalabban vegzett hallgato {legfigatalabb_index}, {legfiatalabb} evesen')


vmikor_vegzett = 0
for i in range(adatok_szama):
    if vegzes_eve[i] == 2016:
        vmikor_vegzett +=1
print(f'{vmikor_vegzett} tanulo vegzett 2016-ban')



#hazi 2023/24 okt 1 fordulo programozoi



