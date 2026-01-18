gsz = int(input())
a = []
for i in range(gsz):
    a.append(int(input()))
h = 0
v = 0
d = 0
k = 0
mi_k = 0
ma_f = 0
for i in range(gsz):
    b=f'{h}:{v}'
    if h == v:
        d += 1
    if a[i] == 1:
        h+=1
        b=f'{h}:{v}'
    elif a[i] == 2:
        v+=1
        b=f'{h}:{v}'
    k = h-v
    ma_f = max(ma_f, k-mi_k)
    mi_k = min(mi_k, k)
if h == v:
    d+=1
print(f'{h} {v}')
print(d)
print(ma_f)
