
x = input()

count = 0
lastc = None
subc = 0

for i, c in enumerate(x):
	if c == '<':
		subc += 1
	elif c == '>':
		if lastc is None:
			lastc = x.count('<', i)
		else:
			lastc -= subc
		subc = 0
		count += lastc

print(count)