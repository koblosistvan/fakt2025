
forras=open('Sipos Kristóf\\python\\6a-hallgatok.txt', mode='r', encoding='utf-8')

szul_ev=[]
szul_ho=[]
szul_nap=[]
kezdes_eve=[]
vegzes_eve=[]




adatok_szama=int(forras.readline())
for sor in forras:
    adat = sor.strip().split(' ')
    szul_ev.append(int(adat[0]))
    szul_ho.append(int(adat[1]))
    szul_nap.append(int(adat[2]))
    kezdes_eve.append(int(adat[3]))
    vegzes_eve.append(int(adat[4]))

eletkor=int(input('Add meg az életkorod: '))

for i in range(adatok_szama):
    kor=vegzes_eve[i] - szul_ev[i]
    if kor < eletkor:
        print(f'Van {eletkor} évnél fiatalabb végzett.')
        break
else:
    print(f'Nincs {eletkor} évnél fiatalabb végzet.')

i=0
while i< adatok_szama and vegzes_eve[i]-szul_ev[i] >= eletkor:
    i+=1
if i < adatok_szama:
    print(f'Van {eletkor} évnél fiatalabb végzet.')
else:
    print(f'nincs {eletkor} évnél fiatalabb végzet.')