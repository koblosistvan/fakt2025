forras = open('_Megoldások\\python\\4c-bolt.txt', mode = 'r', encoding='utf-8')

bevetel = []
kiadas = []
for sor in forras:
    adat = sor.strip().split(',')
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))

adatok_szama = len(bevetel)

print(bevetel)
print(kiadas)

veszteseges_nap = 0
for i in range(adatok_szama):
    if kiadas[i] > bevetel[i]:
        veszteseges_nap += 1

print(f'{veszteseges_nap} nap volt veszteseges')

tizes_profit = 0 
for i in range(adatok_szama):
    if kiadas[i] < bevetel[i]:
        tizes_profit += 1

print(f'{tizes_profit} nap volt ilyen')


ossz_bevetel = 0 
ossz_kiadas = 0 
for i in range(adatok_szama):
    ossz_bevetel += bevetel[i]
    ossz_kiadas += kiadas[i]

print(f'a teljes profit {ossz_bevetel-ossz_kiadas} volt')

hetvegi_bevetel = 0
hetvegi_kiadas = 0 



