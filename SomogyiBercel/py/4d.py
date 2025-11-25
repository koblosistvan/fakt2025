
c = 0 # bentiek száma
R = 1

lines = None

with open("_Feladatok/python/4d-pontok.txt") as points:
	lines = points.readlines()

for line in lines:
	l = line.split(" ")

	if len(l) < 2:
		continue
	
	x, y = float(l[0]), float(l[1])
	r = (x*x+y*y)**0.5
	# print(r)
	if r < R:
		c += 1

print("%d van a körben" % (c))