import random

osztalyzatok = []

for i in range(15, 20):
    osztalyzatok.append(random.randint(1, 5))

oszt_sum = sum(osztalyzatok)
oszt_hossz = len(osztalyzatok)

print(f"Az osztályzatok száma: {len(osztalyzatok)}")
print(f"Az osztályzatok összege: {sum(osztalyzatok)}")
print(f"Az osztályzatokátlaga: {oszt_sum/oszt_hossz:.1f}")

for i in range(oszt_hossz):
    if osztalyzatok[i] == 1:
        print("Van elégtelen osztályzat.")
        break
else:
    print("Nincs elégtelen osztályzat.")

szam = int(input("Add meg a keresett osztályzatot: "))
eloford_index = []

for i in range(oszt_hossz):
    if osztalyzatok[i] == szam:
        eloford_index.append(i)
    

if len(eloford_index) > 0:
    print(f"A {szam}-es osztályzat az osztályzatok {eloford_index } helyein jelennek meg ")
else:
        print(f"Nem fordul elő a {szam}-es osztáyzat az osztályzatok között.")

negy = 0
ot = 0

for i in range(oszt_hossz):
    if osztalyzatok == 4:
        negy += 1
    if osztalyzatok == 5:
        ot += 1

if negy > 0 or ot > 0:
    print(f"A 3-as nál jobb jegyek aránya: {ot} ötös és {negy} negyes")
else:
    print("Nem volt jobb jegy 3-as nál")

legkisebb = 5
legnagyobb = 1

for i in range(oszt_hossz):
    if osztalyzatok[i] < legkisebb:
        legkisebb = osztalyzatok [i]
    if osztalyzatok[i] > legnagyobb:
        legnagyobb = osztalyzatok[i]

print(f"A legkisebb osztályzat: {legkisebb} és a legnagyobb osztályzat: {legnagyobb}")