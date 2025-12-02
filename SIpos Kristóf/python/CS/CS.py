Forrás_1=open('Sipos Kristóf\\python\\CS\\cs.csv',mode='r',encoding='utf-8')
Forrás_2=open('Sipos Kristóf\\python\\CS\\match_results.csv',mode='r',encoding='utf-8')
Forrás_1.readline()
idopont=[]
palya=[]
csapat=[]
pont=[]
pont_kulonbseg=[]
eredmeny=[]

év=[]
honap=[]
nap=[]
óra=[]
perc=[]
másodperc=[]

év_hónap_nap=[]
idő=[]
for sor in Forrás_1:
    adat=sor.split(';')
    idopont.append(adat[0])
    palya.append(adat[1])
    csapat.append(adat[2])
    pont.append(int(adat[3]))
    pont_kulonbseg.append(int(adat[4]))
    eredmeny.append(adat[5])
Forrás_1.close
Forrás_2.close
#Feladat 1
adatok_szama=len(pont)//2
print(f'Ennyi meccs adata van benne {adatok_szama}.')

#Feladat 2
első_meccs=idopont[0]
for i in range(adatok_szama):
    if idopont[i]<első_meccs:
        első_meccs=idopont[i]
print(f'Az első meccs {első_meccs}')
#Feladat 3
min_pont=pont[0]
max_pont=pont[0]
for i in range(adatok_szama):
    if min_pont>pont[i]:
        min_pont=pont[i]
    elif max_pont<pont[i]:
        max_pont=pont[i]
for i in range(adatok_szama):
    j = adatok_szama-i
    if 
print(f'A meccsek sorendje {pont}.')