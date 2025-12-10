forras = open('fakt2025\\Csákai Bendegúz\\Python\\Mozi\\mozi.txt',mode='r',encoding='utf-8')
adat = forras.readline().strip().split(' ')
sorok_szama, szekek_szama = int(adat[0]), int(adat[1])

arak = []
for i in range(sorok_szama):
    adat = forras.readline().strip()
    s = []
    for c in adat:
        s.append(int(c)*500)
    arak.append(s)
    #arak.append([int(c)*500 for c in adat])
foglalas = []
for i in range(sorok_szama):
    adat = forras.readline()[:szekek_szama]
    foglalas.append(adat)
forras.close()

def f(n):
    print(f'\n{n}. feladat')


f(1)
eladott = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            eladott += 1
print(f'Összesen {eladott} jegyet adtak el a filmre.')

f(2)
telj_bev = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        telj_bev += arak[sor][szek]
print(f'Teltház esetén a bevétel {telj_bev:,} Ft lenne')

f(3)
jelen_bev = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            jelen_bev += arak[sor][szek]
print(f'Jelenlegi foglalás mellett a bevétel {jelen_bev:,} Ft')


def foglalt_sorban(s):
    foglaltak_sorban = 0
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            foglaltak_sorban += 1
    return foglaltak_sorban

f(4)
legk = szekek_szama
legk_index = foglalt_sorban(0)
for sor in range(sorok_szama):
    if foglalt_sorban(sor) < legk:
        legk = foglalt_sorban(sor)
        legk_index = sor+1
print(f'A legkevesebb foglalás {legk} volt, és a {legk_index}. sorba történt')

f(5)
print('Az alábbi helyeken vannak szingli helyek: ')
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if (foglalas[sor][szek] == ' '
            and (szek == 0 or foglalas[sor][szek-1] == 'x')
            and (szek ==  szekek_szama-1 or foglalas[sor][szek+1] == 'x')
            ):
            print(f'\t{sor+1}. sor {szek+1}. hely')

f(6)
for sor in range(sorok_szama):
    for szek in range(szekek_szama-2):
        if foglalas[sor][szek:szek+3] == '   ':
            print(f'3 fős helyek: {sor+1}.-sor: {szek} - {szek+2} székek ')

f(7)
letsz = int(input('Adja meg hányan jönnének: '))
print('\n')
a = letsz-1
n = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama-a):
        if foglalas[sor][szek:szek+letsz] == letsz*' ':
            print(f'{letsz} fős helyek: {sor+1}.-sor: {szek} - {szek+a} székek')
            n += 1
            if n == 0:
                print('Nincs ilyen lehetőség')