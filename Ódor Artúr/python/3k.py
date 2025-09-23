"""szam = int(input("Adj meg egy számot: "))"""
szam = 2
osztokszama = 1
for i in range(2, szam//2 + 1):
    
    if szam % i == 0:
        osztokszama += 1
    elif osztokszama > 2:
        break
    
if osztokszama > 2:
    print("Nem prím")
elif szam == 1:
    print("Egyesszám")
else:
    print("Prím")