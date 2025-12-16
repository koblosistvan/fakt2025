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
forras=open('Sipos Kristóf\\python\\Cooper\\cooper.txt', mode='r', encoding='utf-8')
forras.readline()
nev=[]
tavaly=[]
iden=[]
for sor in forras:
    adat = sor.strip().split('\t')
    nev.append(adat[0])
    tavaly.append(int(adat[1]))
    iden.append(int(adat[2]))
forras.close


# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.

reszt_vett_diakok=len(iden)

print(f'{reszt_vett_diakok} diák vett részt a teszten')


# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.
# minta: Idén senki nem futott legalább 3000 m-t.
legalabb_futott_3000_metert=0
for i in range(reszt_vett_diakok):
    if iden[i] >= 3000:
        legalabb_futott_3000_metert+=1
print(f'Idén {legalabb_futott_3000_metert} diák futott legalább 3000 métert.')
# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén és ki futotta azt?
# minta-könnyített: Az idei legjobb eredmény 3450 m volt.
# minta: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.
legnagyobb_tavolsag=0
legnagyobbat_futo_ember=str(0)
for i in range(reszt_vett_diakok-1):
    if iden[i] > legnagyobb_tavolsag:
        legnagyobb_tavolsag=iden[i]
        legnagyobbat_futo_ember=nev[i]
print(f'A legnagyobb távolság {legnagyobb_tavolsag} méter volt és {legnagyobbat_futo_ember} futotta azt.')


# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás és ki követte el (azaz az idei-tavalyi eredmény maximális értéke)?
# minta-könnyített: A legnagyobb javítás 231 m volt.
# minta: A legtöbbet Gáz Áron javított, ő tavaly 2345 m-t futott, idén 2645 m-t, így 3005 m-t javított az eredményén.# # minta-extra: A legnagyobb javítás 234 m volt, megyet Gáz Áron, Szabó Miklós és Kiss Rozália követett el.


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
