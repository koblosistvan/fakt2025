
from random import randint


def prim(n):
	p = True
	for i in range(2, n//2+1):
		if n % i == 0:
			p = False
			break
	return p

data = [randint(1,6) for i in range(100)]
print(data)

even = 0
primes = 0

n1_2 = 0
ng = 0

prev = prev2 = None


for n in data:
    if n % 2 == 0: # párosak
        even += 1
    if prim(n): # prímek
        primes += 1
    if prev == 1 and n == 2: # 1 után 2
        n1_2 += 1
    if prev and prev2 and prev2 < prev and prev < n: # 3x mindig nagyobb
        ng += 1
    
    prev2 = prev
    prev = n

print("%d páros, %d páratlan." % (even, len(data)-even))
print("1 után 2 %d esetben." % (n1_2))
print("%d esetben data[n-2] < data[n-1] < data[n]" % (ng))
for i in range(1, 7):
    print("%d ennyiszer: %d" % (i, data.count(i)))
print("Átlag: %f" % (sum(data)/len(data)))