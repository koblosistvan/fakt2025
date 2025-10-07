forras = open('_Megoldások\\python\\4c-bolt.txt', mode='r', encoding='utf-8')

bevetel = []
kiadas = []
for sor in forras:
    adat = sor.strip().split(',')
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))
napok_szama = len(bevetel)

ossz_bevetel = 0
ossz_kiadas = 0
for i in range(napok_szama):
    ossz_bevetel += bevetel[i]
    ossz_kiadas += kiadas[i]
print(f'A teljes profit {ossz_bevetel - ossz_kiadas} Ft volt.')
