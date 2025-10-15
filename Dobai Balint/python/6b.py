forras = open('Dobai Balint\\python\\6b-forgalom.txt', mode = 'r', encoding='utf-8')

forras.readline()

hely= []
ora = []
perc = []
ido = []



for sor in forras:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1])*60 + int(adat[2]))
forras.close()

meresek = len(hely)


leghosszabb = ido[1] - ido[0]
leghosszabb_index = 0 

for i in range(meresek -1):
    if leghosszabb < ido[i+1] - ido[i]:
        leghosszabb = ido[i+1] - ido[i]
        leghosszabb_index = i

kezdete = f'{ora[leghosszabb_index]:0>2d} : {perc[leghosszabb_index] :0>2d}'
vege = f'{ora[leghosszabb_index+1]:0>2d} : {perc[leghosszabb_index+1]:0>2d}'

print(f'a leghosszabb itervallum kezdete: {kezdete}, a vege pedig {vege}')

otvenhez = 0
for i in range(meresek):
    if hely[i] == 50:
        otvenhez +=1

print(f'az 50-es meresi ponthoz {otvenhez} ertek tartozik')


bekert_ora = int(input('hany orakor? : '))
bekert_perc = int(input('hany perckor? : '))
for i in range(meresek):
    if bekert_ora == ora[i] and bekert_perc == perc[i]:
        print('a megadott idopontban volt meres')
        break
else: 
    print('nincs a megadott idopontban meres')

ket_meres_index = 0

for i in range(meresek):
    if ido[i] == ido[i-1]:
        ket_meres_index +=1

print(f'{ket_meres_index} alkalommal volt olyan amikor 2 meres tortent')



szamlalok = [0] * 101
for i in range(meresek):
    szamlalok[hely[i]] += 1
print(szamlalok)



legtobb_meres = szamlalok[0]
legtobb_meres_index = 0



for i in range(len(szamlalok)):
    if szamlalok[i-1] < szamlalok[i]:
        szamlalok[i] = legtobb_meres
        legtobb_meres_index += 1
print(f'a legtobb meres {legtobb_meres}, melyet {legtobb_meres_index}-nel mertek')


        







