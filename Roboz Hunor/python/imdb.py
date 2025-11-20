forras = open('fakt2025\\_Feladatok\\python\\IMDB\\imdb.txt', mode='r',encoding='utf-8')
forras.readline()
év,idő,értékelés,rendező,bevétel,cím = [],[],[],[],[],[]
for sor in forras:
    adat = sor.strip().split('\t')
    év.append(int(adat[0]))
    idő.append(int(adat[1]))
    értékelés.append(float(adat[2]))
    rendező.append(adat[3])
    bevétel.append(int(adat[4]))
    cím.append(adat[5])
forras.close()
sor=len(cím)

print(f'{sor} film adatai vannak az állományban')

elso = év[0]

for  i in range(sor):
    if év[i] < elso:
        elso = év[i]
print(f'Az első film {elso}-ban jelent meg')

hosszabb = 0
 
for i in range(sor):
     if idő[i] > 120:
         hosszabb+=1
if hosszabb>0:
    print(f'{hosszabb} db film hosszabb 2 óránál')
else:print('Nincs két óránál hosszabb film.')

kilenc = 'nincs '

for i in range(sor):
    if értékelés[i] > 9:
        kilenc = 'Van'
        break

print(f'{kilenc} olyan film ami 9-nél nagyobb értékelést kapott')

legmagasabb_érékelés,legjobb_film = értékelés[0],cím[0]

for i in range(sor):
    if értékelés[i] > legmagasabb_érékelés:
        legmagasabb_érékelés,legjobb_film = értékelés[i],cím[i]
print(f'A legmagasabb értékelés {legmagasabb_érékelés}, ezt a {legjobb_film} című film kapta')

s = ''
szamlalo = 0
for i in range(sor-1,-1,-1):
    if értékelés[i] == értékelés[i-1]:
        szamlalo+=1
    else:
        s+=f'{értékelés[i]} - {szamlalo+1} db\n'
        szamlalo = 0
print(s)

leg_ért = értékelés[0]
leg_ren = ''
for i in range(sor):
    if értékelés[i] > leg_ért:
        leg_ért = értékelés[i]
for i in range(sor):
    if értékelés[i] == leg_ért:
      leg_ren  += f'{rendező[i]} '
print(f'A legjobb film/filmek rendezői: {leg_ren}')

kert_rend = input('Melyik rendező filmjeit keressük?  ')

rend_film = ''

for i in range(sor):
    if kert_rend == rendező[i]:
        rend_film+=f'{cím[i]}\n\t'
        meg=open(f'fakt2025\\Roboz Hunor\\python\\{kert_rend}',mode='w',encoding='utf-8')
print(f'A rendező filmjei:\n\t{rend_film}',file=meg)
