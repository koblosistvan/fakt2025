DATA = [865, 846, 831, 820, 808, 783, 788, 775, 752, 750, 743, 745, 758, 770]

minimum = min(DATA)
print(f"A legkisebb mért érték: {minimum}\nA legkisebb mérési adat sorszáma: {DATA.index(minimum)}")

searched_lt = int(input("Minél kisebb értékeket keres? (egész szám) "))

lt_count = 0
for _ in filter(lambda x: x < searched_lt, DATA):
	lt_count += 1

print("%d alatti mérések száma: %d" % (searched_lt, lt_count))

diffs = map(lambda x: x[0]-x[1], zip(DATA, DATA[1:]))
print("A két mérés közötti legnagyobb csökkenés: %d" % max(diffs))