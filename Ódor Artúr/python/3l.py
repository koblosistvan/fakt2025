a = int(input("Adj meg egy számot: "))
b = int(input("Adj meg még egy számot: "))
szam1, szam2 = a, b

while szam2 != 0:
    szam1, szam2 = szam2, szam1 % szam2
    
print(f"A legnagybb közös osztó {szam1}\nA legnagyobb közös többszörös {abs(a*b) // szam1}")