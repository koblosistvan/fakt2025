elso_szam = int(input("Adj meg egy számot: "))
masodik_szam = int(input("Adj meg még egy számot"))

if elso_szam > masodik_szam:
    osztas = elso_szam % masodik_szam
    if osztas == 0:
        print("osztható")
    else:
        print("nem osztható")

else:
    osztas = masodik_szam % elso_szam
    if osztas == 0:
        print("oszthato")
    else:
        print("nem oszthato")