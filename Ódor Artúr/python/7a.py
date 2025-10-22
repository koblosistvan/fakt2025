forras = open("Ódor Artúr\\python\\7a-lakas-arak.txt", mode="r", encoding="utf-8")
forras.readline()
terulet = []
ar = []
for sor in forras:
    adat = sor.strip().split(" ")
    terulet.append(int(adat[0]))
    ar.append(int(adat[1]))
forras.close
print()
legdragabb_l =ar[0]
legdragabb_l_i = 0
for i in range(1, len(ar)):
    if legdragabb_l <= ar[i]:
        legdragabb_l = ar[i]
        legdragabb_l_i = i
print(f"A {legdragabb_l_i}. lakás volt a legdrágább. {legdragabb_l} millió forint.")
for adat in ar:
    if adat > 500:
        print("Van 500 millió forintnál drágább ingatlan.")
        break
else:
    print("Nincs 500 millió forintnál drágább ingatlan.")

arany_n = ar[0]/terulet[0]
arany_i = 0
for i in range(len(ar)):
    if ar[i]/terulet[i] > arany_n:
        arany_n = ar[i]/terulet[i]
        arany_i = i
print(f"A {arany_i}. ház volt legnagyobb négyzetméterárú lakás.")

szamlalo_h = 0
for adat in ar:
    if adat < 20:
        szamlalo_h += 1
print(f"Húsz millió alatt {szamlalo_h} lakás volt.")



forras = open("Ódor Artúr\\python\\árak.txt", mode="w", encoding="utf-8")

for i in range(len(ar)):
    if terulet[i] > 50 and terulet[i] < 60:
        print(terulet[i], ar[i], file=forras)

min, max = map(int, input("Adj meg egy ár intervallumot (pl.:20-40): ").strip().split("-"))

for i in range(len(ar)):
    if min < ar[i] and max > ar[i]:
        print()