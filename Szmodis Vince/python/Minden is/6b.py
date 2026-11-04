forras = open('Szmodis Vince\\python\\6b-forgalom.txt', mode='r', encoding='utf-8')
forras.readline()

hely=[]
ora=[]
perc=[]
ido=[]

for sor in (forras):
    adat = sor.strip().split(' ')
    hely.append(int(adat[0]))
    ora.append(int(adat[1]))
    perc.append(int(adat[2]))
    ido.append(int(adat[1])*60 + int(adat[2]))
forras.close()

leghosszabb_ido=ido[1]-ido[0]
leghosszabb_ido_index=0
for i in range(len(hely)-1):
    if leghosszabb_ido<ido[i+1]-ido[i]:
        leghosszabb_ido=ido[i+1]-ido[i]
        leghosszabb_ido_index = i
print(f'{leghosszabb_ido} perc volt a leghoszabb idő, amíg nem jött jármű')

