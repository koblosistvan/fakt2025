forras = open('_Megoldások\\python\\Mozi\\mozi.txt',
              mode='r', encoding='utf-8')
adat = forras.readline().strip().split(' ')
sorok_szama, szekek_szama = int(adat[0]), int(adat[1])

arak = []
for i in range(sorok_szama):
    adat = forras.readline().strip() 
    arak.append([int(c)*500 for c in adat])

foglalas = []
for i in range(sorok_szama):
    adat = forras.readline()[:szekek_szama]
    foglalas.append(adat)

forras.close()


def f(n):
    print(f'\n{n}. feladat')


# hány jegyet adtak el a moziban
f(1)
eladott = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            eladott += 1
print(f'Összesen {eladott} jegyet adtak el a filmre.')

# mennyi lenne a mozi bevétele telt ház esetén
f(2)
teljes_bevetel = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        teljes_bevetel += arak[sor][szek]
print(f'Teltház esetén a bevétel {teljes_bevetel:,} Ft lenne.')

# mennyi a jelenlegi foglalás mellett a bevétel
f(3)
jelenlegi_bevetel = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            jelenlegi_bevetel += arak[sor][szek]
print(f'A jelenlegi foglalás mellett a bevétel {jelenlegi_bevetel:,} Ft.')


# megszámolja, hogy az s-edik sorban hány foglalt hely van
def foglalt_sorban(s):
    foglalt = 0
    for szek in range(szekek_szama):
        if foglalas[s][szek] == 'x':
            foglalt += 1
    return foglalt


# melyik sorban van a legkevesebb foglalt hely
f(4)
legkevesebb_index = 0
legkevesebb = foglalt_sorban(0)
for sor in range(1, sorok_szama):
    if foglalt_sorban(sor) < legkevesebb:
        legkevesebb = foglalt_sorban(sor)
        legkevesebb_index = sor
print(f'A legkevesebb ({legkevesebb} darab) hely a {legkevesebb_index+1}. sorban van.')


# hol vannak szingli szabad helyek
f(5)
print('Az alábbi helyeken van csak egy üres szék:')
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if (
            foglalas[sor][szek] == ' '
            and (szek == 0 or foglalas[sor][szek-1] == 'x')
            and (szek == szekek_szama-1 or foglalas[sor][szek+1] == 'x')
            ):
            print(f'\t{sor+1}.sor {szek+1}. hely')

# keress helyet egy háromfős társaság számára
letszam = int(input('Hányan vagytok?'))
for sor in range(sorok_szama):
    for szek in range(szekek_szama-2):
        if foglalas[sor][szek:szek+3] == '   ':
            print('')


print('Vége')
