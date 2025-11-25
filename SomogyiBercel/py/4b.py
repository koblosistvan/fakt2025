from random import randint

JELES = 96
MAX = 120
N = 100 # Dogák száma

points = [randint(0,MAX) for i in range(N)]
# print(points)

jel = 0 # jelesek
mj = 0 # majdnem jeles

counts = [0]*11

for p in points:
	if p > (JELES-3) and p < JELES:
		mj += 1
	elif p >= JELES:
		jel += 1
	counts[p//(MAX//10)] += 1

print("%d jeles dolgozat." % (jel))
print("%d embernek 3-nál kevesebb hiányzott a jeleshez." % (mj))

for i, n in enumerate(counts):
	b = i*10
	if b != 100:
		print("%d-%d%%-os: %d darab" % (b, b+9, n))
	else:
		print("100%%-os: %d darab" % (n))

print("Átlag pontszám: %d" % (sum(points)/len(points)))