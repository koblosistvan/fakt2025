adatok = [865, 846, 831, 820, 808, 783, 788, 775, 752, 750, 743, 745, 758, 770]
legk = adatok[0]
legk_sor = 0
for i in range(len(adatok)):
    if adatok[i] < legk:
        legk = adatok[i]
        legk_sor = i+1
print(f'A legkisebb mért érték: {legk}')
print(f'A legkisebb mérési adat sorszáma: {legk_sor}')
kerdes = int(input('Minél kisebb értéket keres? (egész szám): '))
szamlalo = 0
for i in range(len(adatok)):
    if adatok[i] < kerdes:
        szamlalo += 1
print(f'{kerdes} alatti mérések száma: {szamlalo}')
csokkenes = adatok[0]-adatok[1]
for i in range(len(adatok)-1):
    if adatok[i]-adatok[i+1] > csokkenes:
        csokkenes = adatok[i]-adatok[i+1]
print(f'A két mérés közötti legnagyobb csökkenés: {csokkenes}')