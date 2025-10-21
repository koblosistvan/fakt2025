forras = open('_Megoldások\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')

szul_ev = []
szul_ho = []
szul_nap = []
kezdes_eve = []
vegzes_eve = []

adatok_szama = int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    szul_ev.append(int(adat[0]))
    szul_ho.append(int(adat[1]))
    szul_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    vegzes_eve.append(int(adat[4]))

eletkor_hatar = int(input('Adj meg egy életkort: '))
for i in range(adatok_szama):
    kor = vegzes_eve[i] - szul_ev[i]
    if kor < eletkor_hatar: # az adott ember fiatalabban szerzett diplomát
        print(f'Van {eletkor_hatar} évnél fiatalabb végzett.')
        break
else:
    print(f'Nincs {eletkor_hatar} évnél fiatalabb végzett.')

i = 0
while i < adatok_szama and vegzes_eve[i] - szul_ev[i] >= eletkor_hatar:
    i += 1
if i < adatok_szama:
    print(f'Van {eletkor_hatar} évnél fiatalabb végzett.')
else:
    print(f'Nincs {eletkor_hatar} évnél fiatalabb végzett.')


# Kérjbeafelhasználótólegyéletkorértéket,majddöntsdel,hogyvan-eolyanhallgató,akiennélfiatalabbanszerzettdiplomát!(eldöntés)
# Van-eolyanhallgató,akinekugyanazonanaponvanaszületésnapja,mintNeked?(eldöntés)
# Határozdmeg,hogymikorszületettazavégzetthallgató,akilegfiatalabbanszereztemegadiplomáját!(min/max)
legfiatalabb_index = 0
legfiatalabb_kor = vegzes_eve[0] - szul_ev[0]
for i in range(adatok_szama):
    if legfiatalabb_kor > vegzes_eve[i] - szul_ev[i]:
        legfiatalabb_kor = vegzes_eve[i] - szul_ev[i]
        legfiatalabb_index = i
print(f'A legfiatalabb végzett a {legfiatalabb_index + 1}. hallgató, aki {legfiatalabb_kor} évesen végzett.')

# Számoldmeg,hogyhányhallgatóvégzett2016-ban!(megszámlálás)
# Mekkoraazátlagéletkorazegyetemen2014tavaszán?(összegzés,megszámlálás