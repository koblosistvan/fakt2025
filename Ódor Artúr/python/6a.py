forras = open("Ódor Artúr\\python\\6a-hallgatok.txt", mode= "r", encoding="utf-8")
adatok_sz = int(forras.readline())

szuletesi_ev = []
szuletesi_ho = []
szuletesi_nap = []
kezdes_eve = []
befejezes_eve = []

for sor in forras:
    adat = sor.strip().split(" ")
    szuletesi_ev.append(int(adat[0]))
    szuletesi_ho.append(int(adat[1]))
    szuletesi_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    befejezes_eve.append(int(adat[4]))
forras.close

eletkor = int(input("Add meg a korod: "))
for i in range(adatok_sz):
    kor = befejezes_eve[i] -szuletesi_ev[i]
    if kor < eletkor:
        print(f"Van {eletkor} évnél fiatalabb végzett.")
        break
else:
    print(f"Nincs {eletkor} évnél fiatalabb.")