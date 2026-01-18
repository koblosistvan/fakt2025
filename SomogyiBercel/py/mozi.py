
def feladat(n):
	print("\n%d. feladat" % n)


data = []

with open("_Feladatok/python/Mozi/mozi.txt", "r", encoding="utf-8") as f:
	rows, chairs = map(int, f.readline().split())
	prices = []

	for i in range(rows):
		prices.append(map(lambda x: int(x)*500, f.readline().rstrip()))
	for i in range(rows):
		data.append([(price, x == 'x') for price, x in zip(prices[i], f.readline())])

res_count = 0
max_income = 0
curr_income = 0

minr_n = None
minr_i = None

single_chairs = []

n = int(input("Hány fő: "))

places_for_n = []

for i, row in enumerate(data):
	f_row = tuple(filter(lambda x: x[1], row))

	rc = sum(1 for p,f in f_row)

	res_count += rc
	max_income += sum(p for p,f in row)
	curr_income += sum(p for p,f in f_row)

	if i == 0 or rc < minr_n:
		minr_i = i
		minr_n = rc
	
	for j in range(chairs):
		if not row[j][1] and (j == 0 or row[j-1][1]) and (j == chairs-1 or row[j+1][1]):
			single_chairs.append((i,j))
	
	for j, a in enumerate(zip(*[row[k:] for k in range(n)])):
		if not any(map(lambda x: x[1], a)):
			places_for_n.append((i, j))

feladat(1)
print("Foglalások száma: %d" % res_count)

feladat(2)
print("Teltház esetén a bevétel %s Ft." % format(max_income, ","))

feladat(3)
print("Mostani bevétel: %s Ft" % format(curr_income, ","))

feladat(4)
print("Legkevesebb foglalt helyes sor: %d" % (minr_i+1))

print("Szabad szingli helyek: %s" % str(single_chairs))

feladat(5)
print("%d embernek ezeken a helyeken van elegendő szék: " % n)
for r, c in places_for_n:
	print("- %d. sor, %d-%d. szék" % (r+1, c+1, c+n))