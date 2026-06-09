import re
import sys
from dataclasses import dataclass


@dataclass
class Player:
	last_entered: int
	on: bool
	time_played: int


DEFAULT_FILE = r"_Feladatok\python\11 év végi gyakorlás\2-csapat-3.txt"

data = None
data_len = None
file_version_2 = None

with open(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_FILE) as f:
	data_s = f.read().strip()
	file_version_2 = "," in data_s

	data_split = re.split(r"[^0-9]+", data_s)
	data_len = len(data_split)
	
	data = map(int, data_split)

# print(data)

subst_n = None

if file_version_2:
	subst_n = (data_len - 7) // 3
else:
	next(data)
	subst_n = next(data)

starters = [next(data) for i in range(7)]

substitutions = [tuple(next(data) for i in range(3)) for j in range(subst_n)]


GAME_TIME = 60

players = {n: Player(last_entered=0, on=True, time_played=0) for n in starters}

for time, left, entered in substitutions:
	pl = players[left]
	pl.time_played += time - pl.last_entered
	pl.on = False

	if entered in players:
		players[entered].last_entered = entered
		players[entered].on = True
	else:
		players[entered] = Player(last_entered=time, on=True, time_played=0)

for p in players.values():
	if p.on:
		p.time_played += GAME_TIME - p.last_entered

print("Pályán voltak:", ", ".join(map(str, players.keys())))

played_full = map(lambda x: x[0], filter(lambda x: x[1].time_played==GAME_TIME, players.items()))


print("Végig játszottak:", ", ".join(map(str, played_full)))

for n, p in players.items():
	print("%d: %d" % (n, p.time_played))

played_at_end = map(lambda x: x[0], filter(lambda x: x[1].on, players.items()))

print("Pályán voltak a meccs végén:", ", ".join(map(str, played_at_end)))