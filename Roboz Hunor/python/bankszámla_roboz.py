szamla = [245,-60,150.8,2350,-125.5,-98,-311,100,-28,-185,555.6,600,-45.3,-100,-36.9,50,-895,-225,120,215.5]
osszeg = 0
for i in range(len(szamla)):
    osszeg += szamla[i]
print("Összeg:", osszeg)

terhelesek_szama = 0
for i in range(len(szamla)):
    if szamla[i] < 0:
        terhelesek_szama += 1
print("Terhelések száma:", terhelesek_szama)

legnagyobb_ertek = szamla[0]
for i in range(len(szamla)):
    if szamla[i] > legnagyobb_ertek:
        legnagyobb_ertek = szamla[i]
print("Legnagyobb érték:", legnagyobb_ertek)

pozitiv_ertekek = []
for i in range(len(szamla)):
    if szamla[i] > 0:
        pozitiv_ertekek.append(szamla[i])
legkisebb_pozitiv = min(pozitiv_ertekek)
print("Legkisebb jóváírás:", legkisebb_pozitiv)

atlag = 0
pozitiv_db = 0
for i in range(len(szamla)):
    if szamla[i] > 0:
        atlag += szamla[i]
        pozitiv_db += 1
atlag = atlag / pozitiv_db
print(f"Pozitív átlag: {atlag:.2f}")

osszeg_uj = 0
for i in range(len(szamla)):
    osszeg_uj += szamla[i]
if osszeg_uj > 0:
    print("A számla pozitív egyenlegű")
elif osszeg_uj < 0:
    print("A számla negatív egyenlegű")
else:
    print("A számla egyenlege nulla")