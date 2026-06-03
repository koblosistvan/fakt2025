#1. fájl----------------------------------------------------------
forrás = open("Törös Zétény\\python\\11 év végi gyakorlás\\1-gyongy-1.txt", mode="r", encoding="utf-8")
adat = forrás.readline()
adat = list(adat)
forrás.close()
print(adat)

#2
forrás = open("Törös Zétény\\python\\11 év végi gyakorlás\\1-gyongy-2.txt", mode="r", encoding="utf-8")
adat = forrás.readline().strip()
adat = adat.split()
forrás.close()
print(adat)

#3
forrás = open("Törös Zétény\\python\\11 év végi gyakorlás\\1-gyongy-3.txt", mode="r", encoding="utf-8")
adat=[]
for sor in forrás:
    adat.append(sor.strip())
forrás.close()
print(adat)

#4
forrás = open("Törös Zétény\\python\\11 év végi gyakorlás\\1-gyongy-4.txt", mode="r", encoding="utf-8")
adat = []
int(forrás.readline())
for sor in forrás:
    adat.append(sor.strip())
forrás.close()
print(adat)

#1 feladat

színek=[]
for g in adat:
    if g not in színek:
        színek.append(g)

print(f"A nyakláncon {len(színek)} féle gyöngy van")

#2 feladat
for i in range(len(adat)):
    if adat[i-1] == adat[i]:
        print("Előfodul ilyen eset.")
        break
else:
    print("Nem fordul elő ilyen eset")

#3 feladat
a = int(input("Hány gyöngy egymás után:"))

for i in range(len(adat)):
    if :
        print(f"Van olyan hogy {a} ugyan olyan gyöngy van egymás után.")
        break
else:
    print(f"Nincs olyan hogy {a} ugyan olyan gyöngy van egymás után.")