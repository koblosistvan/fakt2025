forras = open('fakt2025\\_Megoldások\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')
adatok_szama = int(forras.readline())

szuletesi_ev = []
szuletesi_honap = []
szuletesi_nap = []
kezdes_eve = []
befejezes_eve = []

for sor in forras:
    adat = sor.strip().split(' ') 
    szuletesi_ev.append(int(adat[0]))
    szuletesi_honap.append(int(adat[1]))
    szuletesi_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    befejezes_eve.append(int(adat[4]))

eletkor_hatar = int(input('Hány éves vagy? '))

for i in range(len(szuletesi_honap)):
    kor = befejezes_eve[i] - szuletesi_ev[i]
    if kor < eletkor_hatar:
        print('Van aki fiatalabban szerzett diplomát')
        break
else:
    print('Nincs ember aki fiatalabbként végzett volna')

szuletes_honap = int(input('Melyik hónapban  van a szülinapod? '))
szuletesnap =int(input('Melyik napon van a szülinapod? '))
for i in range(adatok_szama):
    if szuletes_honap == szuletesi_honap[i]:
        if szuletesnap == szuletesi_nap[i]:
            print('Van olyan hallgató aki akkor születtett mint te')
            break
else:
    print('Nincs olyan hallgató aki akkor születtett mint te')

legfiatalabb_végző = befejezes_eve[0] - szuletesi_ev[0]
legfiatalabb_index = 0


for i in range(adatok_szama):
    if befejezes_eve[i] - szuletesi_ev[i] < legfiatalabb_végző:
        legfiatalabb_végző = befejezes_eve[i] - szuletesi_ev[i]
        legfiatalabb_index = i
    elif befejezes_eve[i] - szuletesi_ev[i] == legfiatalabb_végző:
        if szuletesi_honap[i] < szuletesi_honap[legfiatalabb_index]:
            legfiatalabb_végző = befejezes_eve[i] - szuletesi_ev[i]
            legfiatalabb_index = i
        elif szuletesi_honap[i] == szuletesi_honap[legfiatalabb_index]:
            if szuletesi_nap[i] < szuletesi_nap[legfiatalabb_index]:
                legfiatalabb_végző = befejezes_eve[i] - szuletesi_ev[i]
                legfiatalabb_index = i
print(f'A legfiatalabb végző hallgató {legfiatalabb_végző} éves volt és {szuletesi_ev[legfiatalabb_index]} {szuletesi_honap[legfiatalabb_index]}. hónap {szuletesi_nap[legfiatalabb_index]}. napján született')



db_halgato_2016 = 0
for i in range(adatok_szama):
    if befejezes_eve[i] == 2016:
        db_halgato_2016 +=1
print(f'{db_halgato_2016} hallgató volt aki 2016-ban végzett')

eletkor_ossz = 0
db_tanuló = 0
for i in range(adatok_szama):
    if befejezes_eve[i] >= 2014 and kezdes_eve[i] <=2014:
        eletkor_ossz += 2014-szuletesi_ev[i]
        db_tanuló += 1
eletkor_atlag = eletkor_ossz / db_tanuló
print(f'{eletkor_atlag} volt az átlagéletkor 2014 tavaszán')