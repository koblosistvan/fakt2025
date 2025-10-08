forras = open('Törös Zétény\\6a-hallgatok.txt', mode='r', encoding='utf-8')

szul_ev = []
szul_ho = []
szul_nap = []
kezdes_ev = []
vegzes_ev = []

adatok_szama = int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    szul_ev.append(int(adat[0]))
    szul_ho.append(int(adat[1]))
    szul_nap.append(int(adat[2]))
    kezdes_ev.append(int(adat[3]))
    vegzes_ev.append(int(adat[4]))

elet_kor = int(input('Add meg az életkorod: '))
for i in range(adatok_szama):
    kor = vegzes_ev[i] - szul_ev[i]
    if kor < elet_kor:
        print(f'Van {elet_kor} nél fiatalabb végzet')
        break
else:
    print('Bocsi de nincs ilyen ember')