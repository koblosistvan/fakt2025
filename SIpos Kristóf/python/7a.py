forras=open('Sipos Kristóf\\python\\7a-lakas-arak.txt', mode='r', encoding='utf-8')
adatok_szama = int(forras.readline())

terulet=[]
erteke=[]

for sor in forras:
    adat= sor.split()
    terulet.append(int(adat[0]))
    erteke.append(int(adat[1]))

legdragabb=erteke[0]
legdragabb_index=1

for i in range(adatok_szama):
    if  legdragabb < erteke[i]:
        legdragabb=erteke[i]
        legdragabb_index= i
print(f'A legdrágább ház {legdragabb} Millió Ft volt és a {legdragabb_index+2}. ház volt az. ')

for i in range(adatok_szama):
    if erteke[i] > 500:
        print('Van 500 milliónál drágáb ház. ')
else:
    print('Nincs 500 milliónál drágáb ház. ')
    
