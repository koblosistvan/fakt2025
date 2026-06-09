import sys

data = None

DEFAULT_FILE = r"_Feladatok\python\11 év végi gyakorlás\1-gyongy-1.txt"

with open(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE, "r") as f:
    data = f.read().replace(" ", "").replace("\n", "").lstrip("0123456789")


data_set = set(data)

print(data)
print(len(data_set))

M = 4


i = 0

repeats = []

while i < len(data):
    j = 1

    while j != len(data) - 1 and data[i] == data[(j+i) % len(data)]:
        j += 1
    
    repeats.append((data[i], j))

    i += j

if repeats[0][0] == repeats[-1][0]:
    repeats = repeats[1:]

print(repeats)
print("Max. ismétlődő:", max(repeats, key=lambda x: x[1]))
print("%d ismétlődő:" % M, *filter(lambda x: x[1] == M, repeats))