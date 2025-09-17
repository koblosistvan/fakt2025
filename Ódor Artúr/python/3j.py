kerdes = int(input("Melyik számrendszerbe akarsz váltani? "))
szam = int(input("Adj meg egy számot: "))
eredmeny = ""
while szam > 0:
    maradek = szam % kerdes
    eredmeny = str(maradek) + eredmeny
    szam = (szam - maradek) // kerdes
print(eredmeny)


