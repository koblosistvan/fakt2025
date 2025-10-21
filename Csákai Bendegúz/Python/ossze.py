import random
db = 5
szám = []
megold = 0
for i in range(db):
    szám.append(random.randint(1,100))
    megold = sum(szám)
print(szám)
print(sum(szám))