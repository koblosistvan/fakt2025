
data = []
"""
[SzülÉv, SzülHó, SzülNap, KezdÉv, VégÉv]
"""


with open("_Feladatok/python/6a-hallgatok.txt", mode="r") as file:
    file.readline()
    for l in file:
        ld = l.strip().split(" ")

        data.append([int(x) for x in ld])

age_lim = int(input("kor: "))

bd = input("Születésnap: ").split(" ") # születésnap
bd_mo, bd_day = int(bd[0]), int(bd[1])

found1 = False
found2 = False

n2016 = 0

for s in data:

    # VégÉv - SzülÉv
    if not found1 and (s[4] - s[0]) < age_lim:
        found1 = True
    
    #                SzülHó            SzülNap
    if not found2 and s[1] == bd_mo and s[2] == bd_day:
        found2 = True
    
    if s[4] == 2016:
        n2016 += 1
    
if found1:
    print("Van fiatalabban végzett.")
else:
    print("Nincs fiatalabban végzett.")

if found2:
    print("Van tanuló, akinek %02d.%02d. a születési dátuma." % (bd_mo, bd_day))
else:
    print("Nincs hallgató a megadott szül. dátummal.")

youngest = min(data, key=lambda x:(x[4]-x[0],x[1],x[2]))

print("Legfiatalabb: %d.%02d.%02d" % (youngest[0], youngest[1], youngest[2]))

print(n2016)