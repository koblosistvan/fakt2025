import random

gondoltam = random.randint (1, 100)
tipp=-1

while tipp != gondoltam:

    tipp = int(input("Mi a tipped? "))

    if tipp == gondoltam:
        print("Gratulálok, eltaláltad!")
    
    else:
        print("Sajnos nem jó.")
