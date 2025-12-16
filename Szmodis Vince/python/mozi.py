forras = open('Szmodis Vince\\python\\mozi.txt' , mode= 'r', encoding='utf-8')
adat=forras.readline().strip().split(' ')
sorok_szama, szekek_szama= int(adat[0]), int(adat[1])

def f(n):
    print(f'\n{n}. feladat')
    print('-'*15)

arak=[]
for sor in range(sorok_szama):
    adat=forras.readline().strip()
    s =[]
    '''
    for c in adat:
        s.append(int(c)*500)
    '''    
    arak.append([int(c)*500 for c in adat])
    

foglalas= []
for i in range(sorok_szama):
    adat=forras.readline()[:szekek_szama]
    foglalas.append(adat)

f(1)
eladott=0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek]=='x':
            eladott+=1
print(f'{eladott} jegyet atdak el a filmre')

f(2)
bevetel=0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        bevetel+=arak[sor][szek]
print(f'{bevetel:,} volt az össz bevétel')

f(3)
jelenlegi_bevetel=0
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek]=='x':
            jelenlegi_bevetel += arak[sor][szek]
print(f'{jelenlegi_bevetel} volt a jelenlegi bevétel ')

def foglalt_sorban(s):
    foglalt=0
    for szek in range(szekek_szama):
        if foglalas[s][szek]=='x':
            foglalt+=1
    return foglalt

f(4)
legkevesebb_index=0
legkevesebb = foglalt_sorban(0)
for sor in range(sorok_szama):
     if foglalt_sorban(sor)<legkevesebb:
        legkevesebb=foglalt_sorban(sor)
        legkevesebb_index=sor

print(f'A legkevesebb {legkevesebb} darab hely a {legkevesebb_index+1} sorban van')

f(5)
print('Az alábbi heyeken van csak egy üres szék')
for sor in range(sorok_szama):
    for szek in range(szekek_szama):
        if foglalas[sor][szek]==' ' and (szek==0 or foglalas[sor][szek-1]=='x')\
            and (szek==szekek_szama-1 or foglalas[sor][szek+1]=='x'):
            print(f'\t{sor+1}. sor {szek+1}. hely')

f(6)

