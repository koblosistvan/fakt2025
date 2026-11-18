bevetelek = [3000, 2500, 4300, 3000, 5600]
print(f'az elemek összege {sum(bevetelek)}')
s=0
db = 0
for i in bevetelek:
    s+=i
for i in bevetelek:
    if i < 3000:
        s+=i
        db+=1
print(f'az osszeg : {s/db}')

