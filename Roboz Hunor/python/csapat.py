forras = open("_Feladatok\\python\\11 év végi gyakorlás\\2-csapat-1.txt",mode="r",encoding="utf-8")
a = forras.readline().strip().split()
jatekos_db,cserek_db = int(a[0]),int(a[1])

"""
kezdo, perc, le, fel = [], [], [], []

for sor in range(7):
    kezdo.append(sor).strip()


for sor in range(cserek_db):
    adat = sor.strip().split()
    perc.append(adat[0])
    le.append(adat[1])
    fel.append(adat[2])"""


jatekosok = {}

for mezszam in range(1, jatekos_db+1):
    jatekosok[mezszam] = False


for _ in range(7):
    sor = int(forras.readline().strip())
    jatekosok[sor] = True





volt_a_palyan = jatekosok.copy()
nincs = jatekosok.copy()
vegen = jatekosok.copy()

for _ in range(cserek_db):
    sor = forras.readline().strip().split()
    perc,le,fel = int(sor[0]),int(sor[1]),int(sor[2])
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





