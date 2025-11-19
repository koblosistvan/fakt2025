forras=open('Sipos Kristóf\\python\\ökolábnyom.csv', mode='r', encoding='utf-8' )

forras.readline()
kód,ország,régió,év,felhasználás,kapacitás,lakosság,gdp=[[] for _ in range(8)]

for sor in forras:
    adat=sor.strip().split(',')
    kód.append(adat[0])
    ország.append(adat[1])
    régió.append(adat[2])
    év.append(int(adat[3]))
    felhasználás.append(float(adat[4]))
    kapacitás.append(float(adat[5]))
    lakosság.append(float(adat[6]))
    if (adat[7]) =='None':
        gdp.append(None)
    else:
        gdp.append(float(adat[7]))
adatok_szama=len(kód)

#Feladat_1
print(f'Feladat 1\nAz adatok száma az {adatok_szama}.')

#Feladat_2
Adatok_2014=0
for i in range(adatok_szama):
    if év[i] == 2014:
        Adatok_2014+= 1
print(f'Feladat 2\n2014-ben {Adatok_2014} országnak volt adata.')

#Feladat_3
Min_év=99999999
Max_év=0
for i in range(adatok_szama):
    if Max_év< év[i]:
        Max_év=év[i]
    elif Min_év> év[i]:
        Min_év=év[i]
print(f'A mért adatok {Min_év}-{Max_év}')
#Feladat_4
Max_kapacitás=0
Max_kapacitás_index=''
for i in range(adatok_szama):
    if kapacitás[i]> Max_kapacitás:
        Max_kapacitás=kapacitás[i]
        Max_kapacitás_index=ország[i]
print(f'A legnagyobb kapacitás {Max_kapacitás} volt {Max_kapacitás_index}-ban.')
#Feladat_5
Min_gdp_ország=''
Min_gdp_év=0
gdp_1emberre=gdp[i]/lakosság[i]
Min_gdp_1emberre=999999999999
for i in range(adatok_szama):
    if Min_gdp_1emberre>gdp_1emberre:
        Min_gdp_1emberre=gdp_1emberre
        Min_gdp_ország=ország[i]
        Min_gdp_év=év[i]
print(f'A legkisebb 1 emberre jutó gdp {Min_gdp_ország}-ban volt {Min_gdp_év} évben és {Min_gdp_1emberre} volt. ')
#Feladat_6
kapacitás_2000=[]
felhasználás_2000=[]
kapacitás_2014=[]
felhasználás_2014=[]
össz_kapacitás_2000=0
össz_felhasználás_2000=0
össz_kapacitás_2014=0
össz_felhasználás_2014=0
for i in range(adatok_szama):
    if év[i]==2000:
        kapacitás_2000.append(kapacitás[i])
        felhasználás_2000.append(felhasználás[i])
    elif év[i] == 2014:
        kapacitás_2014.append(kapacitás[i])
        felhasználás_2014.append(felhasználás[i])
for i in range(len(kapacitás_2000)):
    össz_kapacitás_2000=kapacitás_2000[i]+kapacitás_2000[i-1]
for i in range(len(felhasználás_2000)):
    össz_felhasználás_2000=felhasználás_2000[i]+felhasználás_2000[i-1]
for i in range(len(kapacitás_2014)):
    össz_kapacitás_2014=kapacitás_2014[i]+kapacitás_2014[i-1]
for i in range(len(felhasználás_2014)):
    össz_felhasználás_2014=felhasználás_2014[i]+felhasználás_2014[i-1]
print(f'A teljes kapacitás 2000-ben {össz_kapacitás_2000} volt, a teljes felhasználás {össz_felhasználás_2000} volt\n A teljes kapacitás 2014-ben {össz_kapacitás_2014} volt, a teljes felhsználás {össz_felhasználás_2014} volt.')
#Feladat_7
for i in range(adatok_szama):
    pass
print(f'A két érték aránya {0}-ről {0}-re nőtt.')
#Feladat_8
átlagos_felhasználás_2000=0
átlagos_felhasználás_2014=0
össz_lakos_2000=0
össz_lakos_2014=0
lakosok_2000=[]
lakosok_2014=[]
for i in range(len(kapacitás_2000)):
    if év[i] ==2000:
        lakosok_2000.append(lakosság[i])
    elif év[i] ==2014:
        lakosok_2014.append(lakosság[i])
for i in range(len(kapacitás_2000)):
    össz_lakos_2000=lakosok_2000[i]+lakosok_2000[i-1]
    össz_lakos_2014=lakosok_2014[i]+lakosok_2014[i-1]
for i in range(adatok_szama):
    if év[i] == 2000:
        átlagos_felhasználás_2000=össz_felhasználás_2000/össz_lakos_2000
    elif év[i] == 2014:
        átlagos_felhasználás_2014=össz_felhasználás_2014/össz_lakos_2014
print(f'Az egy személyre jutó felhasználás 2000-ben {átlagos_felhasználás_2000} volt, 2014-ben {átlagos_felhasználás_2014} volt')
#Feladat_9
átlagos_kapacitás_2000=0
átlagos_kapacitás_2014=0
for i in range(adatok_szama):
    if év[i] == 2000:
        átlagos_kapacitás_2000=össz_kapacitás_2000/össz_lakos_2000
    elif év[i] == 2014:
        átlagos_kapacitás_2014=össz_kapacitás_2014/össz_lakos_2014
print(f'Az egy személyre jutó kapacitás 2000-ben {átlagos_kapacitás_2000} volt, 2014-ben {átlagos_kapacitás_2014} volt.')
#Feladat_10
év_határ_fölött=[]
ország_határ_fölött=[]
felhasználás_határ=int(input('Adj meg egy értéket: '))
for i in range(adatok_szama):
    if felhasználás[i]> felhasználás_határ:
        év_határ_fölött.append(év[i])
        ország_határ_fölött.append(ország[i])
print(f'A határ fölött ezek az országok voltak {ország_határ_fölött} ezekben az években {év_határ_fölött}.')