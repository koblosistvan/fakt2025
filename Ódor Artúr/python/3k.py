"""szam = int(input("Adj meg egy számot: "))"""
szam = 100
osztokszama = 0
for i in range(1, szam + 1):
    
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