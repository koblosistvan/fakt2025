import random

nyero_szamok = []
egyezo = 0

for i in range(5):
    nyero_szamok.append(random.randint(1, 90))
    te_szamod = int(input(f"Add meg a(z) {i+1}. számod: "))
    if te_szamod == nyero_szamok [i]:
        print(f"Az {i+1}. számod egyezik a nyerő számmal")
        egyezo += 1

print(f"{egyezo} számú tipped egyezik a nyerővel")
print(f"A nyerő számok: {nyero_szamok}")




















































67