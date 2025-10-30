# prim

def prim(n):
	p = True
	for i in range(2, n//2+1):
		if n % i == 0:
			p = False
			break
	return p

n = int(input("n = "))

print("Prím" if prim(n) else "Nem prím")