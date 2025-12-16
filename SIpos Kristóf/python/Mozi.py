forras=open('Sipos Kristóf\\python\\mozi.txt', mode='r' , encoding='utf-8')

adat= forras.readline().strip().split(' ')
sorok_szama,szekek_szama=int(adat[0]),int(adat[1])

arak=[]
for i in range(sorok_szama):
    adat=forras.readline().strip()
    arak.append([int(c)*500 for c in adat])

foglalas=[]
for i in range(sorok_szama):
    adat=forras.readline()[:szekek_szama]
    foglalas.append(adat)

forras.close

def f(n):
    print(f'\n{n}. Feladat')
# Feladat 1
f(1)
Eladott=0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            Eladott+=1
print(f'{Eladott} széket adtak el összesen.')

# Feladat 2
f(2)
teljes_bevetel = 0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        teljes_bevetel += arak[sor][szek]
print(f'A teljes bevétel {teljes_bevetel:,} FT lenne.')

# Feladat 3
f(3)
bevetel=0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek] == 'x':
            bevetel += arak[sor][szek]
print(f'A mozi bevétele {bevetel} FT.')

# Feladat 4
def foglalt_sorban(s):
    foglalt=0
    for szek in range(szekek_szama):
        if foglalas[s][szek] == 'x':
            foglalt+=1
    return foglalt

f(4)
legkevesebb_index=0
legkevesebb_hely= foglalt_sorban(0)
for sor in range(sorok_szama):
    if foglalt_sorban(sor)< legkevesebb_hely:
        legkevesebb_hely = foglalt_sorban(sor)
        legkevesebb_index = sor
print(f'A legkevesebb foglalt hely a {legkevesebb_index+1}. sorban van és {legkevesebb_hely}.')
# Feladat 5
f(5)
print('Az alábbi helyeken van csak egy üres szék: ')
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if (
            foglalas[sor][szek] ==' ' 
            and (szek==0 or foglalas[sor][szek-1] == 'x') 
            and (szek==szekek_szama-1 or foglalas[sor][szek+1])
            ):
            print(f'\t{sor+1}.sor {szek+1}. hely')

# Feladat 6
f(6)
letszam = int(input('Hányan vagytok: '))
for sor in range(sorok_szama):
    for szek in range(szekek_szama-(letszam-1)):
        if foglalas[sor][szek:szek+letszam] == ' '*(letszam):






