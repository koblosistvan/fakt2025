forras = open('_Megoldások\python\4c-bolt.txt', mode='r', encoding='utf-8')

bevetel = []
kiadas = []
for sor in forras:
    adat = sor.strip().split(',')
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))