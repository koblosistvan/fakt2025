forras = open("Ódor Artúr\\python\\mozi\\mozi.txt", mode= "r", encoding="utf-8")

adat = forras.readline().strip().split(" ")
sorok_sz, szekek_sz = int(adat[0]), int(adat[1])

arak = []
for i in range(sorok_sz):
    adat = forras.readline().strip()
    arak.append([int(c)*500 for c in adat])

foglaltsag = []
for i in range(sorok_sz):
    adat = forras.readline()[:szekek_sz]
    foglaltsag.append(adat)
forras.close()

def f(n):
    print(f"\n{n}. feladat")

f(1) #megszámlálás
eladaott = 0
for sor in foglaltsag:
    for szek in sor:
        if szek == "x":
            eladaott += 1
print(f"Összesen {eladaott} jegyet adtak el a filmre.")

f(2) #összegzés
teljes_bevetel = 0
for sor in range(sorok_sz):
    for szek in range(szekek_sz):
        teljes_bevetel += arak[sor][szek]
print(f"A bevétel {teljes_bevetel:,}ft volt.")

f(3)
bevetel = 0
for sor in range(sorok_sz):
    for szek in range(szekek_sz):
        if foglaltsag[sor][szek] == "x":
            bevetel += arak[sor][szek]
print(f"A jelenlegi foglaltság mellett {bevetel:,}ft a bevétel.")


f(4) #min/max keresés
def foglalt_sorban(s):
    foglalt = 0
    for szek in range(szekek_sz):
        if foglaltsag[s][szek] == "x":
            foglalt += 1
    return foglalt

legkevesebb, legkevesebb_i = foglalt_sorban(0), 0
for sor in range(sorok_sz):
    if foglalt_sorban(sor) < legkevesebb:
        legkevesebb, legkevesebb_i = foglalt_sorban(sor), sor
    
print(f"{legkevesebb} hely foglalt a {legkevesebb_i +1} sorban. Ebben a sorban van a legkevesebb foglalás")

f(5) #kiválogatás
print("Az alábbi helyeken van 1 üres szék: ")
for sor in range(sorok_sz):
    for szek in range(szekek_sz):
        if (
            foglaltsag[sor][szek] == " " 
            and (szek == 0 or foglaltsag[sor][szek-1] == "x")
            and (szek == szekek_sz-1 or foglaltsag[sor][szek +1] == "x")):
#six - seven 
            print(f"{sor + 1} {szek + 1}")

f(6)
for sor in range(sorok_sz):
    for szek in range(szekek_sz - 2):
        if foglaltsag[sor][szek:szek+3] == "   ":
            print(f"{sor + 1} sorban a {szek} - {szek + 2}. székek")