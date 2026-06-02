# 1. fájl –---------------------------------------------------
forrás = open('_Megoldások\\python\\11 év végi gyakorlás\\1-gyongy-1.txt', mode='r', encoding='utf-8')
adat = forrás.readline().strip()
adat = list(adat)
forrás.close()
print(adat)

# 2. fájl –---------------------------------------------------
forrás = open('_Megoldások\\python\\11 év végi gyakorlás\\1-gyongy-2.txt', mode='r', encoding='utf-8')
adat = forrás.readline().strip()
adat = adat.split()
forrás.close()
print(adat)

# 3. fájl –---------------------------------------------------
forrás = open('_Megoldások\\python\\11 év végi gyakorlás\\1-gyongy-3.txt', mode='r', encoding='utf-8')
adat = []
for sor in forrás:
    adat.append(sor.strip())
forrás.close()
print(adat)

# 4. fájl –---------------------------------------------------
forrás = open('_Megoldások\\python\\11 év végi gyakorlás\\1-gyongy-4.txt', mode='r', encoding='utf-8')
adat = []
int(forrás.readline())
for sor in forrás:
    adat.append(sor.strip())
forrás.close()
print(adat)

# hány féle gyöngy van a nyakláncon
szinek = []
for g in adat:
    if g not in szinek:
        szinek.append(g)
print(f"A nyakláncon {len(szinek)} féle gyöngy van.")

# előfordul-e, hogy 2 egyforma színű gyöngy van egymás után
#	figyelj rá, hogy a lánc körbe ér
for i in range(len(adat)):
    if adat[i-1] == adat[i]:
        print(f"Van két egyforma egymás mellett.")
        break
else:
    print(f"Nincs két egyforma egymás mellett.")
