# prim

n = int(input("n = "))

p = True
for i in range(2, n//2+1):
	if n % i == 0:
		p = False
		break

print("Prím" if p else "Nem prím")