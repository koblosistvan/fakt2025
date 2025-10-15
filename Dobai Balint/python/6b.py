forras = open('Dobai Balint\\python\\6b-forgalom.txt', mode = 'r', encoding='utf-8')

forras.readline()

hely= []
ora = []
perc = []
ido = []




for sor in forras:
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    ora.append(int(adat[0]))
    perc.append(int(adat[0]))
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







