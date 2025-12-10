
import sys

N, P = map(int, input().split())

hand = [set() for i in range(4)]

for i in range(N):
	color, value = map(int, input().split())
	color -= 1
	hand[color].add(value)
	# print(hand, file=sys.stderr)
	for j in range(value-2, value+1):
		if (j in hand[color]) and (j+1 in hand[color]) and (j+2 in hand[color]):
			print(max(1, i+1-P))
			exit()
else:
	print("Lehetetlen")