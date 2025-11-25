from dataclasses import dataclass
import os

OUTPATH = os.path.dirname(os.path.abspath(__file__))

# az ökolábnyomoshoz is dataclasst kellett volna használnom...
@dataclass
class Movie:
	year: int
	length: int
	rating: float
	director: str
	income: int
	title: str
	
	def fromline(line: str):
		l = line.strip().split('\t')
		return Movie(int(l[0]), int(l[1]), float(l[2]), l[3], int(l[4]), l[5])

movies = []

with open("_Feladatok/python/IMDB/imdb.txt", "r", encoding="utf-8") as f:
	f.readline()
	for l in f:
		movies.append(Movie.fromline(l))

YEARKEY = lambda x: x.year
RATINGKEY = lambda x: x.rating
INCOMEKEY = lambda x: x.income

print("Filmek száma: %d" % len(movies))
print("Legelső film: %s" % (str(min(movies, key=YEARKEY))))

n2h = len(tuple(filter(lambda x: x.length > 120, movies)))
if n2h > 0:
	print("%d 2 óránál hosszabb film van." % n2h)
else:
	print("Nincs két óránál hosszabb film.")

rating9 = any(map(lambda x: x.rating > 9, movies))
print("Van" if rating9 else "Nincs", "9-nél jobb értékelésű film.")

bests = tuple(filter(lambda x: x.rating == max(movies, key=RATINGKEY).rating, movies))

print("Legmagasabb értékelés: %.1f" % (bests[0].rating))

ratings = {}
income_per_year = {}
directors = {}

for m in movies:
	if m.director in directors:
		directors[m.director].append(m)
	else:
		directors[m.director] = [m]
	
	if m.year in income_per_year:
		income_per_year[m.year] += m.income
	else:
		income_per_year[m.year] = m.income
	
	if m.rating in ratings:
		ratings[m.rating] += 1
	else:
		ratings[m.rating] = 1

for r in sorted(ratings):
	print("%.1f: %d film." % (r, ratings[r]))

best_directors = set(map(lambda x: x.director, bests))

print("Legjobb filmrendező(k): %s" % (", ".join(best_directors)))

director = input("Rendező neve: ").lower()
fname = director.split()[-1] + ".txt"

with open("%s/%s" % (OUTPATH, fname), "w", encoding="utf-8") as outf:
	for m in filter(lambda x: x.director.lower() == director, movies):
		outf.write("%s (%d) - %d perc\n" % (m.title, m.year, m.length))

for y in sorted(income_per_year):
	print("%d: összesen %d $" % (y, income_per_year[y]))

print("Átlagos bevétel: %.1f $" % (sum(income_per_year.values())/len(movies)))

print("A 10 legnagyobb bevételű film:")
for m in sorted(movies, key=INCOMEKEY, reverse=True)[:10]:
	print("%s, %d $" % (m.title, m.income))

for d in sorted(directors, key=lambda x: len(directors[x]), reverse=True)[:5]:
	print("%s (átlagos értékelés: %.1f)" %
		(d, sum(map(lambda x: x.rating, directors[d]))/len(directors[d])))
	for m in sorted(directors[d], key=RATINGKEY, reverse=True):
		print("\t%s: %.1f" % (m.title, m.rating))