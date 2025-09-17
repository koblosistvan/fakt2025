import random
szám=random.randint(1,100)
tipp= -1
probálkozások= 10

while tipp !=szám or probálkozások == 0:
    tipp=int(input("Mi lehet a szám: "))
    if tipp == szám:
        print("Szép munka")
    elif tipp > szám:
        print("Ú ennél azért kisebb")
        probálkozások -1
    elif tipp < szám:
        print("Ennél azért nagyobb a szám")
        probálkozások -1
    elif probálkozások == 0:
        print("vége a játéknak") 
    elif probálkozások <= 5:
        print(f"{tipp} próbálkozásod van még.")