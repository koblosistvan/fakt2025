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
with open(r"Ódor Artúr\python\cooper\cooper.txt", mode="r", encoding="utf-8") as f:
    nev, tavaly, iden = [], [], []
    f.readline()
    for sor in f:
        adat = sor.strip().split("\t")
        nev.append(adat[0])
        tavaly.append(int(adat[1]))
        iden.append(int(adat[2]))
print("A fájl beolvasva")
# --------------------------------------------------------------------------------------------------------
# 2. feladat: hány diák vett részt a teszten
# minta: A teszten 12 diák vett részt.
print(f"A teszten {len(nev)} diák vett részt.")

# --------------------------------------------------------------------------------------------------------
# 3. feladat: hány diák futott legalább 3000 m-t idén?
# minta: Idén 3 diák futott legalább 3000 m-t.
# minta: Idén senki nem futott legalább 3000 m-t.
haromezer = 0
for a in iden:
    if a >= 3000:
        haromezer += 1
if haromezer == 0:
    print("Senki nem futott idén legalább 3000 métert.")
else: 
    print(f"Idén {haromezer} diák futott legalább 3000 m-t")
# --------------------------------------------------------------------------------------------------------
# 4. feladat: mennyi volt a legjobb futó eredménye idén és ki futotta azt?
# minta-könnyített: Az idei legjobb eredmény 3450 m volt.
# minta: Az idei legjobb eredményt Mák Áron érte el 3450 m-es távval.
for i in range(len(iden)):
    if iden[i] == max(iden):
        print(f"Az idei legjobb eredményt {nev[i]} érte el {max(iden)} m-es távával.")
# --------------------------------------------------------------------------------------------------------
# 5. feladat: mennyi volt a legnagyobb javítás és ki követte el (azaz az idei-tavalyi eredmény maximális értéke)?
# minta-könnyített: A legnagyobb javítás 231 m volt.
# minta: A legtöbbet Gáz Áron javított, ő tavaly 2345 m-t futott, idén 2645 m-t, így 3005 m-t javított az eredményén.# 
# # minta-extra: A legnagyobb javítás 234 m volt, megyet Gáz Áron, Szabó Miklós és Kiss Rozália követett el.
legn_jav = 0
for i in range(len(iden)):
    if tavaly[i] - iden[i] > legn_jav:
        legn_jav = tavaly[i] - iden[i]
jav_diak = []
for i in range(len(nev)):
    if tavaly[i] - iden[i] == legn_jav:
        jav_diak.append(nev[i])
print(f"A legnagyobb javítás {legn_jav} m volt, melyet", end=" ")
print(", ".join(jav_diak[0:len(jav_diak) -1]))

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
