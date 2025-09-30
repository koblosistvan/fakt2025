
data = []

with open("SomogyiBercel/4c-bolt.txt") as f:
    lines = f.readlines()
    for line in lines:
        l = line.strip().split(",")
        data.append((int(l[0]), int(l[1])))

ld = 0 # veszteséges napok
in110 = 0 # ahol a bevétel legalább 110%-a a kiadásnak
inc = 0 # ahol nő a profit az előzőhöz képest

weekend = 0

profit = 0
pprofit = 0

for (i, (income, out)) in enumerate(data):
    eprofit = profit
    dprofit = (income-out)
    profit += dprofit
    if (i % 7) in (5,6): # hétvége
        weekend += dprofit
    if income < out:
        ld += 1
    if income >= out*1.1:
        in110 += 1
    if pprofit < profit:
        inc += 1

print("Veszteséges napok: %d" % (ld))
print("Ahol a bevétel legalább 110%%-a a kiadásnak: %d" % (in110))
print("Előző naphoz képest növekedés ennyiszer: %d" % (inc))
print("Teljes profit: %d Ft" % (profit))
print("Hétvégi profit: %d Ft" % (weekend))
