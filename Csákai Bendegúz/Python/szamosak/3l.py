c = a = int(input('Adj meg egy számot: '))
d = b = int(input('Adj meg egy másik számot: '))
while a != b:
    if a > b:
        a = a - b
    elif b > a:
        b = b - a
print(f'A legnagyobb közös osztó: {a}')
lkkt = int((c*d)/a)
print(f'A legkisebb közös többszörös: {lkkt} ')