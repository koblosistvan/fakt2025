
N = int(input())

G = [int(input()) for i in range(N)]

gG = 0
gE = 0

ties = 1

pg = None

si = 0
sd = 0
longest_streak = 0

for i, g in enumerate(G):
	cd = gG-gE
	if pg != g:
		if (sd > 0 and cd < 0) or (sd < 0 and cd > 0):
			longest_streak = max(longest_streak, i-si)
		sd = cd
		si = i
	pg = g

	if g == 1:
		gG += 1
	else:
		gE += 1
	
	if gE == gG:
		ties += 1
	


cd = gG-gE
if (sd > 0 and cd < 0) or (sd < 0 and cd > 0):
	longest_streak = max(longest_streak, N-si)

print(gG, gE)
print(ties)
print(longest_streak)