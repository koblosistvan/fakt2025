p = [1,2,3,4,5,6,7,8,9,10]

print(p)

print(p[8])

print(f"az utolsó érték : {p[-1]} ")

print(p[1:3])
print(p[1:])
print(p[3:])

print(p[1:6:2])
print(p[::-1])

szöveg = "még nyílnak a völgyben a kerti virégok"
print(szöveg)
print(szöveg [0:5])
print(szöveg[::-1])

if 12 in p:
    print('benne van')
else:
    print('nincs benne')