# olvasd be az adatokat tartalmazó fájlok egyikét
# 	a cooper.txt minden számadatot tartalmaz, de a neveket nem, ezzel lesz egyszerűbb dolgoznod
# 	a cooper-extra.txt a neveket és egy fejlécet is tartalmaz, ezzel oldhatod meg az extra feladatokat is

 
# --------------------------------------------------------------------------------------------------------
# mindkét fájl a 11. évfolyam Cooper tesztjének eredményét tartalmazza, azaz hogy tavaly és idén 
# hány métert tudtak futni a diákok 12 perc alatt
# a programodat a megjegyzésként beírt szövegrészek után (közé) írd be
# figyelj a minta szövegre, annak megfelelően formázd a saját kiírásaidat is

# --------------------------------------------------------------------------------------------------------
# 1. feladat: adatok beolvasása és tárolása
forras=open('Szmodis Vince\\python\\cooper.txt',mode='r', encoding='utf-8')
forras.readline()
nev=[]
tavaly=[]
iden=[]
for sor in forras:
    adat=sor.strip().split('\t')
    nev.append(adat[0])
    tavaly.append(int(adat[1]))
    iden.append(int(adat[2]))
adatok_szama=len(nev)
# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.
print(f'A teszten {adatok_szama} diák vett részt.')

# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.
# minta: Idén senki nem futott legalább 3000 m-t.
idei_haromezret_lefutott=0
for i in range(adatok_szama):
        if iden[i]>=3000:
            idei_haromezret_lefutott+=1
            
if idei_haromezret_lefutott>=1:
    print(f'Idén {idei_haromezret_lefutott} diák futott legalább 3000 m-t.')

else:
    print(f'Idén senki nem futott legalább 3000 m-t.')
# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén és ki futotta azt?
# minta-könnyített: Az idei legjobb eredmény 3450 m volt.
# minta: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.
idei_max=iden[0]
idei_max_index=0
for i in range(adatok_szama):
     if idei_max<iden[i]:
          idei_max=iden[i]
          idei_max_index=i
print(f'Az idei legjobb eredményt {nev[idei_max_index]} érte el {idei_max} m-es távval.')

# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás és ki követte el (azaz az idei-tavalyi eredmény maximális értéke)?
# minta-könnyített: A legnagyobb javítás 231 m volt.
# minta: A legtöbbet Gáz Áron javított, ő tavaly 2345 m-t futott, idén 2645 m-t, így 3005 m-t javított az eredményén.# # minta-extra: A legnagyobb javítás 234 m volt, megyet Gáz Áron, Szabó Miklós és Kiss Rozália követett el.
max_javitas=iden[0]-tavaly[0]
max_javitas_index=0
for i in range(adatok_szama):
     if max_javitas<iden[i]-tavaly[i]:
        max_javitas=iden[0]-tavaly[0] 
        max_javitas_index=i
print(f'A legtöbbet {nev[max_javitas_index]} javított, ő tavaly {tavaly[max_javitas_index]} m-t futott, idén {iden[max_javitas_index]} m-t, így {max_javitas} m-t javított az eredményén.')

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
for i in range(adatok_szama):
     if iden[i]>3000:
          print(f'{nev[i]}\t{iden[i]}')
# minta-extra (rendezett): 
# Mekk Elek    3670
# Kis Miska    3460 (-210)
# Kő Pál       3410 (-260)
# ...
