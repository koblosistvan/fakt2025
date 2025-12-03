tol = 'AAABBBCCCDDDEEEEFFGGG'
ig  = 'BDFCEFBEGAEGBCDGABCDE'
elek_szama = len(tol)
suly = [2, 5, 3, 7, 1, 4, 7, 3, 4, 5, 1, 1, 1, 3, 1, 3, 3, 4, 4, 1, 3]

csucs = 'ABCDEFG'
csucsok_szama = len(csucs)
tavolsag = [320237 for _ in csucs]
elozo = [None for _ in csucs]

tavolsag[0] = 0
q = [i for i in range(csucsok_szama)]

while len(q) > 0:
    akt_csucs = q[0]
    for i in range(csucsok_szama):
        if tavolsag[i] < tavolsag[akt_csucs] and i in q:
            akt_csucs = i

    for él in range(elek_szama):
        if tol[él] == csucs[akt_csucs]:
            ig_index = csucs.index(ig[él])
            if tavolsag[akt_csucs] + suly[él] < tavolsag[ig_index]:
                tavolsag[ig_index] = tavolsag[akt_csucs] + suly[él]
                elozo[ig_index] = akt_csucs
    
    q.remove(akt_csucs)

for i in range(csucsok_szama):
    print(f'{csucs[i]}\t{tavolsag[i]}\t{csucs[elozo[i]] if elozo[i] != None else None}')

