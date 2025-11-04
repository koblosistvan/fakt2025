import random

osztalyletszam = random.randint(15, 20)
jegyek = []
for i in range(osztalyletszam):
    jegyek.append(random.randint(1, 5))
print(f"A listta {osztalyletszam} elemet tartalmaz.")
print(f"Az osztályzatok összege {sum(jegyek)}")
print(f"Az osztályzatok átlaga {sum(jegyek) / osztalyletszam :.1f}")

for i in jegyek:
    if i == 1:
        print("Van elégtelen osztályzat.")
        break
else:
    print("Nincs elégtelen osztályzat.")

osztalyzat = int(input("Adj meg egy keresett osztályzatot: "))
elofordul = []
szamlalo = 0

for i in range(osztalyletszam):
    if osztalyzat == jegyek[i]:
        elofordul.append(i)
    if jegyek[i] > 3:
        szamlalo += 1
if len(elofordul) > 0:
    print(f"Az osztályzatok között a {osztalyzat} előfordulásai: {elofordul}")
else:
    print(f"A {osztalyzat} nincs a jegyek közt.")
    
print(f"Az {osztalyzat} az {len(elofordul)} alkalommal fordul elő.")
print(f"{szamlalo} db jegy volt jobb 3-asnál.")
print(f"{szamlalo / osztalyletszam * 100:.0f}% volt jobb, mint 3.")
print(f"A legkisebb osztályzat {min(jegyek)}\nA legnagyobb osztályzat {max(jegyek)}")