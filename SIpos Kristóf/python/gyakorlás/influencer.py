#1.Fájl
forras=open('fakt2025\\Sipos Kristóf\\python\\gyakorlás\\influencer_format_a.txt', mode='r', encoding='utf-8')
forras.readline()
year=[]
month=[]
day=[]
date=[]
name=[]
views=[]
likes=[]
share=[]
comments=[]
for sor in forras:
    adat=sor.strip().split('\t')
    date.append(str(adat[0]))
    name.append(str(adat[1]))
    views.append(int(adat[2]))
    likes.append(int(adat[3]))
    share.append(int(adat[4]))
    comments.append(int(adat[5]))
    datum = adat[0].split('-')
    year.append(int(datum[0]))
    month.append(int(datum[1]))
    day.append(int(datum[2]))  
forras.close

összes_adat=len(name)

#2.Fájl

#3.Fájl

#4.Fájl

#2.feladat
februárban_megjelent=0
for i in range(összes_adat):
    if year[i] == 2025 and month[i]==2:
        februárban_megjelent+=1
print(f'{februárban_megjelent}')

#3.feladat
eltelt_idő=0
for i in range(összes_adat):


#4.feladat


#5.feladat
legtöbb_megosztás=share[0]
legtöbb_megosztás_datum=date[0]
legtöbb_megosztás_neve=name[0]
for i in range(összes_adat):
    if share[i]>legtöbb_megosztás:
        legtöbb_megosztás=share[i]
        legtöbb_megosztás_datum=date[i]
        legtöbb_megosztás_neve=name[i]
print(f'A legtöbb megosztást szerzett videó {legtöbb_megosztás_datum} lett feltöltve és a neve {legtöbb_megosztás_neve}.' )

#6.feladat

#7.feladat


#8.feladat
for i in range(összes_adat):
    if views[i]>100000 and share[i]<1000:
        print('Volt ilyen')
        break
else:
    print('nem volt ilyen')

#9.feladat

#10.feladat
