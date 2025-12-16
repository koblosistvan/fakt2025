bemenet = [
    '>-<-<<-<',
    '>->>-->-<<-<<<',
    '<><-<->-<',
][2]

pacsi = 0
for i in range(len(bemenet)):
    if bemenet[i] == '>':
        pacsi += bemenet[i+1:].count('<')

print(pacsi)