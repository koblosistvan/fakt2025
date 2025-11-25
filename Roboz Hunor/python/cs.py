forras = open('_Feladatok\\python\\CS\\cs.csv', mode='r',encoding='utf-8')
forras.readline()
idő,pálya,csapat,pont,kölünbség,eredmény = [],[],[],[],[],[]

for sor in forras:
    adat = sor.strip().split(';')
    idő.append(adat[0])
    pálya.append(adat[1])
    csapat.append(adat[2])
    pont.append(int(adat[3]))
    kölünbség.append(int(adat[4]))
    eredmény.append(adat[5])
forras.close()

print(f'{int(len(csapat)/2)} meccs adatai vannak az állományban')

elso = idő[0] 
for i in range(len(idő)):
    if idő[i] > elso:
        elso = idő[i]
print(f'Az első meccs {elso}-ben volt')