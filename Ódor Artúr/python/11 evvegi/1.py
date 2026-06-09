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
    if adat[i-1] == adat[i]:
        par += 1
        if par == 1:
            print("Van 2 egymás mellett.")
    
print(f"{par} db szín pár van egymás mellet.")

#3.

korlanc = adat + adat
m_szamlalo = 1
m_egymas_mellett = input("Mennyi legyen egymás mellett? ")
for i in range(len(korlanc)-1):
    if korlanc[i+1] == korlanc[i]:
        m_szamlalo += 1
        if m_egymas_mellett == m_szamlalo:
            print(f"Van {m_egymas_mellett} db szín egymás mellett.")    
    else: 
        m_szamlalo = 1 
