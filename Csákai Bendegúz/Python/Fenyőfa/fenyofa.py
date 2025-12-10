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

# 1. olvasd be és tárold el a kép karaktereit
forras = open('fakt2025\\Csákai Bendegúz\\Python\\Fenyőfa\\fenyofa.txt', mode='r',encoding='utf-8')
adat = forras.readline().strip()
szeles, magas = int(adat[0]),int(adat[1])
szinek = []
for i in range(szeles):
    adat = forras.readline()[:magas]
    szinek.append(adat)
forras.close()

hatter = 0
piros = 0
kek = 0
zold = 0
sarga = 0
feher = 0
barna = 0
for szel in range(szeles):
    for mag in range(magas):
        if szinek[szel][mag] == 'h':
            hatter += 1
        elif szinek[szel][mag] == 'p':
            piros += 1
        elif szinek[szel][mag] == 'k':
            kek += 1
        elif szinek[szel][mag] == 'z':
            zold += 1
        elif szinek[szel][mag] == 's':
            sarge += 1
        elif szinek[szel][mag] == 'f':
            feher += 1
        elif szinek[szel][mag] == 'b':
            barna+= 1
print(hatter, piros, kek, zold, sarga, feher, barna)
0  