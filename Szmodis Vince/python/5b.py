forras = open('Szmodis Vince\\python\\5b-homerseklet.txt',mode='r' , encoding='utf-8')

idopont=[]
homerseklet=[]


for sor in forras:
    adat=sor.strip().split('\t')
    idopont.append(float(adat[0]))
    homerseklet.append(float(adat[1]))

adatok_szama=len(homerseklet)


harminc_felett=0
for i in range(adatok_szama):
    if homerseklet[i] > 30:
        harminc_felett+=1

print(f'{harminc_felett} mérésnél volt harminc fok felett a hőmérséklet')

for i in range(adatok_szama):
    osszes_ho=homerseklet[i]+homerseklet[i+1]
    atlag_ho=osszes_ho/adatok_szama

    print(f'{atlag_ho} az átlag hőmérséklet')

nott=0
csokkent=0

for i in range(adatok_szama):
    if homerseklet[i]>homerseklet[i+1]:
        csokkent+=1
    elif homerseklet[i]<homerseklet[i+1]:
        nott+=1
    
    print(f'{nott} alkalommal nőtt és {csokkent} alkalommal csökkent a hőmérséklet')

legnagyobb=homerseklet[0]
for i in range(adatok_szama):
    if homerseklet[i]<homerseklet[i+1]:
        legnagyobb=homerseklet[i+1]
    idopont[legnagyobb.index]
    print(f'{legnagyobb} a legnagyobb hőmérséklet {idopont[legnagyobb.index]}-kor')

legkisebb=homerseklet[0]
for i in range(adatok_szama):
    if homerseklet[i]>homerseklet[i+1]:
        legkisebb=homerseklet[i+1]
    
    print(f'{legkisebb} a legnagyobb hőmérséklet {idopont[legkisebb.index]}-kor')

legnagyobb_emelkedes=[]
for i in range(adatok_szama):
    legnagyobb_emelkedes=abs(homerseklet[i]-homerseklet[i+1])
    print(f'A legnagyobb emelkedés {idopont[legnagyobb_emelkedes.index]}')

gyanus=[]
for i in range(1, adatok_szama):
    if homerseklet[i-1]+homerseklet[i+1]/2>homerseklet[i]:
        gyanus=homerseklet[i]
    print(f'A leggyanúsabb adat: {gyanus}')
        
