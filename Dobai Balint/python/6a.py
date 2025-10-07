forras = open('Dobai Balint\\python\\6a-hallgatok.txt', mode = 'r', encoding='utf-8')

szul_ev = []
szul_honap = []
szul_nap = []
kezdes_eve = []
vegzes_eve = []
adatok_szama =int(forras .readline())


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