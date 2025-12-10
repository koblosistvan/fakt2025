forras = open('fakt2025\\Csákai Bendegúz\\Python\\Fenyőfa\\fenyofa.txt')
adat = forras.readline().strip().split()
magassag, szelesseg = int(adat[0]), int(adat[1])

kep = []
for sor in range(magassag):
    kep.append(forras.readline().strip())
forras.close()


def f(n):
    print(f'\n{n}. feladat')


f(1)
print(f'Beolvastam a {szelesseg} x {magassag} px méretű képet.')


alapszinek = 'hzbf'
szinek_szama = {}

f(2)
for sor in range(magassag):
    for oszlop in range(szelesseg):
        pixel_szin = kep[sor][oszlop]
        if pixel_szin not in alapszinek:
            if pixel_szin in szinek_szama:
                szinek_szama[pixel_szin] += 1
            else:
                szinek_szama[pixel_szin] = 1
print(szinek_szama)
f(3),print('\n\tés'),f(4)
torzs_telj = []
for sor in range(magassag):
    for oszlop in range(szelesseg):    
        if kep[sor][oszlop] == 'b':
            torzs_telj.append(sor+1)
            break

print(f'{torzs_telj[0]}. sorban van a törzs teteje, {torzs_telj[-1]}. sorban volt a törzs alja, és a törzs {len(torzs_telj)} hosszú.')
f(5)
