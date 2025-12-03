import random

dobasok = []
for i in range(random.randint(100, 120)):
    dobasok.append(random.randint(1, 6))
#1.feladat:
print(f"A szimuláció során {len(dobasok)} dobás történt.")

#2.feladat:
print(f"A dobott számok összege: {sum(dobasok)}")

#3.feladat:
print("A dobott számok átlaga: ", sum(dobasok)/len(dobasok))

#4.feladat:
for i in range(len(dobasok)):
    if dobasok[i] == 6:
        print("A dobások között volt hatos dobás.")
        break
else:
    print("A dobások között nincs hatos dobás.")

#5.feladat:
szam = int(input("Melyik számot keresed a dobások között: "))
index = []
for i in range(len(dobasok)):
    if dobasok[i] == szam:
        index.append(i)
print(f"A {szam} ezeken a helyeken található meg a dobások között: {index} és az első előfordulási helye: {index[0]}")

#6.feladat:
egy = 0
primek = 0 
for i in range(len(dobasok)):
    if dobasok[i] == 3 or dobasok[i] == 2 or dobasok[i] == 5:
        primek += 1
    if dobasok[i] == 1:
        egy += 1
print(f"Az egyes szám {egy} alaklommal volt kidobva, a dobások között {primek} alkalommal volt prímszám aminek a százalékos arány: {primek/len(dobasok)*100:.1f}%")

#7.feladat:
legk = 6
legn = 1
for i in range(len(dobasok)):
    if dobasok[i] < legk:
        legk = dobasok[i]
    if dobasok[i] > legn:
        legn = dobasok[i]
print(f"A legnagyobb dobás: {legn}, és a legkisebb dobás: {legk}")

















67