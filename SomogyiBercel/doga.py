from random import randint

rolls = [randint(1,6) for i in range(randint(100,120))]

print(rolls)

s = sum(rolls)
l = len(rolls)

print("Dobások: %d db" % len(rolls))
print("Összegük: %d" % s)
print("Átlaguk: %.1f" % (s/l))

n = int(input("Szám: "))

primes = (2,3,5)

pr = 0

alln = []

for i, r in enumerate(rolls):
	if r in primes:
		pr += 1
	
	if r == n:
		alln.append(str(i))

print("%d darabszáma a tömbben: %d" % (n, len(alln)))

print("%d összes indexe: %s" % (n, ", ".join(alln) if len(alln) > 0 else "[Nincs]"))

print("Ennyi prím van: %d (%.1f%%-a a tömbnek)" % (pr, 100*(pr/l)))

print("Legkisebb dobott: %d" % min(rolls))
print("Legnagyobb dobott: %d" % max(rolls))