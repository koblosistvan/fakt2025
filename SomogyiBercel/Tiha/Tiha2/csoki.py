
W = tuple(map(int, input().split()))

s2 = sum(W)/2

for i, w1 in enumerate(W[:-1]):
	if (s2-w1) in W[i+1:] or w1 == s2:
		print("IGEN")
		break
else:
	print("NEM")