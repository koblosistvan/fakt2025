# olvasd be az adatokat tartalmazó fájlok egyikét
# 	a cooper.txt minden számadatot tartalmaz, de a neveket nem, ezzel lesz egyszerűbb dolgoznod
# 	a cooper-extra.txt a neveket és egy fejlécet is tartalmaz, ezzel oldhatod meg az extra feladatokat is

# mindkét fájl a 11. évfolyam Cooper tesztjének eredményét tartalmazza, azaz hogy tavaly és idén 
# hány métert tudtak futni a diákok 12 perc alatt
# a programodat a megjegyzésként beírt szövegrészek után (közé) írd be
# figyelj a minta szövegre, annak megfelelően formázd a saját kiírásaidat is

# --------------------------------------------------------------------------------------------------------
# 1. feladat: adatok beolvasása és tárolása

forras = open('_Feladatok\\python\\Cooper\\cooper.txt',mode = 'r',encoding='utf-8')
forras.readline()

nev,tavaly,iden = [],[],[]

for sor in forras:
    adat = sor.strip().split('\t')
    nev.append(adat[0])
    tavaly.append(int(adat[1]))
    iden.append(int(adat[2]))

forras.close()



# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.


print(f'A teszten {len(nev)} diák vett részt.')

# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.
# minta: Idén senki nem futott legalább 3000 m-t.

haromezerfelett = 0

for i in range(len(nev)):
    if iden[i] >= 3000:
        haromezerfelett+=1

if haromezerfelett > 0:
    print(f'Idén {haromezerfelett} diák futott legalább 3000 m-t.')
else: print('Idén senki nem futott legalább 3000 m-t.')   


# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén és ki futotta azt?
# minta-könnyített: Az idei legjobb eredmény 3450 m volt.
# minta: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.


leg_nev = nev[0]
leg_fut = iden[0]

for i in range(len(nev)):
    if iden[i] > leg_fut:
        leg_fut = iden[i]
        leg_nev = nev[i]

print(f'Az idei legjobb eredményt {leg_nev} érte el {leg_fut} m-es távval.')



# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás és ki követte el (azaz az idei-tavalyi eredmény maximális értéke)?
# minta-könnyített: A legnagyobb javítás 231 m volt.
# minta: A legtöbbet Gáz Áron javított, ő tavaly 2345 m-t futott, idén 2645 m-t, így 3005 m-t javított az eredményén.# 
# # minta-extra: A legnagyobb javítás 234 m volt, megyet Gáz Áron, Szabó Miklós és Kiss Rozália követett el.


leg_javit = iden[0] - tavaly[0]
leg_javit_nevek = []

for i in range(len(nev)):
    if iden[i] - tavaly[i] > leg_javit:
        leg_javit = iden[i] - tavaly[i]
        
for i in range(len(nev)):
    if iden[i] - tavaly[i] == leg_javit:
        leg_javit_nevek.append(nev[i])

if len(leg_javit_nevek) > 1: 
    nevek =', '.join(leg_javit_nevek[:-1]) + ' és ' + leg_javit_nevek[-1]
else: nevek = leg_javit_nevek[0]

print(f"A legnagyobb javítás {leg_fut} m volt, melyet " + nevek + " követett el")

# --------------------------------------------------------------------------------------------------------
# 6. feladat: listázd ki az idei 3000 m felett teljesítőket
# minta-könnyített: 
# 3124
# 3187
# ...

# minta: 
# Mekk Elek    3143
# Kis Miska    3251
# Kő Pál       3423
# ...

# minta-extra (rendezett): 
# Mekk Elek    3670
# Kis Miska    3460 (-210)
# Kő Pál       3410 (-260)
# ...



for i in range(len(nev)):
    for k in range(len(nev)-i-1):
        if iden[k] < iden[k+1]:
            nev[k],nev[k+1],tavaly[k],tavaly[k+1],iden[k],iden[k+1] = nev[k+1],nev[k],tavaly[k+1],tavaly[k],iden[k+1],iden[k]
            
for i in range(len(nev)):
    kül = iden[i-1]-iden[i]
    if iden[i] > 3000:
        if i == 0:
            print(f'{nev[i]} \t {iden[i]} ')
        else: print(f'{nev[i]} \t {iden[i]} (-{kül})')