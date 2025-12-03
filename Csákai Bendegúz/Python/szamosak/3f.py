pi = 0
for i in range(1,1001,2):
    if i%4 == 3:
        pi = pi - 1 / i
    else:
        pi = pi + 1 / i
print(pi*4)