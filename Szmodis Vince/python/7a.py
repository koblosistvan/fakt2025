forras =open ('Szmodis Vince\\python\\7a-lakas-arak.txt', mode = 'r', encoding= 'utf-8')
forras.readline()

lakasok_terulete=[]
lakasok_ara=[]

for sor in forras:
    adat=sor.strip().split(' ')
    lakasok_ara.append(int(adat[1]))
    lakasok_terulete.append(int(adat[0]))
    

legdragabb_lakas=lakasok_ara[0]
legdragabb_lakas_index=1

for i in range(len(lakasok_ara)):
    if legdragabb_lakas<lakasok_ara[i]:
        legdragabb_lakas=lakasok_ara[i]
        legdragabb_lakas_index=i
print(f'{legdragabb_lakas} milió ft volt a legdrágább lakás')
print(f'aminek {legdragabb_lakas_index} volt a sorszáma')

for i in range(len(lakasok_ara)):
    if lakasok_ara[i]>500:
        print('Van 500 milliónál drágább lakás')
        break
else:
    print('Nincs 500 milliónál nagyobb lakás')

arterulet_arany_index=0
arterulet_arany=lakasok_ara[0]/lakasok_terulete[0]
for i in range(len(lakasok_ara)):
    if arterulet_arany<lakasok_ara[i]/lakasok_terulete[i]:
        arterulet_arany=lakasok_ara[i]/lakasok_terulete[i]
        arterulet_arany_index=i
print(f'A {arterulet_arany_index}. lakásnak volt a legnagyobb ár-terület  aránya')

husznal_ocsobb=0
for i in range(len(lakasok_ara)):
    if lakasok_ara[i]<20
        husznal_ocsobb+=1
print(f'{}')