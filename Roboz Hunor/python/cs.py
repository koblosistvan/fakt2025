forras = open('fakt2025\\_Feladatok\\python\\CS\\cs.csv', mode='r',encoding='utf-8')
forras.readline()
idő,pálya,csapat,pont,különbség,eredmény = [],[],[],[],[],[]

for sor in forras:
    adat = sor.strip().split(';')
    idő.append(adat[0])
    pálya.append(adat[1])
    csapat.append(adat[2])
    pont.append(int(adat[3]))
    különbség.append(int(adat[4]))
    eredmény.append(adat[5])
forras.close()

print(f'{int(len(csapat)/2)} meccs adatai vannak az állományban')

for i in range(len(különbség)):
    for k in range(len(különbség-i-1)):
        if különbség[k] < különbség[k+1]:
            különbség[k],különbség[k+1] = különbség[k+1],különbség[k]


