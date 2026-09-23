adatok = [865, 846, 831, 820, 808, 783, 788, 775, 752, 750, 743, 745, 758, 770]

print(f"A legkisebb mért érték: {min(adatok)}\nA legkisebb adat sorszáma: {adatok.index(min(adatok))+1}")

keresett_szam = int(input("Minél kisebb értékeket keres? (egész szám)"))
szamlalo = 0
for a in adatok:
    if a < keresett_szam:
        szamlalo += 1 
print(f"{keresett_szam} alatti mérések száma: {szamlalo}")
csokkenes = 0
for i in range(len(adatok)-1):
    if adatok[i] - adatok[i+1] > csokkenes:
        csokkenes = adatok[i] - adatok[i+1]
print(f"A két mérés közötti legnagyobb csökkenés: {csokkenes}")