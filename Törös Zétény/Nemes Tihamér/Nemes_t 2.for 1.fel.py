csokik = list(map(int,input().split()))
if csokik[0] + csokik[1] == csokik[2] + csokik[3] or csokik[0] + csokik[2] == csokik[1] + csokik[3] or csokik[0] + csokik[3] == csokik[1] + csokik[2] or csokik[0] + csokik[1] + csokik[2] == csokik[3] or csokik[0] + csokik[1] + csokik[3] == csokik[2] or csokik[0] + csokik[2] + csokik[2] == csokik[1] or csokik[3] + csokik[1] + csokik[2] == csokik[0]:
    print("IGEN")
else:
    print("NEM")