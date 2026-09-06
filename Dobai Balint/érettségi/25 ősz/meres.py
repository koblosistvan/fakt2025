meres_db =16
meres_eredmenyek = [36, 48, 39, -1, 30, 43, -1, 76, 67, 82, 73, 75, 64, 73, 69, 63]

meres_sum =0
for i in range(meres_db):
    if meres_eredmenyek[i]>0:
        meres_sum += meres_eredmenyek[i]

print(meres_sum)

legnagyobb = meres_eredmenyek[0]

for i in range(meres_db):
    if meres_eredmenyek[i] > legnagyobb:
        legnagyobb = meres_eredmenyek[i]

print(f'Az athaladok maximalis szama : {meres_eredmenyek[i]}, a rogzites idopontja 8:30')
