import random

oszt = []
letszam = random.randint(15, 20)

for i in range(letszam):
    oszt.append(random.randint(1,5))
print(f'Ennyi osztályzat van: ', len(oszt))

osszeg = 0

for i in range(letszam):
    osszeg = sum(oszt)

print("Ennyi az osztályzatok összege:", osszeg)
print(f"Ekkora az osztály átlag: {osszeg/letszam:.1f}")

for i in range(letszam):
    if oszt[i] == 1:
        print('Van elégtelen osztályzat.')
        break
else:
    print("Nincs elégtelen az osztályban.")

kereset = int(input("Add meg hogy melyik számot keresed: "))
kereset_index = 0

for i in range(letszam):
    if oszt[i] == kereset:
        kereset_index = i
        print(f"A keresett szám legelősször a {kereset_index}. helyen található meg.")
        break
else:
    print("Nincs ilyen szám az átlagok között")

osztaly = int(input("Add megy hogy mit keressek hogy miből mennyi van: "))
hanyszor = 0

for i in range(letszam):
    if oszt[i] == osztaly:
        hanyszor += 1
print("Ennyi általad keresett osztályzat volt:", hanyszor)

menyi = 0

for i in range(letszam):
    if oszt[i] > 3:
        menyi += 1
print("Ennyi osztályzat jobb közepesnél:", menyi)

leg_kisebb = 5
leg_nagyobb = 1

for i in range(letszam):
    if oszt[i] > leg_nagyobb:
         leg_nagyobb = oszt[i]
    if oszt[i] < leg_kisebb:
        leg_kisebb = oszt[i]

print("A legkisebb szám:", leg_kisebb)
print("A legnagyobb szám:", leg_nagyobb)





67