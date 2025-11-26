import sys

data = []

header = None

def getline(x: str):
	# \n bent maradt a végén
	x2 = x.rstrip().split(",")
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
	header = f.readline().rstrip().split(",")
	for l in f:
		l2 = getline(l)
		data.append(l2)
		if l2["év"] == 2014:
			cd.add(l2["kód"])

YEARKEY = lambda x:x["év"]
GDPKEY = lambda x:x["gdp"]
CAPACITYKEY = lambda x:x["kapacitás"]
USAGEKEY = lambda x:x["felhasználás"]

print("Az adatforrás %d sort tartalmaz." % len(data))
print("2014-ről %d sort tartalmaz." % len(cd))
print("Az adatok %d-%d közötti évekere vonatkoznak." % (min(data, key=YEARKEY)["év"],max(data, key=YEARKEY)["év"]))

maxcap = max(data, key=CAPACITYKEY)

print("A legnagyobb kapacitású ország %s, melynek kapacitása %.0f hektár." % (maxcap["ország"],maxcap["kapacitás"]))

mingdp = min(filter(GDPKEY,data),key=GDPKEY)

print("Legkisebb GDP: %s (%.0f USD/fő)" % (mingdp["ország"],mingdp["gdp"]))

data1980 = tuple(filter(lambda x:x["év"]==1980,data))
data2014 = tuple(filter(lambda x:x["év"]==2014,data))

capsum1980 = sum(map(CAPACITYKEY,data1980))
capsum2014 = sum(map(CAPACITYKEY,data2014))

print("Összesített kapacitás 1980-ban: %.0f, 2014-ben: %.0f" % (capsum1980,capsum2014))

usagesum1980 = sum(map(USAGEKEY,data1980))
usagesum2014 = sum(map(USAGEKEY,data2014))

print("Összesített felhasználás 1980-ban: %.0f, 2014-ben: %.0f" % (usagesum1980,usagesum2014))

