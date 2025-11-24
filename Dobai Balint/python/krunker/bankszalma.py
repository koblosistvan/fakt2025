szamla = [245,-60,150.8,2350,-125.5,-98,-311,100,-28,-185,
             555.6,600,-45.3,-100,-36.9,50,-895,-225,120,215.5]
#1.feladat - Hány alkalommal vontak le pénzt a bankszámláról, hányszor utaltak rá pénzt?
feltoltes =0
levonas = 0
for i in range(len(szamla)):
    if szamla[i] > 0:
        feltoltes +=1
    if szamla[i] < 0:
        levonas +=1
print(f'{levonas} alkalommal vontak le és {feltoltes} alkalommal toltottek fel penzt a szamlara')



#2.feladat - Mennyi a jóváírások és levonások összege külön-külön?
joir =[]

#3.feladat - Hányszor utaltak a számlára aprópénzes összeget?
apro_db = 0
for i in range(len(szamla)):
    if szamla[i] %1 !=0:
        apro_db +=1
print(f'{apro_db} alkalommal utaltak apropenzes osszeget')
#4.feladat - Összesen mennyi aprópénzt utaltak a számlára (eurócentben)?

        
#5.feladat - Hány esetben utaltak legalább száz eurót a számlára?
tbbomintszaz = 0
for i in range(len(szamla)):
    if szamla[i] > 100:
        tbbomintszaz +=1
print(f'{tbbomintszaz} db utalas van ami 100 felett volt')


#6.feladat - Melyik a legnagyobb jóváírás és a legnagyobb levonás? Melyik a legkisebb jóváírás?
max_jova = szamla[0]
max_levonas = szamla[0]
for i in range(len(szamla)):
    if szamla[i] > max_jova:
        max_jova = szamla[i]
print(f'a legnagyobb jovahagyas {max_jova}')
for i in range(len(szamla)):
    if szamla[i] < max_levonas:
        max_levonas = szamla[i]
print(f'a legnagyobb levonas {max_levonas}')

#7.feladat - Hányadik sorszámú tranzakció az 50 eurós összeg? Ha a levonásokat nem számítjuk, akkor hányadik?
otvenes = 0
for i in range(len(szamla)):



#8.feladat - Van 500 eurónál nagyobb jóváírás a számlán?
#Írjuk ki az első és az utolsó ilyen utalás sorszámait!


#9.feladat - Van-e olyan összeg a számlán, melyet bankautomatából ki lehet venni
#kizárólagosan 10 eurós bankjegyeket választva a kiadáshoz?

    
#10.feladat - Ha minden utalás és levonás után még tranzakciónként 0,75 fontot pluszban levontak a számláról,
#mennyi pénz maradt rajta a nap végén? És, ha csak az utalásoknál vonták le ezt az illetéket?
