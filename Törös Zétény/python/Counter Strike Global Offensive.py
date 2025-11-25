forras = open("Törös Zétény\python\cs.csv", mode= "r", encoding= "utf-8")
forras.readline()
idopont = []
palya = []
csapat = []
pont = []
pont_kulonbseg = []
eredmeny = []
for sor in forras:
    adat = sor.strip().split(";")
    idopont.append(str(adat[0]))
    palya.append(str(adat[1]))
    csapat.append(str(adat[2]))
    pont.append(int(adat[3]))
    