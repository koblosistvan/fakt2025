
def lnko(a,b):
	if a == 0 or b == 0:
		raise ValueError("nem lehet 0")
	if a > b:
		a,b = b,a
	
	while b != 0:
		a,b = b,a%b
	
	return a

a = int(input("a = "))
b = int(input("b = "))

o = lnko(a,b)

print("lnko(%d, %d) = %d" % (a,b, o))
print("lkkt(%d, %d) = %d" % (a,b, abs(a*b)//o))