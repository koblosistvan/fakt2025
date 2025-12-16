from dataclasses import dataclass
import sorts
import time
import enum

class Result(enum.Enum):
	LOSE = -1
	TIE = 0
	WIN = 1
	def fromstr(s):
		if s == "győzelem":
			return Result.WIN
		elif s == "döntetlen":
			return Result.TIE
		else:
			return Result.LOSE

@dataclass
class Match:
	time: str
	cs_map: str
	team: str
	points: int
	point_diff: int
	result: Result
	
	def fromline(line: str):
		ls = line.strip().split(';')
		
		return Match(ls[0], ls[1], ls[2], int(ls[3]), int(ls[4]), Result.fromstr(ls[5]))

data = []

with open("_Feladatok/python/CS/cs.csv", "r", encoding="utf-8") as f:
	f.readline()
	for l in f:
		data.append(Match.fromline(l))

# print("\n".join(map(str, data)))

print("Meccsek száma: %d" % (len(data)/2))

print("Első meccs ekkor: %s" % (min(data, key=lambda x:x.time).time))


s = time.time_ns()

sorts.quicksort(data, key=lambda x: x.point_diff)

print(time.time_ns() - s, "ns")

maps = set()

for d in data:
	maps.add(d.cs_map)

print("Ennyi pálya: %d" % len(maps))

extrasalt = tuple(filter(lambda x: x.team == "Extra Salt", data))

print("Az Extra Salt ennyi meccset játszott: %d" % len(extrasalt))

wins = 0
ties = 0
loses = 0

for m in extrasalt:
	if m.result == Result.LOSE:
		loses += 1
	elif m.result == Result.TIE:
		ties += 1
	else:
		wins += 1

print("Győzelmek: %d, Döntetlenek: %d, Vereségek: %d" % (wins, ties, loses))
print("Átlag pontkülönbség: %.2f" % (sum(m.point_diff for m in extrasalt)/len(extrasalt)))