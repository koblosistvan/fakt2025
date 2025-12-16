
N, M = map(int, input().split())
possible = ['#'+'.'*(2*i-1)+'#'*(i>0) for i in range(min(N,M)//2+1)]

data = [input() for i in range(N)]

count = 0
for y in range(len(data)-2):
	for x in range(1,len(data[y])-1):
		if data[y][x] == '#':
			l = 1
			found = False
			while (dst:=y+l) < len(data):
				l += 1
				if data[dst][x] == '#':
					found = True
					break
			if found and l % 2 != 0:
				sl = list(range(0,l//2+1))
				sl += sl[:-1][::-1]
				for i,s in enumerate(sl):
					yi = y+i
					if yi >= len(data) or x-s < 0:
						break
					if not data[yi].startswith(possible[s], x-s):
						break
				else:
					count += 1

print(count)