def Előállít(A,B,S):
    SA=[]
    SB=[]
    i=0
    j=0
    for k in range(len(S)):
        if A >= S[k]:
            SA.append(0)
            SA[i] = S[k]
            i += 1
            A -= S[k]
        else:
            if B >= S[k]:
                SB.append(0)
                SB[j] = S[k]
                j += 1
                B -= S[k]
    if A>0 or B>0:
        print('Error')
    else:
        print(SA,SB) 

Előállít(14,14,[7,6,5,4,3,2,1])
