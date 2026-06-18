#1.Fájl
forras=open('SIpos Kristóf\\python\\gyakorlás\\influencer_format_a.txt', mode='r', encoding='utf-8')#'fakt2025\\Sipos Kristóf\\python\\gyakorlás\\influencer_format_a.txt'
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
forras=open('SIpos Kristóf\\python\\gyakorlás\\influencer_format_b.txt', mode='r', encoding='utf-8')#'fakt2025\\Sipos Kristóf\\python\\gyakorlás\\influencer_format_a.txt'
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

#3.Fájl
forras=open('SIpos Kristóf\\python\\gyakorlás\\influencer_format_c.txt', mode='r', encoding='utf-8')#'fakt2025\\Sipos Kristóf\\python\\gyakorlás\\influencer_format_a.txt'
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
    adat=sor.strip().split(' ')
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

#4.Fájl
forras=open('SIpos Kristóf\\python\\gyakorlás\\influencer_format_d.txt', mode='r', encoding='utf-8')#'fakt2025\\Sipos Kristóf\\python\\gyakorlás\\influencer_format_a.txt'
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
    adat=sor.strip().split(';')
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

def f(szám):
    print(f'\n{szám}.feladat')


#2.feladat
f(2)
februárban_megjelent=0
for i in range(összes_adat):
    if year[i] == 2025 and month[i]==2:
        februárban_megjelent+=1
print(f'{februárban_megjelent}')

#3.feladat
f(3)
utolsó_feltöltés=day[összes_adat-1]+31+28+31+30+31+30+31+31+30+31+30+25
eltelt_idő=utolsó_feltöltés-day[0]
átlagos_idő=eltelt_idő//összes_adat
print(f'Átlagosan {átlagos_idő} nap telik el 2 poszt között.')
#4.feladat
f(4)
februárban_kedvelések=[]
februárban_hozzászólások=[]
for i in range(összes_adat):
    if month[i]==2:
        februárban_kedvelések.append(likes[i])
        februárban_hozzászólások.append(comments[i])
print(f'A hozzászólások és a kedvelések aránya februárban {round(sum(februárban_kedvelések)/sum(februárban_hozzászólások),3)} összesen meg {round(sum(likes)/sum(comments),3)}.')


#5.feladat
f(5)
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
f(6)
hónap_1=int(input('Add meg az első hónapot: '))
nap_1=int(input('Add meg az első napot: '))
hónap_2=int(input('Add meg hogy melyik hónapból nézzük az első számot: '))
nap_2=int(input('Add meg hogy melyik naptól nézzük az első számot: '))
if hónap_2 == 2:
    nap_2=nap_2+31
elif hónap_2 == 3:
    nap_2=nap_2+31+28
elif hónap_2 == 4:
    nap_2=nap_2+31+28+31
elif hónap_2 == 5:
    nap_2=nap_2+31+28+31+30
elif hónap_2 == 6:
    nap_2=nap_2+31+28+31+30+31
elif hónap_2 == 7:
    nap_2=nap_2+31+28+31+30+31+30
elif hónap_2 == 8:
    nap_2=nap_2+31+28+31+30+31+30+31
elif hónap_2 == 9:
    nap_2=nap_2+31+28+31+30+31+30+31+31
elif hónap_2 == 10:
    nap_2=nap_2+31+28+31+30+31+30+31+31+30
elif hónap_2 == 11:
   nap_2= nap_2+31+28+31+30+31+30+31+31+30+31
elif hónap_2 == 12:
    nap_2=nap_2+31+28+31+30+31+30+31+31+30+31+30
elif hónap_2 == 1:
    nap_2=nap_2+0
else:
    print('Számba add meg a hónapot vagy adj meg létező hónapot.')
if hónap_1 or hónap_2 == 2 and nap_1 or nap_2 > 29:
    print('Ezt te is tudod hogy helytelen.') 
    
eltelt_napok_száma=nap_2-nap_1
print(f'A kettő dátum közötti eltelt napok száma {eltelt_napok_száma}')





#7.feladat
f(7)
leghosszabb_tétlenség=0
leghosszabb_tétlenség_nap_1=0
leghosszabb_tétlenség_nap_2=0
for i in range(összes_adat):
    if day[i]-day[i-1]>leghosszabb_tétlenség:
        leghosszabb_tétlenség=day[i]-day[i-1]
        leghosszabb_tétlenség_nap_1=date[i-1]
        leghosszabb_tétlenség_nap_2=date[i]

print(f'A leghosszabb tétlenség {leghosszabb_tétlenség} nap volt és {leghosszabb_tétlenség_nap_1} és {leghosszabb_tétlenség_nap_2} között')

#8.feladat
f(8)
for i in range(összes_adat):
    if views[i]>100000 and share[i]<1000:
        print('Volt ilyen')
        break
else:
    print('nem volt ilyen')

#9.feladat
f(9)
legtöbb_megtekintés_1=0
legtöbb_megtekintés_2=0
legtöbb_megtekintés_3=0
legtöbb_megtekintés_4=0
legtöbb_megtekintés_5=0
legtöbb_megtekintés_6=0
legtöbb_megtekintés_7=0
legtöbb_megtekintés_8=0
legtöbb_megtekintés_9=0
legtöbb_megtekintés_10=0
szortírozott_megtekintések = views.copy()
while legtöbb_megtekintés_1 < legtöbb_megtekintés_2 and legtöbb_megtekintés_2 < legtöbb_megtekintés_3 and legtöbb_megtekintés_4 < legtöbb_megtekintés_5 and legtöbb_megtekintés_5 < legtöbb_megtekintés_6 and legtöbb_megtekintés_6 < legtöbb_megtekintés_7 and legtöbb_megtekintés_7 < legtöbb_megtekintés_8 and legtöbb_megtekintés_8 < legtöbb_megtekintés_9 and legtöbb_megtekintés_9 < legtöbb_megtekintés_10:
    for i in range(összes_adat):
        if szortírozott_megtekintések[i] > szortírozott_megtekintések[i-1]:
            szortírozott_megtekintések[i-1]=szortírozott_megtekintések[i]
            szortírozott_megtekintések[i]=szortírozott_megtekintések[i-1]
print(f'A 10 legnagyobb megtekintés csökkenő sorrendbe \n{legtöbb_megtekintés_1}\n{legtöbb_megtekintés_2}\n{legtöbb_megtekintés_3}\n{legtöbb_megtekintés_4}\n{legtöbb_megtekintés_5}\n{legtöbb_megtekintés_6}\n{legtöbb_megtekintés_7}\n{legtöbb_megtekintés_8}\n{legtöbb_megtekintés_9}\n{legtöbb_megtekintés_10}\n')

#10.feladat
f(10)
Unboxing=0
videó_lényege=[]
Unboxing_videók_megtekintései=[]
for i in range(összes_adat):
    név_bontva=adat[1].split('_')
    videó_lényege.append(str(név_bontva[0]))
for i in range(összes_adat):
    if videó_lényege[i]=='Unboxing':
        Unboxing +=1
        Unboxing_videók_megtekintései.append(views[i])
összes_pénz_unboxingból=float(Unboxing*50000)
összes_bevétel_megtekintésekből=sum(Unboxing_videók_megtekintései)*3.14
össz_bevétel=összes_pénz_unboxingból+összes_bevétel_megtekintésekből
print(f'Az össz bevétele unboxingból {össz_bevétel} FT volt.')


