#1
forras = open("Dobai Balint\\python\\1-gyongy-1-utolsó pár.txt", mode='r', encoding="utf-8")
adat=forras.readline()
adat = list(adat)
forras.close()

print(adat)
'''
#2
forras = open("Dobai Balint\\python\\1-gyongy-2.txt", mode='r', encoding="utf-8")
adat=forras.readline().strip()
adat = adat.split()
forras.close()

print(adat)

#3
forras = open("Dobai Balint\\python\\1-gyongy-3.txt", mode='r', encoding="utf-8")
adat= []
for sor in forras:
    adat.append(sor.strip())

forras.close()

print(adat)



#4
forras = open("Dobai Balint\\python\\1-gyongy-4.txt", mode='r', encoding="utf-8")
adat= []
int(forras.readline())
for sor in forras:
    adat.append(sor.strip())
forras.close()

print(adat)
'''

#1 feladat

szinek = []
for g in adat:
    if g not in szinek:
        szinek.append(g)

print(f"A nyaklancon {len(szinek)} fele gyongy van")

#2 feladat

for i in range(len(adat)):
    if adat[i-1] == adat[i]:
        print("elofordult ilyen eset")
        break
else:
    print("nem fordult elo ilyen eset")

#3 feladat



