'''
Adott egy kép egy fenyőfáról, melynek minden pixelét egy karakter jelöl a forrás állományban
Méretek: 40x40 pixel, soronként balról jobbra haladva.
Jelmagyarázat: h=háttér, z=zöld, b=barna, s=sárga, p=piros, k=kék, f=fehér

Feladatok:
1. olvasd be és tárold el a kép karaktereit
2. hány hópihét látsz a képen?
3. melyik sorban van a törzs teteje?
4. melyik sorban van a törzs alja, milyen magas a fa törzse?
5. hány dísz van a fán? 
6. milyen színű díszeket látsz, melyikből hányat?
'''

forras = open('Dobai Balint\\python\\fenyofa\\fenyofa.txt', mode ='r', encoding='utf-8')
adat = forras.readline().strip().split(' ')

sorok_szama , pixel_szama = int(adat[0]) , int(adat[1])

# kép beolvasás és tárolás
a = []
for i in range(sorok_szama):
    adat = forras.readline()[:pixel_szama]
    a.append(adat)
forras.close()

def f(n):
    print(f'\n {n}. feladat:')

f(2)
hopihe = 0 
for sor in range(sorok_szama):
    for pixel in range(pixel_szama):
        if a[sor][pixel] == 'f':
            hopihe +=1
print(f'A kepen {hopihe} db hopihe talalhato')

f(3)
torzs = []
for sor in range(sorok_szama):
    for pixel in range(pixel_szama):
        if a[sor][pixel] == 'b':
            torzs.append(sor)
print(f'A torzs teteje {min(torzs)}.-edik sorban van')

f(4)
print(f'A torzs alja {max(torzs)}.-edik sorban van')
print(f'A torzs magassaga {max(torzs)-min(torzs)} sor')

f(5)
diszek_szama = 0
for sor in range(sorok_szama):
    for pixel in range(pixel_szama):
        if a[sor][pixel] == 'k' or a[sor][pixel] == 'P' or a[sor][pixel] =='s':
            diszek_szama +=1
print(f'A diszek szama : {diszek_szama}')

f(6)
alap = 'hfbz'
szinek_szama = {}

for sor in range(sorok_szama):
    for pixel in range(pixel_szama):
        b = a[sor][pixel]
        if b not in alap:
            if b not in szinek_szama:
                szinek_szama[b] = 1
            else:
                szinek_szama[b]+=1
print(szinek_szama )
             