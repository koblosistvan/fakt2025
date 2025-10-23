
a = int(input("Add meg az intervallum kezdetét: "))
b = int(input("Add meg az intervallum végét: "))

prim_lista = []

for szam in range(a, b + 1):
    if szam > 1:
        prim = True
        for oszto in range(2, int(szam ** 0.5) + 1):
            if szam % oszto == 0:
                prim = False
                break
        if prim:
            prim_lista.append(szam)

print(f"{a}-{b} között:", end=" ")
print(*prim_lista, sep=", ", end=" ")
print(f"– {len(prim_lista)} prímszám!")