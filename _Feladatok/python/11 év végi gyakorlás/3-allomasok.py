forras = open('_Megoldások\\python\\11 év végi gyakorlás\\3-allomasok-3.txt', mode='r', encoding='utf-8')

ora = []
perc = []
sor = forras.readline()
while sor:
    ora.append(int(sor.strip()))
    sor = forras.readline()
    perc.append(int(sor.strip()))
    sor = forras.readline()

print(ora)
print(perc)
