számla = [245,-60,150.8,2350,-125.5,-98,-311,100,-28,-185,
             555.6,600,-45.3,-100,-36.9,50,-895,-225,120,215.5]
#1.feladat - Hány alkalommal vontak le pénzt a bankszámláról, hányszor utaltak rá pénzt?
utalas = []
levonas = []

for i in range(len(számla)):
    if számla[i] < 0:
        levon += 1
        levonas.append(számla[i])
    else:
        utal += 1
        utalas.append(számla[i])
print(f"{len(levonas)}-ször vontak le pénzt a számláról és {len(utalas)}-ször utaltak a számlára")

#2.feladat - Mennyi a jóváírások és levonások összege külön-külön?
print(f"A levonások összege: {sum(levonas)}, utalások összege: {sum(utalas)}")

#3.feladat - Hányszor utaltak a számlára aprópénzes összeget?


#4.feladat - Összesen mennyi aprópénzt utaltak a számlára (eurócentben)?

        
#5.feladat - Hány esetben utaltak legalább száz eurót a számlára?
nagyob100 = 0
for i in range(len(utalas)):
    if utalas[i] > 100:
        nagyob100 += 1
print(f"Ennyiser utaltak többet mint 100 eurót: {nagyob100}")

#6.feladat - Melyik a legnagyobb jóváírás és a legnagyobb levonás? Melyik a legkisebb jóváírás?
print(f"A legnagyobb levonás: {min(levonas)} és a legkisebb levonás: {max(levonas)}, A legnagyobb utalás: {max(utalas)} a legkisebb utalás {min(utalás)}")

#7.feladat - Hányadik sorszámú tranzakció az 50 eurós összeg? Ha a levonásokat nem számítjuk, akkor hányadik?
index50 = 0
for i in range(len(számla)):
    if számla[i] != 50:
        index50 += 1
    else: 
        index50 += 1
        break
index50minusznelk = 0
for i in range(len(utalas)):
    if utalas[i] != 50:
        index50minusznelk += 1
    else:
        index50minusznelk += 1
        break
print(f"Az {index50}. tranzakció az 50 eurós,és {index50minusznelk}. tranzakció levonások nélkül.")

#8.feladat - Van 500 eurónál nagyobb jóváírás a számlán?
#Írjuk ki az első és az utolsó ilyen utalás sorszámait!
legk500 = 0
legn500 = 0
for i in range(len(számla)):
    if számla[i] > 500 and számla[i] > 0:
        if legk500 != 0:
            legk500 = i
        legn500 = i


#9.feladat - Van-e olyan összeg a számlán, melyet bankautomatából ki lehet venni
#kizárólagosan 10 eurós bankjegyeket választva a kiadáshoz?

    
#10.feladat - Ha minden utalás és levonás után még tranzakciónként 0,75 fontot pluszban levontak a számláról,
#mennyi pénz maradt rajta a nap végén? És, ha csak az utalásoknál vonták le ezt az illetéket?
