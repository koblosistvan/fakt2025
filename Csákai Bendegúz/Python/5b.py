forras = open('_Feladatok\\python\\5b-homerseklet.txt', mode= 'r', encoding= 'utf-8')
ido = []
fok = []

for sor in forras:
    adat = sor.strip().split('\t')
    ido.append(adat[0])
    fok.append(float(adat[1]))
forras.close()
idohossz =len(ido)

harmincfolottinapokszama = 0
for i in range (1, idohossz):
    if fok[i] > 30:
        harmincfolottinapokszama += 1
print(f'A 30 fok fölötti napok száma: {harmincfolottinapokszama}')

átlag = 0
for i in range(1, idohossz):
    átlag = (sum(fok))/idohossz
print(f'Az átlaghőmérséklet {átlag:.2f} volt')

nott = 0
csokk = 0
for i in range(idohossz):
    if fok[i] > fok[i-1]:
        nott += 1
    elif fok[i] < fok[i-1]:
        csokk += 1
print(f'{nott} esetben nőtt a hőmérséklet a napok között')
print(f'{csokk} esetben csökkent a hőmérséklet a napok között') 

legn = max(fok)
legk = min(fok)
legn_index = ido[(fok.index(max(fok)))]
legk_index = ido[(fok.index(min(fok)))]
print(f'A legmagasabb hőmérséklet {legn_index}-kor volt, {legn} hőmérséklet')
print(f'A legalacsonyabb hőmérséklet {legk_index}-kor volt, {legk} hőmérséklet')

