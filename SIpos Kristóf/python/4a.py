import random
rolls = []
for i in range(100):
    rolls.append(random.randint(1,6))
print(rolls)

rolled_6=0
for i in range (len(rolls)):
    if rolls[i] == 6:
        rolled_6 +=1
print(f'a dobások között {rolled_6} hatos volt. ')
