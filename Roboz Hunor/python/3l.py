

a = int(input("Add meg egy  számot: "))
b = int(input("Add meg még egy számot: "))


while b != 0:
    maradek = a % b
    a = b
    b = maradek

lnko = a
lkkt = a * b // lnko

print(lnko)
print(lkkt)
