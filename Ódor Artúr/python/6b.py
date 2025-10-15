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

# for pontok in set(hely):
#     legtobb_i = p_ido[1] - p_ido[0]
#     uj_hely = 0



szamlalo = 0
for i in range(len(hely)):
    if hely[i] == 50:
        szamlalo += 1
print(f"{szamlalo} db mérési adat volt az 50-es mérési helyen.")

# bekert_o, bekert_p = map(int, input("Adj meg egy mérési időpontot (pl.: 04:50): ").strip().split(":"))
# bekert_i = bekert_o * 60 + bekert_p
bekert_i = 100

for i in range(len(ido)):
    if bekert_i == ido[i]:
        print("Volt ebben az időpontban mérés.")
        break
else:
    print("Nem volt ebben az időpontban meres.")

for i in range(len(ido) - 1):
    if ido[i] == ido[i+1]:
        print("Volt ugyan abban az időpontban 2 mérési eredmény")
        break
else:
    print("Nem volt ugyan abban az időpontban mérés.")

statisztika = []
legnagyobb_i = 0
for n in range(100):
    statisztika.append(0)
    for i in range(len(ido)):
        if hely[i] == n + 1:
            statisztika[n] += 1
    print(f"{statisztika[n]} db mérés volt a {n+1}. helyen")
print(f"\n{statisztika.index(max(statisztika)) + 1} helyen volt a legtöbb mérés.")
print(f"A legtöbb mérés a {legnagyobb_i + 1} helyen volt.")
