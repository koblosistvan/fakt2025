pi = 0
x = 1
for i in range(2, 1000):
    pi += -1**i/x
    x += 2
    print(pi)
