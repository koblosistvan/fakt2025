a, b = 1, 1
print(a)
print(b) 

while a + b < 1000:
    a, b = b, a+b
    print(b)