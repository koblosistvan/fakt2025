forras = open('fakt2025\Roboz Hunor\\python\\Mozi\\mozi.txt',mode = 'r', encoding='utf-8')
adat = forras.readline().strip().split(' ')
sorok,szekek_szama=int(adat[0]),int(adat[1])

arak = []

for sor in range(sorok):
    adat = forras.readline().strip()
    arak.append([int(c)*500 for c in adat])

foglalas = []

for i in range(sorok):
    adat = forras.readline()[:szekek_szama]
    foglalas.append(adat)
forras.close()

def f(n):
    print(f'\n{n}. feladat')

eladtak = 0

for sor in range(sorok):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            eladtak += 1
f(1)
print(f'Összesen {eladtak} jegyet adtak el' )

össz_bev = 0

for sor in range(sorok):
    for szek in range(szekek_szama):
        össz_bev += arak[sor][szek]
f(2)
print(f'Összesen {össz_bev:,}Ft lenne a mozi teljes bevétele teltház esetén')

f(3)
jel_bev = 0
for sor in range(sorok):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            jel_bev += arak[sor][szek]
print(f'Összesen {jel_bev:,}Ft a mozi teljes bevétele')

f(4)

def foglalt_sorban(s):
    akt_darab = 0
    for szek in range(szekek_szama):
        if foglalas[s][szek] == 'x':
            akt_darab += 1
    return(akt_darab)

legkevesebb = foglalt_sorban(0)
legkis_sor = 0 

for sor in range(sorok):
    if legkevesebb > foglalt_sorban(sor):
            legkevesebb = foglalt_sorban(sor)
            legkis_sor = sor

print(f'A {legkis_sor+1}. sorban van a legkevesebb foglalt szék ({legkevesebb})')        
        
f(5)
print('Az alábbi helyeken van üres szék')
#six-seven 67 67 67 67 67 67 67 67 67 67 67 67 67 67 


for sor in range(sorok):
    for szek in range(szekek_szama):
        if (
            foglalas[sor][szek] == ' '
            and (szek == 0 or foglalas[sor][szek-1] == 'x') 
            and (szek == szekek_szama-1 or foglalas[sor][szek+1] == 'x')
            ):
            print(f'\t{sor+1}.sor {szek+1}.szék')

f(6)

for sor in range(sorok):
    for szek in range(szekek_szama-2):
       if foglalas[sor][szek:szek+3]  == '   ':
           print(f'Ide ülhet a 3 fös társaság:\n{sor}. sor {szek}. szék {sor}. sor {szek+1}. szék {sor}. sor {szek+2}. szék')


f(7)
#Házi
létszám = int(input('Hányan vagytok'))

for sor in range(sorok):
    for szek in range(szekek_szama-(létszám-1)):
        if foglalas[sor][szek:szek+létszám]  == ' '*létszám:
            print(f'\nIde ülhet a {létszám} fös társaság:')
            for x in range(létszám):
                print(f'{sor+1}. sor {szek+x}. szék',end=' ')