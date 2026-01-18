def f(n):
    print('\n' + '-'*40)
    print(f'{n}. feladat')

forras = open('_Feladatok\\python\\Mozi\\mozi.txt', mode='r', encoding='utf-8')
adat = forras.readline().strip().split()
sorok_szama, szekek_szama = int(adat[0]), int(adat[1])

arak = []
for i in range(sorok_szama):
    sor = [int(c) * 400 for c in forras.readline().strip()]
    arak.append(sor)

elkelt = []
for i in range(sorok_szama):
    sor = forras.readline()[:szekek_szama]
    elkelt.append(sor)


# hány jegyet adtak el a moziban
f(1)
jegyek_szama = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if elkelt[sor][szek] == 'x':
            jegyek_szama += 1
print(f'Összesen {jegyek_szama} jegy kelt el a filmre.')

# mennyi lenne a mozi bevétele telt ház esetén
f(2)
telthaz = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        telthaz += arak[sor][szek]
print(f'Telház esetén a bevétel {telthaz:,} Ft lenne.')

# mennyi a jelenlegi foglalás mellett a bevétel
f(3)
bevetel = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if elkelt[sor][szek] == 'x':
            bevetel += arak[sor][szek]
print(f'A jelenlegi foglalás mellett a bevétel {bevetel:,} Ft.')

# melyik sorban van a legkevesebb foglalt hely
f(4)
legkevesebb = szekek_szama
legkevesebb_index = -1
for sor in range(sorok_szama):
    foglalt_a_sorban = 0
    for szek in range(szekek_szama):
        if elkelt[sor][szek] == 'x':
            foglalt_a_sorban += 1
    if foglalt_a_sorban < legkevesebb:
        legkevesebb_index = sor
        legkevesebb = foglalt_a_sorban
print(f'A legkevesebb ({legkevesebb} darab) jegy a {legkevesebb_index+1}. sorba kelt el.')

# hol vannak szingli szabad helyek
f(5)
szingli_helyek = []
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if (elkelt[sor][szek] == ' ' 
            and (szek == 0 or elkelt[sor][szek-1] == 'x')
            and (szek == szekek_szama-1 or elkelt[sor][szek+1] == 'x')):
            szingli_helyek.append((sor+1, szek+1))
if len(szingli_helyek) > 0:
    print('Szabad szingli helyek:')
    for sor, szek in szingli_helyek:
        print(f'\t{sor}. sor {szek}. szék')
else:
    print('Nincs szabad szingli hely.')

# keress helyet egy háromfős társaság számára
f(6)
letszam = 5
szabad_helyek = []
for sor in range(sorok_szama):
    for szek in range(szekek_szama - letszam + 1):
        if elkelt[sor][szek:szek + letszam] == ' ' * letszam:
            szabad_helyek.append((sor+1, f'{szek+1}-{szek+letszam}'))
if len(szabad_helyek) > 0:
    for sor, szek in szabad_helyek:
        print(f'\t{sor}. sor {szek}. szék')
else:
    print(f'Sajnos nincs már hely {letszam} fős társaság számára.')

print('Vége.')
