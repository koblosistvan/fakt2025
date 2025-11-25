forras= open('Szmodis Vince\\CS\\cs.csv', mode='r', encoding='utf-8')
idopont=[]
palya=[]
csapat=[]
pont=[]
pont_kulombseg=[]
eredmeny=[]

for sor in forras:
    adat=sor.strip().split(';')
    idopont.append(adat[0])