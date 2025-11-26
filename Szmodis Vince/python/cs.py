forras =open ('Szmodis Vince\\python\\cs.csv', mode = 'r', encoding= 'utf-8')
idopont=[]
palya=[]
csapat=[]
pontszam=[]
pont_kulonbseg=[]
eredmeny=[]
forras.readline()

for sor in forras:
    adat=sor.strip().split(';')
    idopont.append(adat[0])
    palya.append(adat[1])
    csapat.append(adat[2])
    pontszam.append(int(adat[3]))
    pont_kulonbseg.append(int(adat[4]))
    eredmeny.append(adat[5])

print(f'{len(idopont)/2} meccs adatai vannak az állományban.')

elso_meccs=idopont[0]
for i in range(len(idopont)):
    if elso_meccs>idopont[i]:
        elso_meccs=idopont[i]
print(f'{elso_meccs} időpontban volt az első meccs.')

'''
for i in range(len(idopont)-1):
    for j in range(len(idopont)-1-i):
        if pont_kulonbseg[j]>pont_kulonbseg[j+1]:
            pont_kulonbseg[j+1],pont_kulonbseg[j] = pont_kulonbseg[j],pont_kulonbseg[j+1] 

'''


print(f'{len(palya)/2} pályán folytak a meccsek')

meccs_db_extrasalt=0
for i in range(len(idopont)):
    if csapat[i]=='Extra Salt':
        meccs_db_extrasalt+=1
print(f'{meccs_db_extrasalt} alkalommal játszott az Extra Salt')

nyert_extrasalt=0
dontetlen_extrasalt=0
vesztett_extrasalt=0


