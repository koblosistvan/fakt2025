"""
5 2017
1 20 6 18
12 24 1 5
7 12 12 10
6 22 6 10
6 22 7 10

"""



import datetime

def date_d(y, m1, d1, m2, d2):
    if m1 > m2 or (m1 == m2 and d1 > d2):
        m2, m1 = m1, m2
        d2, d1 = d1, d2

    date1 = datetime.date(y,m1,d1)
    date2 = datetime.date(y,m2,d2)
    diff = date2 - date1

    year_length = 365 if (y%4 != 0) else 366

    return min(diff.days, year_length - diff.days)

l = input().split(" ")

N = int(l[0])
EV = int(l[1])

best = 366
bests = []

for i in range(N):
    in_data = [int(x) for x in input().split(" ")]
    d = date_d(EV, *in_data)

    if d < best:
        bests.clear()
        best = d
    elif d > best:
        continue
    bests.append(str(i+1))

print(len(bests))
print(" ".join(bests))
