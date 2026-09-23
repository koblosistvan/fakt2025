adatok = [865, 846, 831, 820, 808, 783, 788, 775, 752, 750, 743, 745, 758, 770]
össz_adatok_szama=len(adatok)
legkisebb=adatok[0]
legkisebb_index=0
for i in range(össz_adatok_szama):
    if adatok[i] < legkisebb:
        legkisebb=adatok[i]
        legkisebb_index=i+1   #Mert i 0-ról indul
print(f'A legkisebb mért érték: {legkisebb} \nA legkisebb mérési adat sorszáma: {legkisebb_index}')
szám=int(input('Minél kisebb értékeket keres? (egész szám)  '))
érték_alatt=0
for i in range(össz_adatok_szama):
    if adatok[i] < szám:
        érték_alatt += 1 
print(f'{szám} alatti mérések száma: {érték_alatt}')

legnagyobb_csökkenés=0
for i in range(össz_adatok_szama):
    if  adatok[i-1]-adatok[i] > legnagyobb_csökkenés:
        legnagyobb_csökkenés=adatok[i-1]-adatok[i]
print(f'A két mérés közötti legnagyobb csökkenés: {legnagyobb_csökkenés}')