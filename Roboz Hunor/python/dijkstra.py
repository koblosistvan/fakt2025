tol = 'AAABBBCCCDDDEEEEFFGGG'
ig =  'BDFCEFBEGAEGBCDGABCDE'
suly = [2, 5, 3, 7, 1, 4, 7, 3, 4, 5, 1, 1, 1, 3, 1, 3, 3, 4, 4, 1, 3]
csucs = 'ABCDEFG'
tavolsag =[max(suly) for _ in range(len(csucs))]
elozo = [None for _ in range(len(csucs))]
tavolsag[0]=0
q=[i for  i in range(len(csucs))]

while len(q) > 0:
    akt_csucs = q[0]
    for i in range(len(csucs)):
        if tavolsag[i] < akt_csucs and i in q:
            akt_csucs = i
    for  i in range(len(tol)):
        if tol[i] == csucs[akt_csucs]:
            ig_index = csucs.index(ig[i])
            if tavolsag[akt_csucs] + suly[i] < tavolsag[ig_index]:
                tavolsag[ig_index] = tavolsag[akt_csucs] + suly[i]
                elozo[ig_index] = tavolsag[akt_csucs]
    q.remove(akt_csucs)
    
for i in range( len(csucs)):
    print(f'{csucs[i]}\t{tavolsag[i]}\t{csucs[elozo[i]] if elozo[i] != None else None}')

