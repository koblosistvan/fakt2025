emberek = input('')
pacsi = 0
jobbra = 0

for i in range(len(emberek)):
    if emberek[i] == '>':
        jobbra += 1
    elif emberek[i] == '<':
        pacsi += jobbra
print(pacsi)
























































67