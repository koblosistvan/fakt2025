bevetelek = [3000, 2500, 4300, 3000, 5600]

elem = int(input('mi legyen a keresett elem? :'))

for i in bevetelek:
    if elem == i:
        van = True
        print('van ilyen elem a sorszama:' bevetelek.index(i+1))
        break
if van == False:
    print('nincs ilyen elem')

for i in range(len(bevetelek)):
    if bevetelek[i] == elem:
        print(f'az elem sorszamai : {i+1}')