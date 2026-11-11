'''
Eljárás PozitívakSzáma(T[1...n])
    C := 0;
    Ciklus i = 1-től n-ig
        Ha T[i] pozitív, akkor
        C := C+1
    Ciklus vége
    KI:C


PozitívakSzáma([1,2,3,-1,-2,-3])
'''
def pozitivakszama(t):
    c = 0
    for i in range(len(t)):
        if t[i] >= 0:
            c = c+1
    return c

print(pozitivakszama([1,2,3,-1,-2,-3]))