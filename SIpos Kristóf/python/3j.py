számrendszer= int(input("Milyen szám rendszerben akarod a számodat: "))
szám= int(input("Adj meg egy számot: "))
eredmény= ""
while szám > 0:
    maradék=szám%számrendszer
    eredmény = str(maradék) + eredmény
    if szám % számrendszer == 0:
        szám //=számrendszer
    else:
        szám = (szám-maradék) // számrendszer
print(f"A számod {számrendszer} szám rendszerében: {eredmény}")