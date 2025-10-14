
data = None

with open("_Feladatok/python/6b-forgalom.txt","r") as f:
    M, N = f.readline().split(" ")[:2]

    print(M,N)
    data = [[]] * int(M)

    max_d = None

    prev_t = 0

    for l in f:
        sl = l.split(" ")
        t = int(sl[1])*60 + int(sl[2])
        
        delta = t - prev_t
        if max_d is None:
            max_d = 0
        elif max_d < delta:
            max_d = delta

        data[int(sl[0])-1].append(t)

        prev_t = t
    print("Nem állomás szerint besorolva a legnagyobb távolság %d perc volt." % max_d)
