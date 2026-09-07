forras = open("_Feladatok\\python\\11 év végi gyakorlás\\2-csapat-2.txt",mode="r",encoding="utf-8")

jatekosok = {}

kezdo = forras.readline().strip().split(",")

for i in range(len(kezdo)):
    szam = int(kezdo[i])
    jatekosok[szam] = True
print(jatekosok)



volt_a_palyan = jatekosok.copy()
nincs = jatekosok.copy()
vegen = jatekosok.copy()

for sor in forras:
    adat_sor = sor.strip().split(",")
    perc,le,fel = int(adat_sor[0]),int(adat_sor[1]),int(adat_sor[2])
    volt_a_palyan[fel] = True
    jatekosok[fel] = True
    jatekosok[le] = False
    nincs[le] = False
    vegen[fel] = True
    vegen[le] = False

for szam, volt in volt_a_palyan.items():
    if volt:
        print(szam,end=" ")
print()


for szam, n in nincs.items():
    if n == True:
        print(szam,end=" ")
print()

for szam, a in vegen.items():
    if a == True:
        print(szam,end=" ")
print()

