
magassag = int(input("Magasság: "))
szelesseg = int(input("Szélessége: "))

for y in range(magassag):
    for x in range(szelesseg):
        if (x + y) % 2 == 0:
            print("o", end= "")
        else:
            print(" ", end= "")
    
    print()

for y in range(magassag):
    for x in range(y + 1):
        print("o", end="")
    print()


for y in range(magassag):
    for x in range(magassag- y):
        print(" ", end="")
    for x in range(y):
        print("o", end="")
    print()

for y in range(magassag):
    for x in range(y):
        print(" ", end="")
    for x in range(magassag - y):
        print("o", end="")
    print()

