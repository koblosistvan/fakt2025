forras = open('Törös Zétény\python\mozi.txt',mode='r', encoding='utf-8')
adat = forras.readline().strip().split(' ')
sorok_szama, szekek_szama, = int(adat[0]), int(adat[1])
arak = []
for i in range(sorok_szama):
    adat = forras.readline().strip()
    arak.append([int(c)*500 for c in adat])

foglalt = []
for i in range(sorok_szama):
    adat = forras.readline()[:szekek_szama]
    foglalt.append(adat)

forras.close()

elkelt = 0
for i in range(sorok_szama):
    for j in range(szekek_szama):
        if foglalt[i][j] == 'x':
            elkelt += 1

print(f"Összesen  {elkelt} jegyet adtak el a filmre.")

teljes_bevetel = 0
for i in range(sorok_szama):
    for j in range(szekek_szama):
        teljes_bevetel += arak[i][j]

print(f"A teljes bevétel teltház esetén: {teljes_bevetel:,} Ft")

eladott = 0

jelenlegi_bevetel = 0
for i in range(sorok_szama):
    for j in range(szekek_szama):
        if foglalt[i][j] == "x":
            jelenlegi_bevetel += arak[i][j]
print(f"A jelenlegi eladott jegyek összege: {jelenlegi_bevetel:,} Ft")




























67