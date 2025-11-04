
g = {
    "A": "ABDF",
    "B": "ACDEG",
    "C": "BEH",
    "D": "AB",
    "E": "BC",
    "F": "AG",
    "G": "BFHI",
    "H": "CGJ",
    "I": "G",
    "J": "H"
}

for a in g:
    g[a] = "".join(sorted(g[a]))

first_gray = input("A-J: ").upper()

if first_gray not in g.keys():
    print("nope")
    exit(-1)

gray_order = [first_gray]

blacks = set()

while len(gray_order):
    for p in g[gray_order[0]]:
        if p not in gray_order and p not in blacks:
            gray_order.append(p)
            print(end=p)
            break
    else:
        blacks.add(gray_order.pop(0))

print()