forras=open('SIpos Kristóf\\Közúti ellenőrzés\\kozut.txt', mode='r' , encoding='utf-8')
forras.readline()

ora=[]
perc=[]
mp=[]
sebesseg=[]
rendszam=[]

for sor in forras:
    adat=sor.strip().split(' ')
    ora.append(int(adat[0]))
    perc.append(int(adat[1]))
    mp.append(int(adat[2]))
    sebesseg.append(int(adat[3]))
    rendszam.append(adat[4])

forras.close
adatok_szama=len(rendszam)

# 1.Feladat
print('1.Feladat')
sebesseg_nagyobb_mint_50=0
for i in range(adatok_szama):
    if sebesseg[i]>50:
        sebesseg_nagyobb_mint_50+=1
print(f'{sebesseg_nagyobb_mint_50} ember ment gyorsabban 50km/h-nál.')

# 2.Feladat
print('2.Feladat')
for i in range(adatok_szama):
    if sebesseg[i]>55:
        break
    elif i==adatok_szama :
        print('Nincs olyan aki 55 km/h-nál gyorsabban ment.')
print('Volt olyan aki 55 km/h-nál többel ment')

# 3.Feladat
print('3.Feladat')
leggyorsabb_auto_sebesseg=0
leggyorsabb_auto=str(0)
for i in range(adatok_szama):
    if sebesseg[i]> leggyorsabb_auto_sebesseg:
        leggyorsabb_auto_sebesseg=sebesseg[i]
        leggyorsabb_auto=rendszam[i]
print(f'A leggyorsabb auto az a {leggyorsabb_auto} rendszámú autó volt és {leggyorsabb_auto_sebesseg}km/h-val ment.')
# 4.Feladat
print('4.Feladat')
print(f'Az áthaladó autók átlagsebessége {round(sum(sebesseg)/adatok_szama)}km/h volt.')
# 5.Feladat
print('5.Feladat')
kozut_kimenet=open('SIpos Kristóf\\Közúti ellenőrzés\\kozut-kimenet', mode='w',encoding='utf-8')
for i in range(adatok_szama):
    if sebesseg[i]< 30:
        kozut_kimenet.write(str(ora[i]))
        kozut_kimenet.write(':')
        kozut_kimenet.write(str(perc[i]))
        kozut_kimenet.write(':')
        kozut_kimenet.write(str(mp[i]))
        kozut_kimenet.write(' ')
        kozut_kimenet.write(str(sebesseg[i]))
        kozut_kimenet.write(' ')
        kozut_kimenet.write(rendszam[i])
        kozut_kimenet.write('\n')
# 6.Feladat
print('6.Feladat')
for i in range(2):
    for j in range(2-i-1):
        if sebesseg[j]> sebesseg[j+1]:
            sebesseg[j],sebesseg[j+1]=sebesseg[j+1],sebesseg[j]
            ora[j],ora[j+1]=ora[j+1],ora[j]
            perc[j],perc[j+1]=perc[j+1],perc[j]
            mp[j],mp[j+1]=mp[j+1],mp[j]
            rendszam[j],rendszam[j+1]=rendszam[j+1],rendszam[j]
kozut_kimenet.write(str(ora[i]))
kozut_kimenet.write(':')
kozut_kimenet.write(str(perc[i]))
kozut_kimenet.write(':')
kozut_kimenet.write(str(mp[i]))
kozut_kimenet.write(' ')
kozut_kimenet.write(str(sebesseg[i]))
kozut_kimenet.write(' ')
kozut_kimenet.write(rendszam[i])
kozut_kimenet.write('\n')
# 7.Feladat
print('7.Feladat')
# 8.Feladat
print('8.Feladat')
# 9.Feladat
print('9.Feladat')
# 10.Feladat
print('10.Feladat')