def f(n):
    print(f'\n\n{n}. feladat:')

#1
forras = open('fakt2025\\_Feladatok\\python\\11 év végi gyakorlás\\2-csapat-2.txt', mode='r', encoding='utf-8')

jatekosok = {}

kezdo = forras.readline().strip().split(',')
for i in range(len(kezdo)):
    szam = int(kezdo[i])
    jatekosok[szam] = True
print(jatekosok)

volt_palyan = jatekosok.copy()
vegig_volt = jatekosok.copy()

for sor in forras:
    adat = sor.strip().split(',')
    perc, le, fel = int(adat[0]), int(adat[1]), int(adat[2])
    volt_palyan[fel] = True
    jatekosok[fel] = True
    volt_palyan[le] = False
    vegig_volt[le] = False
f(1)
for szam, volt in volt_palyan.items():
    if volt:
        print(szam, end=" ")
f(2)
for szam, vegig in vegig_volt.items():
    if vegig:
        print(szam, end=" ")
