forras = open("Törös Zétény\\python\\futar.txt", mode="r", encoding="utf-8")
forras.readline()
nap, fuvar, hossz = [], [], []
for sor in forras:
    adat = sor.strip().split(" ")
    nap.append(int(adat[0]))
    fuvar.append(int(adat[1]))
    hossz.append(int(adat[2]))
forras.close
#1.feladat:
legh = 0
legh_index = 0
for i in range(len(hossz)):
    if hossz[i] > legh:
        legh = hossz[i]
        legh_index = i

print(f"A leghosszabb út: {nap[legh_index]}. nap, {fuvar[legh_index]}. fuvar - {legh}km ")

#2.feladat:
ossszut = 0
for i in range(len(hossz)):
    if nap[i] == 3:
        ossszut += hossz[i]
print(f"A harmadik napon összesen {ossszut}km-t tett meg.")

#3.feladat:
negy = 0
for i in range(len(nap)):
    if nap[i] == 4:
        negy += 1
print(f"A negyedik napon {negy} fuvart teljesített.")

#4.feladat:
for i in range(len(hossz)):
    if hossz[i] > 20:
        print("A futárnak volt 20 km-nél nagyobb útja.")
        break
else:
    print("A futárnak nem volt 20 km-nél nagyobb útja.")

#5.feladat:
for i in range(len(fuvar)):
    if fuvar[i] == 1:
        print(f"{nap[i]}. nap: {hossz[i]}")

#bónusz:
