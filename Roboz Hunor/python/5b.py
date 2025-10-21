forras = open('_Feladatok\\python\\5b-homerseklet.txt', mode='r', encoding='utf-8')
idopont = []
homerseklet = []
for sor in forras:
    adat = sor.strip().split('\t') 
    idopont.append(adat[0])
    homerseklet.append(float(adat[1]))
    
harmicfelett = 0 
    
for i in range(len(homerseklet)):
    if homerseklet[i] > 30:
        harmicfelett += 1
        
print(f'{harmicfelett} x volt 30 fok felett a hőmérséklet')

osszhomerseklet = 0

for i in range(len(homerseklet)):
    osszhomerseklet += homerseklet[i]
    atlaghomerseklet = osszhomerseklet/len(homerseklet)
print(f'{atlaghomerseklet} fok volt átlagosan a nap folyamán')

nott = 0
csokkent = 0

for i in range(len(homerseklet)-1):
    if homerseklet[i] > homerseklet[i+1]:
        csokkent += 1 
    if homerseklet[i] < homerseklet[i+1]:
        nott += 1
        
print(f'{nott} x nőtt a hőmérséklet az azt megelőzőhőz képest ')
print(f'{csokkent} x csökkent a hőmérséklet az azt megelőzőhőz képest ')

min_hom = min(homerseklet)
max_hom = max(homerseklet)

min_index = homerseklet.index(min_hom)
max_index = homerseklet.index(max_hom)

print(f'A legalacsonyabb hőmérséklet: {min_hom} volt, ekkor: {idopont[min_index]}')
print(f'A legmagasabb hőmérséklet: {max_hom} volt, ekkor: {idopont[max_index]}')

legnagyobb_emelkedes = 0
legnagyobb_index = 0

for i in range(len(homerseklet)-1):
    kulonbseg = homerseklet[i + 1] - homerseklet[i]
    if kulonbseg > legnagyobb_emelkedes:
        legnagyobb_emelkedes = kulonbseg
        legnagyobb_index = i
print(f'A legnagyobb hőmérséklet emelkedés volt {idopont[legnagyobb_index]} és {idopont[legnagyobb_index + 1]} között: {homerseklet[legnagyobb_index+1]} - {homerseklet[legnagyobb_index]} = {kulonbseg:.2f}')


leggyanusabb = 0
leggyanusabb_index = 0

for i in range(len(homerseklet)-1):
    átlag = (homerseklet[i-1]+homerseklet[i+1])/2
    elteres = abs(átlag - homerseklet[i])
    if elteres > leggyanusabb:
        leggyanusabb = elteres
        leggyanusabb_index = i

        
print(f'A leggyanúsabb mérést {idopont[leggyanusabb_index]}-kor mértük: {homerseklet[leggyanusabb_index-1]} {homerseklet[leggyanusabb_index]} {homerseklet[leggyanusabb_index]+1}')
        
        