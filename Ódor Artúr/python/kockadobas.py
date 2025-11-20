import random

dobasok = []
for i in range(random.randint(100, 120)):
    dobasok.append(random.randint(1, 6))

print(f"{len(dobasok)} darab dobas volt")
print(f"{sum(dobasok)} a dobások összege")
print(f"{sum(dobasok) / len(dobasok) :.2f} volt a dobások átlaga")
for i in dobasok:                           # az i arra utal, hogy egy indexet tárolsz benne
    if i == 6:                              # szerencsésebb lenne a for dobas in dobasok
        print(f"Van hatos dobás.")          # ez a konvenció: for item in items
        break                               # a lista/tömb neve többesszámú és amikor ciklussal bejárod, akkor egyesszámban használod
else:
    print("Nincs hatos dobás")

keresett_sz = int(input("Adj meg egy számot amit keresel: "))
for i in range(len(dobasok)):                               
    if keresett_sz == dobasok[i]:
        print(f"{i}. sorszámú elem ugyan az a szám.")       # ugyanaz - egybe kell írni
if keresett_sz not in dobasok:
    print(f"A {keresett_sz} nem lett dobva.")               # kicsit még dolgozzunk a magyar nyelvi kifejezőkésségen :)
                                                            # pl. "A(z) {keresett_sz} szám nem szerepel a dobások között." 
primek = [2,3,5]                                            # vagy: "A keresett számot nem dobtuk."
tetszoleges_sz = int(input("Adj meg egy tetszőleges számot: "))
szamlalo_t = 0
szamlalo_p = 0
for i in range(len(dobasok)):
    if tetszoleges_sz == dobasok[i]:
        szamlalo_t += 1
    if dobasok[i] in primek:
        szamlalo_p += 1
print(f"{szamlalo_t} alkalommal fordult elő a {tetszoleges_sz}. Ez {szamlalo_t / len(dobasok) * 100:.2f}%")
print(f"{szamlalo_p} alkalommal lett prímszám dobva. Ez {szamlalo_p / len(dobasok) * 100:.2f}%")                # ... alkalommal dobtunk prímszámot...
print(f"A legkisebb dobott szám a {min(dobasok)}")
print(f"A legnagyobb dobott szám a {max(dobasok)}")