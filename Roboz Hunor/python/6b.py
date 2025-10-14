forras = open('_Feladatok\\python\\6b-forgalom.txt', mode='r', encoding='utf-8')
felesleges = forras.readline()
hely = []
ora = []
perc = []
ido = []

for sor in forras:
    adat = sor.strip().split(' ') 
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1])*60+int(adat[2]))
forras.close()

leghosszab = ido[1]-ido[0]
leghosszab_index = 0

for i in range(len(hely)-1):
    kül = ido[i+1]-ido[i]
    if kül > leghosszab:
        leghosszab = kül
        leghosszab_index = i

print(f'{ora[leghosszab_index]:0>2d}:{perc[leghosszab_index]:0>2d} és {ora[leghosszab_index+1]:0>2d}:{perc[leghosszab_index+1]:0>2d} között volt')


egyponton=0

for i in range(len(hely)-1):
    if hely[i] == 50:
        egyponton +=1
print(f'az ötvenes ponton összesen {egyponton} autó haladt át')


idopont = input('Adj meg egy időpontot: ')
idoszak = idopont.strip().split(':')
oraban = idoszak[0] 
percben = idoszak[1] 

for i in range(len(hely)-1):
    if oraban == ora[i] and percben == perc[i]:
        print('Van autó amit ebben az időpontban mértek')
        break
else:
    print('Nincs autó amit ebben az időpontban mértek')

