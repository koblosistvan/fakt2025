meresek_szama = 16
szamok = [36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]

def f(n):
    print(f"\n{n}. feladat")



f(2)
osszes = 0
for i in range(meresek_szama):
    if szamok[i] > 0:
        osszes += szamok[i]
print(f"Összesen {osszes} kerékpárost számoltak meg.")

f(3)
print("Óránkénti mérések:")
osszes = 0
ora = 6
szamlalo = 0
for a in szamok:
    szamlalo += 1
    if a > 0:
        osszes += a
    if szamlalo == 4:
        print(f"{ora} órától {osszes} kerékpáros")
        osszes = 0
        ora += 1
        szamlalo = 0

f(4)
max_id = 0
max = szamok[0]
for i in range(1, meresek_szama):
    if szamok[i] > max:
        max = szamok[i]
        max_id = i
print(f"Az áthaladók maximális száma: {max}; a rögzítés időpontja: {(max_id+1)//4+6}:{(max_id+1)%4/4*60:.0f}")
