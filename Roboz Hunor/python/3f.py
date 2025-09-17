pi = 0 
for i in range(1,1001,2):
    if i % 4 == 3:
        pi-=1/i
    else:
        pi+=1/i

print(pi*4)