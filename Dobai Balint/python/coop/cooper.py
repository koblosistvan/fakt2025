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
forras = open('Dobai Balint\\python\\coop\\cooper.txt', mode ='r', encoding='utf-8')
forras.readline()
nev , tavaly , iden = [] ,[] ,[]
for sor in forras:
    adat = sor.strip().split('\t')
    nev.append(str(adat[0]))
    tavaly.append(int(adat[1]))
    iden.append(int(adat[2]))
forras.close()

def f(n):
    print(f'\n {n}. feladat:')
# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.
f(2)
print(f'A teszten {len(nev)} diak vett reszt')

# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.
# minta: Idén senki nem futott legalább 3000 m-t.
f(3)
haromezer_felett = 0

for i in range(len(nev)):
    if iden[i] > 3000:
        haromezer_felett +=1
print(f'{haromezer_felett} diak futott 3000m-nel tobbet iden')




# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén és ki futotta azt?
# minta-könnyített: Az idei legjobb eredmény 3450 m volt.
# minta: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.
f(4)
legjobb_futo_tav = iden[0]
legjobb_futo_nev = nev[0]
for i in range(len(nev)):
    if iden[i] > legjobb_futo_tav:
        legjobb_futo_tav = iden[i]
        legjobb_futo_nev = nev[i]

print(f'A leghosszabb futas {legjobb_futo_tav} volt, amit {legjobb_futo_nev}')



# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás és ki követte el (azaz az idei-tavalyi eredmény maximális értéke)?
# minta-könnyített: A legnagyobb javítás 231 m volt.
# minta: A legtöbbet Gáz Áron javított, ő tavaly 2345 m-t futott, idén 2645 m-t, így 3005 m-t javított az eredményén.# # minta-extra: A legnagyobb javítás 234 m volt, megyet Gáz Áron, Szabó Miklós és Kiss Rozália követett el.
f(5)


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
