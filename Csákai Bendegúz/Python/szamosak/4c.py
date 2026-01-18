forras = open('_Megoldások\\python\\4c-bolt.txt', mode= 'r', encoding='utf-8')

bevetel = []
kiadas = []
for sor in forras:
    adat = sor.strip().split(',')
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))

vesztesegesnap = 0
for i in range(len(bevetel)):
    if bevetel[i] < kiadas[i]:
        vesztesegesnap += 1
print(f'{vesztesegesnap} nap volt veszteséges')

bevnagykia10 = 0
for i in range(len(bevetel)):
    if bevetel[i] >= kiadas[i]*1.1:
        bevnagykia10 += 1
print(f'{bevnagykia10} napon volt 10%-kal nagyobb profit')

osszbev = 0
osszkia = 0
for i in range(len(bevetel)):
    osszbev += bevetel[i]
    osszkia += kiadas[i]
print(f'Az összbevétel {osszbev} volt')
print(f'Az összkiadás {osszkia} volt')
print(f'A teljes profit {osszbev-osszkia}')