w, h = [int(i) for i in input().split()]
n = int(input())
x0, y0 = [int(i) for i in input().split()]
while True:
    cél = ""
    bomb_dir = input()
    if bomb_dir == 'U':
        cél += str(x0) +' ' + str(int(h/2-y0)-1)
    elif bomb_dir == 'UR':
        cél += str(int(w/2+x0)-1) +' ' + str(int(h/2-y0)-1)
    elif bomb_dir == 'UL':
        cél += str(int(w/2-x0)-1) +' ' + str(int(h/2-y0)-1)
    elif bomb_dir == 'R':
        cél += str(int(w/2+x0)-1) +' ' + str(y0)
    elif bomb_dir == 'L':
        cél += str(int(w/2-x0)-1) +' ' + str(y0)
    elif bomb_dir == 'D':
        cél += str(x0) +' ' + str(int(h/2+y0)-1)
    elif bomb_dir == 'DR':
        cél += str(int(w/2+x0)-1) +' ' + str(int(h/2+y0)-1)
    elif bomb_dir == 'DL':
        cél += str(int(w/2-x0)-1) +' ' + str(int(h/2+y0)-1)
    if cél == bomb_dir:
        break
    print(cél)