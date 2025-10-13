

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

for s in data:
    # VégÉv - SzülÉv
    if (s[4] - s[0]) < age_lim:
        print("van")
        break
else:
    print("nincs")