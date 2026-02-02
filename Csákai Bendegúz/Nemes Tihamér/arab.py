szoveg = input('Mondat: ')
magan = ['a','e','i','o','u']
rovid = []
for i in range(len(szoveg)):
    if (szoveg[i] in magan) and (szoveg[i+1] not in magan) and (szoveg[i+2] not in magan):
        rovid.append(i)
print(rovid)