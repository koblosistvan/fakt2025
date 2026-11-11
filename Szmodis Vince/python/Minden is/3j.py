szám=int(input('Adj meg egy számot: '))
rendszer=int(input('Hányas számrendszerbe váltsam át? '))
eredmény= ' '

while szám>0:
 

    eredmény=str(szám%rendszer)+eredmény
 
    if szám%rendszer==0:
        szám//=rendszer

    else: szám = (szám-1)//rendszer

print(f'A választott számrendszerben: {eredmény}')