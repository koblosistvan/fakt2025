<<<<<<< HEAD
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
=======
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
print()
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

palyak=[]
for i in range(len(idopont)):
    if palya[i] not in palyak:
        palyak.append(palya[i])
print(f'{len(palyak)} féle pályán folytak a meccsek')
print()
meccs_db_extrasalt=0
for i in range(len(idopont)):
    if csapat[i]=='Extra Salt':
        meccs_db_extrasalt+=1
print(f'Extra Salt csapat: \n\t{meccs_db_extrasalt} alkalommal játszott  ')


nyert_extrasalt=0
dontetlen_extrasalt=0
vesztett_extrasalt=0
for i in range(len(idopont)):
    if csapat[i]=='Extra Salt' and eredmeny[i]=='győzelem':
        nyert_extrasalt+=1
    elif csapat[i]=='Extra Salt' and eredmeny[i]=='vereség':
        vesztett_extrasalt+=1
    elif csapat[i]=='Extra Salt' and eredmeny[i]=='döntetlen':
        dontetlen_extrasalt_extrasalt+=1
print(f'\t{nyert_extrasalt} alkalommal nyert\n\t{dontetlen_extrasalt} alkalommal játszott döntetlent\n\t{vesztett_extrasalt} alkalommal szenvedett vereséget')

legnagyobb_pontkul=pont_kulonbseg[0]
legkisebb_pontkul=pont_kulonbseg[0]
for i in range(len(idopont)):
    if legnagyobb_pontkul<pont_kulonbseg[i]:
        legnagyobb_pontkul=pont_kulonbseg[i]
    elif legkisebb_pontkul>pont_kulonbseg[i]:
        legkisebb_pontkul=pont_kulonbseg[i]
print(f'\t{legnagyobb_pontkul} pont volt a legnagyobb pontkülönbsége\n\t{legkisebb_pontkul} volt a legkisebb pontkülönbsége')

ossz_pontkul=0
szamlalo=0
for i in range(len(idopont)):
    if csapat[i]=='Extra Salt':
        ossz_pontkul+=pont_kulonbseg[i]
        szamlalo+=1
print(f'\t{ossz_pontkul/szamlalo} volt  a csapat pontjainak átlaga')
print()


>>>>>>> 6ea5185cb248114b28bc17a948e9b0d7d041b5d5
