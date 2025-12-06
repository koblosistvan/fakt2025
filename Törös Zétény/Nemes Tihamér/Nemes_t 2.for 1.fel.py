csokik = [int(input())]
if csokik[0] + csokik[1] == csokik[2] + csokik[3] or csokik[0] + csokik[2] == csokik[1] + csokik[3] or csokik[0] + csokik[3] == csokik[2] + csokik[1]:
    print("IGEN")
else:
    print("NEM")