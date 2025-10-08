forras = open('_Feladatok\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')
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

i = 0
while i < adatok_szama and befejezes_eve[i] -szuletesi_ev[i] > eletkor_hatar:
    break