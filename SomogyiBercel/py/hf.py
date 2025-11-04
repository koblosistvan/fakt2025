from random import randint, choice

arr = [randint(1,5) for i in range(randint(15,20))]

l = len(arr)
s = sum(arr)

print("Létszám: %d" % l)
print("Jegyek összege: %d" % s)
print("Jegyek átlaga: %.1f" % (s/l))

for n in arr:
    if n == 1:
        print("Van 1-es")
        break
else:
    print("Nincs 1-es")

n = int(input("Jegy: "))
alln = [str(i) for i,x in enumerate(arr) if x == n]

if len(alln) > 0:
    print("%d összes előfordulása: %s (%d darab)" % (n, ", ".join(alln), len(alln)))
else:
    print("Nincs %d osztályzat" % n)


c45 = arr.count(4)+arr.count(5)
print("%d darab 3-asnál jobb jegy van (A jegyek %.1f%%-a)" % (c45, 100*(c45/l)))

print("Min. osztályzat: %d, max. osztályzat: %d" % (min(arr), max(arr)))

print(arr)