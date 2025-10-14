forras = open("Ódor Artúr\\python\\6b-forgalom.txt", mode= "r", encoding= "utf-8")

forras.readline()

hely = []
ora = []
perc = []
ido = []
for sor in forras:
    adat = sor.strip().split(" ")
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1]) * 60 + int(adat[2]))
forras.close

legtobb_i = ido[1] - ido[0]
uj_hely = 0

for n in range(max(hely)):
    for i in range(len(ido) - 1):
        if hely[n] == hely[i] and ido[i] - ido[uj_hely]:
            legtobb_i = ido[i] - ido[uj_hely]
            uj_hely = i
print(f"{legtobb_i} perc volt a legtöbb idő ami eltelt azonos pontokon, úgy hogy nem jött autó.")

szamlalo = 0
for i in range(len(hely)):
    if hely[i] == 50:
        szamlalo += 1
print(f"{szamlalo} db mérési adat volt az 50-es mérési helyen.")

bekeres = map(int, input("Adj meg egy mérési időpontot (pl.: 04:50): ").strip().split(":"))

for i in range(len(ido)):