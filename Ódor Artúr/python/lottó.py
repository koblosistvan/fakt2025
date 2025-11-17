import random

ny_szamok = []
tippek = []

while len(ny_szamok) != 5:
    ny = random.randint(1, 90)
    if ny not in ny_szamok:
        ny_szamok.append(ny)
while len(tippek) != 5:
    tipp = int(input("Tippelt szám:"))
    if tipp in tippek:
        print("Ezt már tippelted")
    elif tipp > 90 or tipp < 0:
        print("1-től 90-ig tippelj!")
    else:    
        tippek.append(tipp)

print("\nNyerőszámok: ", end="")
for i in range(4):
    print(ny_szamok[i], end=", ")
print(ny_szamok[-1])
print("\nTippeid: ", end="")
for i in range(4):
    print(tippek[i], end=", ")
print(tippek[-1])

talalatok = []
for i in range(5):
    if tippek[i] in ny_szamok:
        talalatok.append(tippek[i])

print(f"\n{len(talalatok)} találatod volt.")
if len(talalatok) > 0:
    print("A következők: ", end="")
    for i in range(len(talalatok) - 1):
        print(talalatok[i], end=", ")
    print(talalatok[-1])