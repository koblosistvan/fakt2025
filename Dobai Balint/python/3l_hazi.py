x = int(input('add meg az elso szamot'))
y = int(input('add meg az masodik szamot'))

a, b = x, y 
while b!= 0:
    a, b = b, a % b
lnko = a

lkkt = abs(x*y) // lnko

print(f' a ket szam legnagyobb kozos osztoja {lnko}')
print(f' a ket szam legkisebb kozos tobbszorose {lkkt}')