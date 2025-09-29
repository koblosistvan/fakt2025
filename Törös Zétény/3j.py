szám = int(input("Adj meg egy számot: "))
alap = int(input("Add meg a számrendszer alapját: "))
eredmény = ''

while szám > 0:
    maradék = szám % alap
    eredmény = str(maradék) + eredmény
    szám = (szám - maradék) // alap
print(f"Kettes számrendszerben: {eredmény}")