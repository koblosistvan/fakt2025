x = 0
megoldva = False
gyokok = 0

while not megoldva:
    if x **3 - 78 * x **2 + 1787 * x - 11070 == 0: 
        gyokok += 1
        print(x)
    if gyokok == 3:
        megoldva = True
    x += 1

megoldva = False
gyokok = 0
x = 0
print()

while not megoldva:
    if x **3 - 58 * x **2 + 427 * x + 11070 == 0:
        gyokok += 1
        print(x)
    if abs(x) **3 - 58 * abs(x) **2 + 427 * abs(x) + 11070 == 0:
        gyokok +=1
        print(abs(x))
    if gyokok == 3:
        megoldva = True 
    x -= 1
