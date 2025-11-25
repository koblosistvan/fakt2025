számla = [245,-60,150.8,2350,-125.5,-98,-311,100,-28,-185,
             555.6,600,-45.3,-100,-36.9,50,-895,-225,120,215.5]
#1.feladat - Hány alkalommal vontak le pénzt a bankszámláról, hányszor utaltak rá pénzt?
utal = 0
levon = 0
for i in számla:
    if i < 0:
        levon+=1
    elif i > 0:
        utal += 1
print(f'{levon} db levonás és {utal} db utalás volt.')
#2.feladat - Mennyi a jóváírások és levonások összege külön-külön?
sulevo = 0
suossz = 0
for i in számla:
    if i < 0:
        sulevo += i
    else:
        suossz += i
print(f'A levonás {abs(sulevo)} volt, a jóváírás {suossz}.')
#3.feladat - Hányszor utaltak a számlára aprópénzes összeget?
aprsz = 0
for i in számla:
    if int(i) != float(i):
        aprsz += 1
print(f'Összesen {aprsz} aprópénzes utalás volt.')
#4.feladat - Összesen mennyi aprópénzt utaltak a számlára (eurócentben)?
apros = 0
for i in számla:
    if int(i) != float(i):
        apros += i
print(f'Összesen {apros} aprócentes utalás volt.')
#5.feladat - Hány esetben utaltak legalább száz eurót a számlára?
szazcount=0
for i in számla:
    if i >= 100:
        szazcount += 1
print(f'Összesen {szazcount} száz euró fölötti utalás volt.')
#6.feladat - Melyik a legnagyobb jóváírás és a legnagyobb levonás? Melyik a legkisebb jóváírás?
legnjo = 0
legkijo = max(számla)
legnle = min(számla)
for i in számla:
    if i > legnjo and i > 0:
        legnjo = i
    elif i < legkijo and i > 0:
        legkijo = i
    elif i < legnle and i < 0:
        legnle = i
print(f'A legnagyobb jóváírás {legnjo}, a legnagyobb levonás {abs(legnle)}, a legkisebb utalás {legkijo} volt.')
#7.feladat - Hányadik sorszámú tranzakció az 50 eurós összeg? Ha a levonásokat nem számítjuk, akkor hányadik?
ind = 0
for i in range(len(számla)):
    if számla[i] == 50:
        ind = i+1
print(f'Az 50 eurós összeg {ind}. tranzakció volt.')
#8.feladat - Van 500 eurónál nagyobb jóváírás a számlán?
#Írjuk ki az első és az utolsó ilyen utalás sorszámait!
for i in számla:
    if i > 500:
        print('Van 500 eurónál nagyobb jóváírás a számlán.')
        break
else:
    print('Nincs 500 eurónál nagyobb jóváírás a számlán.')
na500 = []
for i in range(len(számla)):
    if számla[i]> 500:
        na500.append(i+1)
print(f'Első: {na500[0]}.\nUtolsó: {na500[-1]}.')
#9.feladat - Van-e olyan összeg a számlán, melyet bankautomatából ki lehet venni
#kizárólagosan 10 eurós bankjegyeket választva a kiadáshoz?
for i in számla:
    if i%10==0:
        print('Van olyan összeg.')
        break
else:
    print('Nincs olyan összeg.')
#10.feladat - Ha minden utalás és levonás után még tranzakciónként 0,75 fontot pluszban levontak a számláról,
#mennyi pénz maradt rajta a nap végén? És, ha csak az utalásoknál vonták le ezt az illetéket?
minden = 0
csaku = 0
for i in számla:
    minden += (i-0.75)
    if i > 0:
        csaku += (i-0.75)
    else:
        csaku += i
print(f'A nap végén alapesetben {minden} pénz maradt a számlán, csak utalásos levonásnál pedig {csaku}')


