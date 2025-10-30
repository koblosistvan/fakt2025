

"""
15 3
SSSCSSVSSSSSSSS

"""

l = input().split(" ")
N = int(l[0])
K = int(l[1])

data = input()

n = 0 # megrendezhetők
n1 = 0 # meghosszabbíthatók

c = 0 # ismétlődő S számláló

for d in data:
    if d == "S":
        c += 1
    else:
        c = 0
    
    if c == 3:
        n += 1
    if c == 4:
        n1 += 1
        c = 0

print(n, n1, sep="\n")