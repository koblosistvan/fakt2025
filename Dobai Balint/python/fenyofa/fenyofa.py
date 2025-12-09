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

def f(n):
    print(f'\n {n}. feladat:')

f(1)
hopihe = 0 
for sor in range(sorok_szama):
    for pixel in range(pixel_szama):
        if sor == 'f':
            hopihe +=1

print(hopihe)