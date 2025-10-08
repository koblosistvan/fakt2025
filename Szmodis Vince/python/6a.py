forras = open('Szmodis Vince\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')

szul_ev=[]
szul_nap=[]
szul_ho=[]
kezdes_eve=[]
vegzes_eve=[]


adatok_szama=int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    szul_ev.append(int(adat[0]))
    szul_ho.append(int(adat[1]))
    szul_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    vegzes_eve.append(int(adat[4]))

eletkor_hatar = int(input('Adj meg egy életkort: '))
for i in range(adatok_szama):
    kor =vegzes_eve[i]-szul_ev[i]
    if kor < eletkor_hatar:
        print(f'Van {eletkor_hatar} évnél fiatalabb végzett')
        break

else:
    print(f'Nincs {eletkor_hatar} évnél fiatalabb végzett')