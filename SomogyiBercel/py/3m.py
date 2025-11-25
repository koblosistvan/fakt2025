
w = int(input("w = "))
h = int(input("h = "))



for y in range(h):
    for x in range(w):
        print("o", end=" ")
    print()

xedge = (0,w-1)
yedge = (0,h-1)

for y in range(h):
    for x in range(w):
        if y in yedge:
            print("+" if x in xedge else "-", end="")
        else:
            print("|" if x in xedge else ":", end="")
    print()

w = int(input("háromszög w = "))

for y in range(w,-1,-1):
    for x in range(w-y):
        print(end=" ")
    for x in range(2*y+1):
        print(end="*")
    print()

for y in range(w):
    for x in range(w-y):
        print(end=" ")
    for x in range(y):
        print(end="*")
    print()

for y in range(w,-1,-1):
    for x in range(w-y):
        print(end=" ")
    for x in range(y):
        print(end="*")
    print()
