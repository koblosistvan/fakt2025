forras = open('fakt2025\\Csákai Bendegúz\\Python\\5b-homerseklet.txt', mode= 'r', encoding= 'utf-8')
ido = []
fok = []

for sor in forras:
    adat = sor.strip().split('\t')
    ido.append(adat[0])
    fok.append(float(adat[1]))
forras.close()
idohossz =len(ido)-1

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

legn_em = fok[1] - fok[0]
ido1 = ido[0]
ido2 = ido[1]
for i in range(1,idohossz):
    if legn_em < fok[i+1] - fok[i]:
        legn_em = fok[i+1] - fok[i]
        ido1 = ido[i]
        ido2 = ido[i+1]
print(f'A legnagyobb emelkedés {ido1} és {ido2} között volt, {legn_em:.2f} fok')

