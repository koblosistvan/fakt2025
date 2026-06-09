forras = open('Szmodis Vince\\python\\11 év végi gyakorlás\\2-csapat-2.txt', mode='r', encoding='utf-8')


jatekosok = {}

kezdo= forras.readline().strip().split(',')

for i in range(len(kezdo)):
    szam = int(kezdo[i])
    jatekosok[szam] = True



volt_palyan = jatekosok.copy()
maradt_palyan = jatekosok.copy()

for sor in forras:
    adat = sor.strip().split(',')
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
