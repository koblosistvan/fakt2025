forras = open('_Megoldások\\python\\4c-bolt.txt', mode='r', encoding='utf-8')

bevetel= []
kiadas = []
for sor in forras:
    adat = sor.strip().split(',')
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))
print(bevetel)
print(kiadas)

napok_szama = len(bevetel)
v_nap=0

for i in range(napok_szama):

    if bevetel[i] < kiadas[i] :
        v_nap += 1  

print(f'{v_nap} ennyi veszteséges nap volt.')

big_money=0
for i in range(napok_szama):
    if bevetel[i] > kiadas[i]:
        big_money +=1

print(f'{big_money} napon volt 10%-kal nagyobb bevétel.')

ossz_bevetel = 0
ossz_kiadas = 0
for i in range(napok_szama):
    ossz_bevetel += bevetel[i]
    ossz_kiadas += kiadas[i]
print(f'A teljes profit {ossz_bevetel - ossz_kiadas}Ft volt.')

