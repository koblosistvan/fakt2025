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
forras = open("Törös Zétény\\python\\fenyofa.txt",encoding="utf-8", mode="r")
adat = forras.readline().strip().split()
sorok_szama, pixelek_szama, = int(adat[0]), int(adat[1])


kep = []
for i in range(sorok_szama):
    adat = forras.readline().strip()
    kep.append(adat)
forras.close() 
#2. hány hópihét látsz a képen?
x = 0
for i in range(sorok_szama):
    for j in range(pixelek_szama):
        if kep[i][j] == "f":
            x += 1
print(f"Ennyi hópihe van: {x}")

#3. melyik sorban van a törzs teteje?
index = 0
for i in range(sorok_szama):
    if "b" in kep[i]:
        index = i+1
        break
print(f"Ebben a sorban kezdődik a fa törzse: {index}")

#4. melyik sorban van a törzs alja, milyen magas a fa törzse?
idex_2 = 0
for i in range(sorok_szama):
    if "b" in kep[i]:
        index_2 = i+1
print(f"A fa törzse {index_2}-nél van az alja és a fa törzse {index_2-index+1} hosszú")

#5. hány dísz van a fán? 
disz = 0
for i in range(sorok_szama):
    for j in range(pixelek_szama):
        if kep[i][j] == "k" or kep[i][j] == "p" or kep[i][j] == "s":
            disz += 1
print(f"Ennyi dísz van: {disz}")

#6. milyen színű díszeket látsz, melyikből hányat?
szinek = []
h_szinek = ['z','h','f','b']
for i in range(sorok_szama):
    for j in range(pixelek_szama):
        if kep[i][j] not in h_szinek:
            szinek.append(kep[i][j])

s = 0
k = 0
p = 0 #67
for i in range(len(szinek)):
    if szinek[i] == 's':
        s += 1
    if szinek[i] == 'p':
        p += 1
    if szinek[i] == 'k':
        k += 1
print(f"Van {s} sárga: , {k} kék, és {p} piros színű dísz van")
