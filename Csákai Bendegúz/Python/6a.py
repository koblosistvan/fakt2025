forras = open('fakt2025\\Csákai Bendegúz\\Python\\6a-hallgatok.txt', mode= 'r', encoding= 'utf-8')

born_year = []
born_month = []
born_day = []
kezdes_eve = []
vegzes_eve = []

adt_szm = int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    born_year.append(int(adat[0]))
    born_month.append(int(adat[1]))
    born_day.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    vegzes_eve.append(int(adat[4]))

eletkor = int(input('Add meg az életkorodat: '))
for i in range(adt_szm):
    kor = vegzes_eve[i]-born_year[i]
    if kor < eletkor:
        print(f'Van {eletkor} évnél fiatalabb végzett')
        break
else:
    print(f'Nincs {eletkor} évnél fiatalabb végzett')