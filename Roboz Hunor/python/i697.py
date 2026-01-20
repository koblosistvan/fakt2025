a = input().split()
növények,maxviz = a[0], a[1]
 
locsolt = []

for i in range(növények):
    a = int(input())
    locsolt.append(a)

átlag = round(sum(locsolt)/len(locsolt))

for i in range(locsolt):
    if átlag == locsolt[i]:
        sorsz = locsolt[i+1]



