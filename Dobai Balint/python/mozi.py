forras = open('Dobai Balint\\mozi.txt', mode ='r', encoding='utf-8')
adat = forras.readline().strip().split(' ')
sorok_szama , szekek_szama = int(adat[0]) , int(adat[1])

arak = []
for i in range(sorok_szama):
    adat = forras.readline().strip()
    arak.append([int(c)*500 for c in adat])

'''     for c in adat:
        s.append(int(c)*500)
    arak.append(s)
'''


foglalas = []
for i in range(sorok_szama):
    adat = forras.readline()[:szekek_szama]
    foglalas.append(adat)
forras.close()

def f(n):
    print(f'\n {n}. feladat')

f(1)
eladott = 0
for sor in range(sorok_szama):
    for szek in range (szekek_szama):
        if foglalas[sor][szek] == 'x':
            eladott +=1
print(f'Osszesen {eladott} db jegyet adtak el')

f(2)
teljes_bevetel = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        teljes_bevetel += arak[sor][szek]
print(f'A teljes bevetel telthaz eseten {teljes_bevetel:,} Ft')

f(3)
foglalt_bevetel = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':  
            foglalt_bevetel += arak[sor][szek]
print(f'A jelenlegi foglaltsag mellet a bevetel : {foglalt_bevetel:,} Ft')

#megszamolja s-edik sorban hany hely foglalt
def foglalt_sorban(s):
    foglalt = 0
    for szek in range(szekek_szama):
        if foglalas[s][szek] == 'x':
            foglalt +=1
    return foglalt
f(4)
legkevesebb_index = 0 
legkevesebb = foglalt_sorban(0)
for sor in range(1, sorok_szama):
    if foglalt_sorban(sor) < legkevesebb:
        legkevesebb = foglalt_sorban(sor)
        legkevesebb_index = sor
print(f'A legkevesebb elkelt hely a {legkevesebb_index+1} sorban {legkevesebb} db hely')

'''
foglalt_sorban = 0
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            foglalt_sorban +=1

'''

f(5)
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if (
            foglalas[sor][szek] == ' ' 
            and (szek==0 or foglalas[sor][szek-1] == 'x')
            and (szek ==szekek_szama-1 or foglalas[sor][szek+1] == 'x')
            ):
            print(f'\t A {sor+1}-adik sor {szek+1}-edik hely')

f(6)    
for sor in range(sorok_szama):
    for szek in range(szekek_szama-2):
        if foglalas[sor][:szek+3] == '   ':
            print('')






