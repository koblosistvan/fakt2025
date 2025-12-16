számla = [245,-60,150.8,2350,-125.5,-98,-311,100,-28,-185,555.6,600,-45.3,-100,-36.9,50,-895,-225,120,215.5]
apro = 0
for i in számla:
    if float(i) != int(i):
        apro += 1
print(f'Aprópénz: {apro}.')

szazalekba = 0
for i in számla:
    if i > 500:
        szazalekba += 1
print(f'Az 500 nál nagyobb az {int(szazalekba/len(számla)*100)}%-a.')

szazfolott = 0
for i in számla:
    if i > 100:
        szazfolott += 1
if  szazfolott != 0:
    print(f'{szazfolott}x volt 100 fölötti jóváírás.')
else:
    print('Nem volt 100 fölötti jóváírás.')

hossz = len(számla)
jovairasegymu = 0
for i in range(hossz-1):
    if számla[i] > 0 and számla[i+1] > 0:
        jovairasegymu += 1
print(f'{jovairasegymu}x történt ilyen.')