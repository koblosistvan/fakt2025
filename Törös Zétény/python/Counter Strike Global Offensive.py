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
'''
for i in range(sorok-1):
    print(f'{i/sorok*100:.2f}%')
    for j in range(sorok-i-1):
        if pont_kulonbseg[j] < pont_kulonbseg[j+1]:
            pont_kulonbseg[j], pont_kulonbseg[j+1] = pont_kulonbseg[j+1], pont_kulonbseg[j]
            idopont[j], idopont[j+1] = idopont[j+1], idopont[j]
            palya[j], palya[j+1] = palya[j+1], palya[j]
            csapat[j], csapat[j+1] = csapat[j+1], csapat[j]
            pont[j], pont[j+1] = pont[j+1], pont[j]
            eredmeny[j], eredmeny[j+1] = eredmeny[j+1], eredmeny[j]
'''
#print(pont_kulonbseg[:1000])

#4.feladat:
palyak = []
for i in range(sorok):
    if palya[i] not in palyak:
        palyak.append(palya[i])
print(f"Az adatok szerint {len(palyak)} pályán játszottak a csapatok.")

#5.feladat:
mecsek = 0
nyert = 0
vesztett = 0
dontetlen = 0
pontkul = 0
for i in range(sorok):
    if csapat[i] == 'Extra Salt':
        mecsek += 1
        pontkul += pont_kulonbseg[i]
        if eredmeny[i] == 'győzelem':
            nyert += 1
        elif eredmeny[i] == 'vereség':
            vesztett += 1
        elif eredmeny[i] == 'döntetlen':
            dontetlen += 1
print(f"Az Extra Salt összesen {mecsek} mecset játszott amiből {nyert} nyert meg {dontetlen} lett döntetlen és végül {vesztett} mecset vesztett el, az átlagos pontkülönbségük: {pontkul/mecsek:.2f} ")