lista = [865,846,831,820,808,783,788,775,752,750,743,745,758,770]

#2
min = lista[0]
min_index = 0
for i in range (len(lista)):
    if lista[i] < min:
        min = lista[i]
        min_index +=1

print(f'A legkisebb meres {min} volt. Ez volt a {min_index}. meres')

#3

keres = int(input('minel kisebb erteket keres?'))

keres_alatt = 0

for i in range(len(lista)):
    if lista[i] < keres:
        keres_alatt +=1

print(f'A kert ertek alatt {keres_alatt} db meres volt')

#4

max_csokk = lista[0] - lista[0]

for i in range(len(lista)-1):
    if lista[i] - lista[i-1] < max_csokk:
        max_csokk = lista[i] - lista[i-1]

vegso = abs(max_csokk)
print(f'A legnagyobb visszaeses erteke {vegso}')


