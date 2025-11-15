forras = open('Szmodis Vince\\python\\6b-forgalom.txt', mode='r',encoding='utf-8')
forras.readline()

hely=[]
ora=[]
perc=[]
ido=[]


for sor in forras:
    adat=sor.strip().split(' ')
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
        leghosszabb_ido_index=i
print(f'{leghosszabb_ido} perc volt a leghosszabb idő, amíg nem jött egy jármű sem')
print(f'Ennek {ido[leghosszabb_ido_index]} perckor volt a kezdő és {ido[leghosszabb_ido_index+1]} perckor volt a végpontja')

otvenes_meresipont=0
for i in range(len(hely)):
    if hely[i]==50:
        otvenes_meresipont+=1
print(f'{otvenes_meresipont} db jármű haladt át az ötvenes mérési ponton')

bekert_óra=int(input('Add meg az órát: '))
bekert_perc=int(input('Add meg a percet: '))
for i in range(len(hely)):
    if bekert_óra*60+bekert_perc==ido[i]:
        print('Haladt el jármű ebben az időpontban')
        break
    
else:
    print('Nem haladt el jármű')

legtobb_meres_hely=1
legtobb_meres=0
szamlalok= [0]*101
for i in range(len(hely)):
    szamlalok[hely[i]]+=1
    if legtobb_meres_hely:
        break

        
        
    
    
    
      