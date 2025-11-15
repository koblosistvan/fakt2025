N, M = map(int, input().split())

data = {}
for i in range(M):
	to,fr = map(int, input().split())
	to -= 1
	fr -= 1
	if fr not in data:
		data[fr] = [[],[to]]
	else:
		data[fr][1].append(to)

	if to not in data:
		data[to] = [[fr],[]]
	else:
		data[to][0].append(fr)

# print(data)

ops = []

while True:
	for d in data.keys():
		if len(data[d][0]) == 0:
			ops.append("%d %d" % (d+1, 0))
			del data[d]
			break
		elif len(data[d][1]) == 0:
			ops.append("%d %d" % (d+1, 1))
			del data[d]
			break
	else:
		break

if len(ops) == 0:
	print("-1")
else:
	print(len(ops))
	print("\n".join(ops))