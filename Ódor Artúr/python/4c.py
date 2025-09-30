forras = open("Ódor Artúr\\python\\4c-bolt.txt", mode="r", encoding="utf-8")
bevetel = []
kiadas = []
for sor in forras:
    adat = sor.strip().split(",")
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))

veszteseges_napok = 0
tizszazalek_sz = 0
for i in range(len(bevetel)):
    if bevetel[i] < kiadas[i]:
        veszteseges_napok += 1
    if bevetel[i] >= kiadas[i] * 1.1:
        tizszazalek_sz += 1

profit_sz = 0
for i in range(len(bevetel) - 1):
    if bevetel[i] - kiadas[i] < bevetel[i + 1] - kiadas[i + 1]:
        profit_sz += 1

profit = sum(bevetel) - sum(kiadas)
osszeg_hetvege = 0
for i in range(len(bevetel)):
    if i == 5 or i == 6:
        osszeg_hetvege += bevetel[i] - kiadas[i]


print(f"\nVeszteséges napok {veszteseges_napok}\nProfit minimum 10% {tizszazalek_sz}\nProfit {profit_sz}\n"
      f"Napi adatok száma: {len(bevetel)}\nÖsszes profit: {profit}\nHétvégi profit: {osszeg_hetvege}")