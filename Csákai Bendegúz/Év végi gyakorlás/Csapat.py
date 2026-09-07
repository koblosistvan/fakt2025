def f(n):
    print(f'\n\n{n}. feladat:')

#1
forras = open('fakt2025\\_Feladatok\\python\\11 év végi gyakorlás\\2-csapat-1.txt', mode='r', encoding='utf-8')
sor = forras.readline().strip().split(' ')
jatekos_db, csere_db = int(sor[0]), int(sor[1])
'''print(f'{jatekos_db = }\n {csere_db = }')
'''

jatekosok = {}

for mezszam in range(1, jatekos_db+1):
    jatekosok[mezszam]= False
'''print(jatekosok)
'''
for _ in range(7):
    sor = int(forras.readline().strip())
    jatekosok[sor] = True
'''print(jatekosok)
'''
volt_palyan = jatekosok.copy()
vegig_volt = jatekosok.copy()

for _ in range(csere_db):
    sor = forras.readline().strip().split()
    perc, le, fel = int(sor[0]), int(sor[1]), int(sor[2])
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
