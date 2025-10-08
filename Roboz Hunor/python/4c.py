forras = open('fakt2025\\_Megoldások\\python\\4c-bolt.txt', mode='r', encoding='utf-8') 

bevetel = []
kiadas= []
for sor in forras:
    adat = sor.strip().split(',') 
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))

print(bevetel)
print(kiadas)

veszteseges_napok = 0

for i in range(len(bevetel)):
    if bevetel[i] < kiadas[i]:
        veszteseges_napok +=1
print(f'{veszteseges_napok} nap volt veszteséges')

tizszazalekos_profit = 0

for i in range(len(bevetel)):        #fjdhsfu
    if bevetel[i]  >= kiadas[i]:
        tizszazalekos_profit +=1
print(f'{tizszazalekos_profit} napon volt a profit legalabb 10%kal nagyobb')


napok_szama=len(bevetel)
ossz_nyer = 0
ossz_kiad = 0

for i in range(napok_szama):
    ossz_kiad += kiadas[i]
    ossz_nyer += bevetel[i]
print(f'A teljes profit {ossz_nyer-ossz_kiad} volt')

hetvegi_bevetel = 0
hetvegi_kiadas = 0
for i in range(napok_szama):
    if napok_szama[i] == 6 or 7:
        hetvegi_bevetel += bevetel[i]
        hetvegi_kiadas -=kiadas[i]
print(f'A hetvégi össz profit {hetvegi_bevetel-hetvegi_kiadas}')
