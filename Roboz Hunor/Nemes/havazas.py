e,m = [],[]
a,b = input().strip().split(),input().strip().split()

for i in range(10):
    e.append(int(a[i]))
    m.append(int(b[i]))

esz,msz = e[0],m[0]

for i in range(len(m)-1):
    if e[i] < e[i+1]:
        esz += e[i+1]-e[i]
    if m[i] < m[i+1]:
        msz += m[i+1]-m[i]

if esz > msz:
    print(2)
else:print(1)