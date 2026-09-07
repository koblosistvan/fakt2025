forras = open('Szmodis Vince\\python\\11 év végi gyakorlás\\2-csapat-1.txt', mode='r', encoding='utf-8')
sor= forras.readline().strip().split(' ')
jatekos_db= int(sor[0])
csere_db= int(sor[1])

jatekosok = {}

for mezszam in range(1, jatekos_db):
    jatekosok[mezszam]= False
print(jatekosok)

for _ in range(7):
    sor=int(forras.readline().strip())
    jatekosok[sor] = True
print(jatekosok)


volt_palyan = jatekosok.copy()
maradt_palyan = jatekosok.copy()
for _ in range(csere_db):
    sor = forras.readline().strip().split(' ')
    perc = int(sor[0])
    ki = int(sor[1])
    be = int(sor[2])
    volt_palyan[be]=True
    jatekosok[be]=True
    jatekosok[ki]=False
    maradt_palyan[be] = False
    maradt_palyan[ki] = False


for szam, volt in volt_palyan.items():
    if volt:
        print(szam, end=' ')


#print(jatekosok)
#print(volt_palyan)

for szam, maradt in maradt_palyan.items():
    if maradt:
        print(szam, end=' ')
print()

