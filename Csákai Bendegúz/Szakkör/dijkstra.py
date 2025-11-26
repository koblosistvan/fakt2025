tol = 'AAABBBCCCDDDEEEEFFGGG'
ig =  'BDFCEFBEGAEGBCDGABCDE'
suly = [2, 5, 3, 7, 1, 4, 7, 3, 4, 5, 1, 1, 1, 3, 1, 3, 3, 4, 4, 1, 3]

csucs = 'ABCDEFG'
csucsok_szama = len(csucs)
elek_szama = len(tol)
tavol = [320237 for _ in csucs]
elozo = [None for _ in csucs]


tavol[0] = 0
q = [i for i in range(csucsok_szama)]


while len(q) > 0:
    akt_csucs = q[0]
    for i in range(csucsok_szama):
        if tavol[i] < tavol[akt_csucs] and i in q:
            akt_csucs = i


    szomszedok = []
    for el in range(elek_szama):
        if tol[el] == csucs[akt_csucs]:
            szomszedok.append(ig[el])


            ig_index = csucs.index(ig[el]) 
            if tavol[akt_csucs] + suly[el] < tavol[ig_index]:
                tavol[ig_index] = tavol[akt_csucs] + suly[el]
                elozo[ig_index] = akt_csucs
    q.remove(akt_csucs)
for i in range(csucsok_szama):
    print(f'{csucs[i]}\t{tavol[i]}\t{csucs[elozo[i]]}' if elozo[i] != None else None)