forras = open("_Feladatok\\python\\4d-pontok.txt", mode="r", encoding="utf-8")

x = []
y = []
sugar = 1

for sor in forras:
    adat = sor.strip().split(" ")
    x.append(float(adat[0]))
    y.append(float(adat[1]))

szamlalo = 0
for i in range(len(x)):
    if x[i]**2 + y[i]**2 <= sugar**2:
        szamlalo += 1
        
print(szamlalo)