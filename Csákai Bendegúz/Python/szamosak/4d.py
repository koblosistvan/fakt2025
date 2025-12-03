
forras = open("_Feladatok\\python\\4d-pontok.txt", mode="r", encoding= "utf-8")
r = 1

x = []
y = []
for sor in forras:
    adat = sor.strip().split(' ')
    x.append(float(adat[0]))
    y.append(float(adat[1]))