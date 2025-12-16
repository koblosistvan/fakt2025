
W = None
H = None

data = []


with open("SomogyiBercel/py/szakkor/labirintus.txt") as f:
	H, W = map(int, f.readline().rstrip().split())
	for l in f:
		data.append(l.rstrip())


neighbors = (
	(-1, 0),
	(0, -1),
	(1, 0),
	(0, 1)
)

graph = {}

def new_edge(x1, y1, x2, y2):
	if (x1, y1) not in graph:
		graph[(x1,y1)] = []
	graph[(x1,y1)].append((x2, y2))

for y in range(1, H-1):
	for x in range(1, W-1):
		if data[y][x] == '#':
			continue

		for rx, ry in neighbors:
			nx = x+rx
			ny = y+ry
			if data[ny][nx] == '.':
				new_edge(x, y, nx, ny)

print(graph)