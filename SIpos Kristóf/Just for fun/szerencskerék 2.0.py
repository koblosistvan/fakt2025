import random
words=['macska','kutya','asztal']
used=[]
time=['1','5','10','20']
number_time=random.randint(0,len(time)-1)
number=random.randint(0,len(words)-1)
print(f'Amit kell épiteni az {[words[number]]}és van rá {time[number_time]} perced')
used.append(words[number])
while len(used) != len(words):
    if words[number] in used:
        number=random.randint(0,len(words)-1)
        number_time=random.randint(0,len(time)-1)
    else:
        phaser=input('Add meg a kellő parancsot: ')
        if phaser == 'spin' or 'next' or '':
            used.append(words[number])
            print(f'Amit kell épiteni az {words[number]} és van rá {time[number_time]} perced')

        
        




