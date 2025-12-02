FROM = 'AAABBBCCCDDDEEEEFFGGG'
TO =   'BDFCEFBEGAEGBCDGABCDE'
WEIGHTS = [2, 5, 3, 7, 1, 4, 7, 3, 4, 5, 1, 1, 1, 3, 1, 3, 3, 4, 4, 1, 3]

maxw=max(WEIGHTS)

START = 'A'
TARGET = 'D'

VERTICES = "ABCDEFG"
dist = [maxw]*len(VERTICES)
prev = [None]*len(VERTICES)

dist[VERTICES.index(START)] = 0
q = list(range(7))

while len(q) > 0:
	current_vertex = q.pop(dist.index(min(dist)))


	for i, f in enumerate(FROM):
		if f == VERTICES[current_vertex]:
			idx = VERTICES.index(TO[i])
			if dist[current_vertex] + WEIGHTS[i] < dist[idx]:
				dist[idx] = dist[current_vertex] + WEIGHTS[i]
				prev[idx] = current_vertex

s = []
u = VERTICES.index(TARGET)
while prev[u] is not None:
	s.insert(0, VERTICES[u])
	u = prev[u]
s.insert(0, START)
print(" -> ".join(s))