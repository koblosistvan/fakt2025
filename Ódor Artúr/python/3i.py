import random

randomszam = random.randint(1, 100)
kitalalta = False
proba = 10

while not kitalalta and proba > 0:
    tipp = int(input("Írj egy tippet: ")) 
    
    if tipp == randomszam:
        print("Kitaláltad!!!")
        kitalalta = True
    elif tipp < randomszam:
        print("A szám nagyobb.")
        proba -= 1
    elif tipp > randomszam:
        print("A szám kisebb.")
        proba -= 1

    if proba == 5:
        print("Még 5 lehetőséged van")
    elif proba == 0:
        print("Vesztettél")
        