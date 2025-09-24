import random

dobasok = []

for i in range(1, 101):
    dobasok.append(random.randint(1, 6))


hatosak = 0
for i in range(len(dobasok)):
    
    if dobasok[i] == 6:
        hatosak += 1
print(f"\n{hatosak} hatos dobás volt\n")

parosokszama = 0
for i in range(len(dobasok)):
    if dobasok[i] % 2==0:
        parosokszama += 1
print(f"{parosokszama} páros volt\n{len(dobasok) - parosokszama} páratlan volt")

primek = [2, 3, 5]
prim_szamlalo = 0
for dobas in dobasok:
    if dobas in primek:
        prim_szamlalo += 1
print(f"{prim_szamlalo} ennyi prím volt")

egy_utan_ketto = 0
for i in range(len(dobasok) - 1):
    if dobasok[i] == 1 and dobasok[i + 1 ] == 2:
        egy_utan_ketto += 1
print(f"{egy_utan_ketto} ször volt egy után kettő")


nagyobb_mint_sz = 0
for i in range(len(dobasok) - 1):
    if dobasok[i] < dobasok[i + 1]:
        nagyobb_mint_sz += 1
print(f"{nagyobb_mint_sz} szer volt nagyobb mint az előző dobás")

szamlalok = [0, 0, 0, 0, 0, 0]
for i in range(len(dobasok)):
    szamlalok[dobasok[i] - 1] += 1


print(f"Dobások: ")
for i in range(len(szamlalok)):
    print(f"\t{i + 1}:\t{szamlalok[i]}db")