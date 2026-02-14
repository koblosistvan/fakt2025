hazai = input().split()
vendeg = input().split()
h_vedett,h_gol,h_loves,v_vedett,v_gol,v_loves = int(hazai[0]),int(hazai[1]),int(hazai[2]),int(vendeg[0]),int(vendeg[1]),int(vendeg[2])

while True:
    valt = False

    if h_gol != -1 and v_vedett != -1 and h_loves == -1:
        h_loves = h_gol + v_vedett
        valt = True


    if h_loves != -1 and h_gol != -1 and v_vedett == -1:
        a = h_loves - h_gol
        if a >= 0:
            v_vedett = a
            valt = True
        else:
            v_vedett = -1


    if v_gol != -1 and h_vedett != -1 and v_loves == -1:
        v_loves = v_gol + h_vedett
        valt = True


    if v_loves != -1 and v_gol != -1 and h_vedett == -1:
        a = v_loves - v_gol
        if a >= 0:
            h_vedett = a
            valt = True
        else:
            h_vedett = -1


    if h_loves != -1 and v_vedett != -1 and h_gol == -1:
        a = h_loves - v_vedett
        if a >= 0:
            h_gol = a
            valt = True
        else:
            h_gol = -1


    if v_loves != -1 and h_vedett != -1 and v_gol == -1:
        a = v_loves - h_vedett
        if a >= 0:
            v_gol = a
            valt = True
        else:
            v_gol = -1

    if not valt:
        break


print(h_vedett,h_gol,h_loves)
print(v_vedett,v_gol,v_loves)
