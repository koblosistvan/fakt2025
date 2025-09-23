p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"\n{p}")
print(p[-1])
print(p[2:5])
print(p[2:])
print(p[:4])
print(p[2:8:3])
print(p[:: -1])

szöveg = "Még nyilnak a völgyben a kerti virágok... "
print(szöveg[0:6])
print(szöveg[:: -1])
if 11 in p:
    print("Benne van")
else:
    print("Nincs benne")