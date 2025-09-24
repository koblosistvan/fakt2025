forrás = open('Szmodis Vince\\python\\4c-bolt.txt', mode='r' , encoding='utf-8')

bevetel=[]
kiadas=[]

for sor in forrás:
    adat= sor.strip().split(',')
    bevetel.append(int(adat[0]))
    kiadas.append(int(adat[1]))

napok_szama=len(bevetel)

veszt_nap=0

for i in range(napok_szama):

    if kiadas[i]>bevetel[i]:
        veszt_nap+=1

print(f'Veszteséges napok száma: {veszt_nap}')


szazalek_napok=0
for i in range(napok_szama):

    if bevetel[i]+bevetel[i]*1/10>kiadas[i]:
        szazalek_napok+=1
        
print(f'{szazalek_napok} nap vot amikor a bevétel 10%-kal több volt a kiadásnál')

ossz_bevetel=0
ossz_kiadas=0
for i in range(napok_szama):
    ossz_bevetel += bevetel[i]
    ossz_kiadas += kiadas[i]

print(f'A teljes profit {ossz_bevetel-ossz_kiadas} Ft volt')

hetvegi_bevetel=0
hetvegi_kiadas=0

for i in range

        