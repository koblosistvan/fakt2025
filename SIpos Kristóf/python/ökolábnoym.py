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

#Feladat 1
print(f'Az adatok száma az {adatok_szama}.')

#Feladat 2
Adatok_2014=0
for i in range(adatok_szama):
    if év[i] == 2014:
        Adatok_2014+= 1
print(f'2014-ben {Adatok_2014} országnak volt adata.')

#Feladat 3
Min_év=99999999
Max_év=0
for i in range(adatok_szama):
    if Max_év< év[i]:
        Max_év=i
    elif Min_év> év[i]:
        Min_év=i
print(f'')
#Feladat 4
for i in range(adatok_szama):
#Feladat 5
for i in range(adatok_szama):
#Feladat 6
for i in range(adatok_szama):
#Feladat 7
for i in range(adatok_szama):
#Feladat 8
for i in range(adatok_szama):
#Feladat 9
for i in range(adatok_szama):
#Feladat 10