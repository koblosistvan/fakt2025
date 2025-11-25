
data = []

lc = 1

header = None

def getline(x):
	# \n bent maradt a végén
	x2 = x[:-1].split(",")
	gdp = None if x2[7] == "None" else float(x2[7])
	# print(x, x2)
	return {
		header[0]: x2[0],
		header[1]: x2[1],
		header[2]: x2[2],
		header[3]: int(x2[3]),
		header[4]: float(x2[4]),
		header[5]: float(x2[5]),
		header[6]: int(x2[6]),
		header[7]: gdp
	}
cd = set()

with open("SomogyiBercel/py/ökolábnyom.csv", "r", encoding="utf-8") as f:
	header = f.readline().split(",")
	for l in f:
		l2 = getline(l)
		data.append(l2)
		cd.add(l2["kód"])


print("%d sor" % len(data))
print("%d ország" % len(cd))
print("%d-től %d-ig" % (min(data, key=lambda x:x["év"])["év"],max(data, key=lambda x:x["év"])["év"]))

maxcap = max(data, key=lambda x:x["kapacitás"])

print("%s a legnagyobb kapacitású ország (%.1fha)" % (maxcap["ország"],maxcap["kapacitás"]))
