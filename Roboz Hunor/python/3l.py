a = int(input("Add meg egy  számot: "))
b = int(input("Add meg még egy számot: "))

a2 = a
b2 = b

while b2 != 0:
    maradek = a2 % b2
    a2 = b2
    b2 = maradek

lnko = a2
lkkt = a * b // lnko

print(lnko)
print(lkkt)