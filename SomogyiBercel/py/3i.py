from random import randint

rand = randint(1,100)
tippek = 7

while rand != (t:=int(input("Találd ki: "))):
    tippek -= 1
    if tippek == 0:
        print("Vesztettél")
        break
    print("Nagyobb!" if t < rand else "Kisebb!")
    print("Még %d tipp." % tippek)

if tippek > 0:
    print("Nyertél")