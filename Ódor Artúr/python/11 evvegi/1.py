"""with open(r"Ódor Artúr\python\11 evvegi\11 év végi gyakorlás\1-gyongy-1.txt","r") as f:
    adat1 = f.readline()
    adat1 = list(adat1)
print(adat1)

with open(r"Ódor Artúr\python\11 evvegi\11 év végi gyakorlás\1-gyongy-2.txt", "r") as f:
    adat2 = f.readline().split()
    adat2 = list(adat2)
print(adat2)

with open(r"Ódor Artúr\python\11 evvegi\11 év végi gyakorlás\1-gyongy-3.txt", "r") as f:
    adat3 = []
    for sor in f:
        adat3.append(sor.strip())
print(adat3)"""



adat = None
forras = r"Ódor Artúr\python\11 evvegi\11 év végi gyakorlás\1-gyongy-4.txt"
with open(forras, "r") as f:
    adat = f.read().replace(" ", "").replace("\n", "").lstrip("0123456789")
print(adat)



# 1.
szinek = []
for g in adat:
    if g not in szinek:
        szinek.append(g)
print(f"\n{len(szinek)} db szín van a nyakláncon")

#2.
par = 0
for i in range(len(adat)):
    if adat[i] == adat[i+1] if i+1 != len(adat) else adat[i] == adat[0]:
        par += 1
print()
print(f"{par} db szín pár van egymás mellet.")