tömeg = input().split()
egy,kettő,három,négy = int(tömeg[0]),int(tömeg[1]),int(tömeg[2]),int(tömeg[3])
fel = (egy + kettő + három + négy) / 2
if fel % 1 == 0:
    if egy+kettő == fel:
        print("IGEN")
    elif egy+három == fel:
        print("IGEN")
    elif egy+négy == fel:
        print("IGEN")
    elif kettő+három == fel:
        print("IGEN")
    elif kettő + négy == fel:
        print('IGEN')
    elif három+négy == fel:
        print("IGEN")
    elif egy == fel:
        print('IGEN')
    elif kettő == fel:
        print('IGEN') 
    elif három == fel:
        print('IGEN') 
    elif négy == fel:
        print('IGEN') 
    else:print("NEM")
else:
    print("NEM")
