'''
Adott egy kép egy fenyőfáról, melynek minden pixelét egy karakter jelöl a forrás állományban
Méretek: 40x40 pixel, soronként balról jobbra haladva.
Jelmagyarázat: h=fekete háttér, z=zöld, b=barna, s=sárga, p=piros, k=kék, f=fehér

Feladatok:
1. olvasd be és tárold el a kép karaktereit
2. hány hópihét látsz a képen?
3. melyik sorban van a törzs teteje?
4. melyik sorban van a törzs alja, milyen magas a fa törzse?
5. hány dísz van a fán? 
6. milyen színű díszeket látsz, melyikből hányat?
'''

data = []

snow = 0
trunk_start = None

trunk_end = None

decorations = {
	's': 0,
	'p': 0,
	'k': 0
}

with open("_Megoldások/python/Fenyőfa/fenyofa.txt") as f:
	f.readline()
	for i, l in enumerate(f):
		l2 = l.rstrip()
		data.append(l2)
		snow += l2.count('f')
		if trunk_start is None and 'b' in l2:
			trunk_start = i
		
		if trunk_start is not None and trunk_end is None and 'b' not in l2:
			trunk_end = i
		
		for d in decorations.keys():
			decorations[d] += l2.count(d)

		

print("Hópihék száma: %d" % snow)
print("Törzs teteje: %d" % trunk_start)
print("Törzs alja: %d, Törzs hossza: %d" % (trunk_end, trunk_end-trunk_start))
print("Díszek: Összesen %d" % sum(decorations.values()))

for d in decorations:
	print("- %s: %d" % (d, decorations[d]))