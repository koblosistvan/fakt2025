import random
a = set()
b = set()
while len(b) !=5:
    c=int(input('Adj meg egy számot'))
    if c <= 90:
        b.add(c)
    else: 
        print('1-90 ig tippelj')
while len(a)!=5:
    f= random.randint(1,90)
    a.add(f)
d = a-b
print(f'{5-len(d)} számot találtál el')