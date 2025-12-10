
Q = int(input())

for q in range(Q):
	f, t = map(int, input().split())
	curr_sum = 0
	for i in range(f, t+1):
		ps = sum(map(int, str(i)))
		while True:
			s = sum(map(int, str(ps)))
			if ps == s:
				curr_sum += s
				break
			ps = s
	print(curr_sum)