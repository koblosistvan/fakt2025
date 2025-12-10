'''
Adott egy kép egy fenyőfáról, melynek minden pixelét egy karakter jelöl a forrás állományban
Méretek: 40x40 pixel, soronként balról jobbra haladva.
Jelmagyarázat: k=fekete háttér, Z=zöld, B=barna, s=sárga, p=piros, b=kék, f=fehér

Feladatok:
1. olvasd be és tárold el a kép karaktereit
2. hány hópihét látsz a képen?
3. melyik sorban van a törzs teteje?
4. melyik sorban van a törzs alja, milyen magas a fa törzse?
5. hány dísz van a fán? 
6. milyen színű díszeket látsz, melyikből hányat?
'''
def f(n):
    print(f"\n {n}. feladat")

f(1)    
forras = open(r"Ódor Artúr\python\Fenyőfa\fenyofa.txt", mode="r", encoding="utf-8")
adat = forras.readline().strip().split(" ")
sorok_sz, pixel_sz = int(adat[0]), int(adat[1])

pixelek = []
for i in range(sorok_sz):  
    pixelek.append(forras.readline().strip())
print(f"A fájl beolvasva")


f(2)
hopehely = 0
for sor in pixelek:
    for pixel in sor:
        if pixel == "f":
            hopehely += 1  
print(f"A hópelyhek száma: {hopehely}")

f(3)
teteje = 0
for sor in range(sorok_sz):
    for pixel in range(pixel_sz):
        if pixelek[sor][pixel] == "b":
            teteje = sor + 1
            print(f"A {teteje}. sorban kezdődik a törzs.")
            break
    if pixelek[sor][pixel] == "b":
            break
    
f(4)
szamlalo = 0
for sor in range(sorok_sz):
    for pixel in range(pixel_sz):
        if pixelek[sor][pixel] == "b":
            szamlalo += 1
            break
print(f"A törzs alja {teteje + szamlalo}. sorban van, és {szamlalo} magas a törzs.")

f(5)
disz = 0
for sor in pixelek:
    for pixel in sor:
        if pixel == "s" or pixel == "p" or pixel == "k" or pixel=="a":
            disz += 1
print(f"{disz} pixel dísz van.")

f(6)
alapszinek = "fhzb"
diszek = {}
#six-seven 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67 67
for sor in pixelek:
    for pixel in sor:
        if pixel not in alapszinek:
            if pixel in diszek:
                diszek[pixel] += 1
            elif pixel not in diszek:
                diszek[pixel] = 1
print(diszek)