a = float(input("Add meg az a-t: "))
b = float(input("Add meg a b-t: "))
c = float(input("Add meg a c-t: "))

d = b**2 -4*a*c

print(d)

if d < 0:
    print("nincs megoldás")
elif d == 0:
    print(f"x= {(-b + d**0.5) / 2*a}")
else:
    print(f"x1= {(-b + d**0.5) / 2*a}\nx2= {(b - d**0.5) / 2*a}")