
S = input()

Q = int(input())

INDEX = lambda x: int(x) - 1


windows = tuple(tuple(map(INDEX, input().split())) for i in range(Q))

P = tuple(map(INDEX, input().split()))


good = True
for l, r in windows:
	sset = set()
	for j in range(l, r+1):
		if S[j] in sset:
			good = False
			break
		sset.add(S[j])
	if not good:
		break
if good:
	print(0)
	exit(0)

pset = set()

for i, p in enumerate(P):
	pset.add(p)
	good = True
	for l, r in windows:
		sset = set()
		for j in range(l, r+1):
			if j not in pset:
				
				if S[j] in sset:
					good = False
					break
				sset.add(S[j])
		if not good:
			break
	if good:
		print(i+1)
		break