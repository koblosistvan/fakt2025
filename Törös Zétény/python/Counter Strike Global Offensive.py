forras = open("Törös Zétény\python\cs.csv", mode= "r", encoding= "utf-8")
forras.readline()
idopont = []
palya = []
csapat = []
pont = []
pont_kulonbseg = []
eredmeny = []
sorok = 0
for sor in forras:
    adat = sor.strip().split(";")
    idopont.append(str(adat[0]))
    palya.append(str(adat[1]))
    csapat.append(str(adat[2]))
    pont.append(int(adat[3]))
    pont_kulonbseg.append(int(adat[4]))
    eredmeny.append(str(adat[5]))
    sorok += 1
forras.close()
#1.feladat:
print(f"Az állományban {sorok/2:.0f} mecs adatai szerepelnek")

#2.feladat:
legregebb = idopont[0]
for i in range(sorok):
    if idopont[i] < legregebb:
        legregebb = idopont[i]
print(f"A legrégebb mecs {legregebb} ban játszódott.")

#3.feladat:
for i in range(sorok):
    for j in range()