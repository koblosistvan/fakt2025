
data = None

with open("_Feladatok/python/6b-forgalom.txt","r") as f:
    M, N = f.readline().split(" ")[:2]

    print(M,N)
    data = [[] for i in range(int(M))]

    max_d = None

    prev_time = 0

    for l in f:
        sl = l.split(" ")
        t = int(sl[1])*60 + int(sl[2])
        data[int(sl[0])-1].append(t)
        
        delta = t - prev_time
        if max_d is None:
            max_d = 0
        elif max_d < delta:
            max_d = delta


        prev_time = t
    print("Nem állomás szerint besorolva a legnagyobb távolság %d perc volt." % max_d)

max_d = 0
max_i = 0
for i, m in enumerate(data):
    prev_time = None

    for n in m:
        delta = 0 if prev_time is None else n-prev_time
        if delta > max_d:
            max_d = delta
            max_i = i
        
        prev_time = n

print("Állomás szerint besorolva a legnagyobb távolság %d perc volt a(z) %d. állomáson." % (max_d, max_i+1))
print("Az 50-es mérési ponton %d mérés történt." % len(data[49]))

time = input("Idő (ÓÓ:PP): ").split(":")
mins = int(time[0])*60 + int(time[1])

found = False
for m in data:
    if mins in m:
        print("Van mérési adat ekkorról")
        found = True
        break
    if found: break
else:
    print("Nincs mérési adat ekkorról")

lengths = list(map(len, data))
for i,l in enumerate(lengths):
    print("%3d. állomás: %2d mérés" % (i+1, l))

print("A %d. állomáson volt a legtöbb mérés." % (lengths.index(max(lengths))+1))

