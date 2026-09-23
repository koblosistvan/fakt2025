forras = open(r'fakt2025\Roboz Hunor\erettsegi\2026_tavasz\nyomas.txt')

for sor in forras:
    adatok = sor.split(', ')

meresek = []

for i in range(len(adatok)):
    meresek.append(int(adatok[i]))
    
min_hely = 0
min_ertek = meresek[0]

for i in range(len(meresek)):
    if min_ertek > meresek[i]:
        min_hely = i 
        min_ertek = meresek[i]

print(f'A legkisebb mért érték: {min_ertek}')
print(f'A legkisebb mérési adat sorszáma: {min_hely}')

a = int(input('Minél kisebb értékeket keres? (egész szám) '))
b = 0
for i in range(len(meresek)):
    if a > meresek[i]:
        b += 1
print(f'{a} alatti mérések száma: {b}')

leg_cs = 0

for i in range(len(meresek)-1):
    if meresek[i] > meresek[i+1]:
        kul = meresek[i] - meresek[i+1]
        if kul > leg_cs:
            leg_cs = kul

print(f'A két mérés közötti legnagyobb csökkenés: {leg_cs}')