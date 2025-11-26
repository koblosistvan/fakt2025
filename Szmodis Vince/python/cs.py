forras = forras =open ('Szmodis Vince\\python\\cs.csv', mode = 'r', encoding= 'utf-8')
idopont=[]
palya=[]
csapat=[]
pont_kulonbseg=[]
eredmeny=[]


for sor in forras:
    adat=sor.strip().split(';')
    idopont.append(adat[0])
    palya.append(adat[1])
    csapat.append(adat[2])
    pont_kulonbseg.append(adat[3])
    eredmeny.append(adat[4])

