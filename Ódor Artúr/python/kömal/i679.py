novenyek_sz, terfogat = map(int, input().strip().split(" "))
viz_be = input("")
viz, vizmas = [], []
for sor in range(novenyek_sz):
    adat = viz_be.strip().split(" ")
    viz.append(int(adat[sor]))
    vizmas.append(int(adat[sor]))
print()
atlag= round(sum(viz)/novenyek_sz)
szamlalo = 0
elso_i = 0
for i in range(novenyek_sz):
    if viz[i] == atlag:
        szamlalo += 1
        if szamlalo == 1:
            elso_i = i + 1
print(atlag, elso_i, szamlalo)

modusz = {}
for e in viz:
    if e in modusz:
        modusz[e] += 1
    else:
        modusz[e] = 1
modusz_db=0
valos_modusz = viz[0]
for e in viz:
    if modusz[e] > modusz_db:
        modusz_db = modusz[e]
        valos_modusz = e
modusz_i = -1
modusz_sz = 0
for i in range(novenyek_sz):
    if valos_modusz == viz[i] and modusz_i==-1:
        modusz_i = i+1
    if valos_modusz == viz[i]:
        modusz_sz += 1
print(valos_modusz, modusz_i, modusz_sz)


for i in range(novenyek_sz):
    for n in range(novenyek_sz-i-1):
        if viz[n] > viz[n+1]:
            viz[n], viz[n+1] = viz[n+1], viz[n]
kozep = novenyek_sz // 2
median = 0
if novenyek_sz % 2 ==1:
    median = viz[kozep]
else:
    median = (viz[kozep - 1] + viz[kozep]) / 2
median_i = -1
median_sz = 0
for i in range(novenyek_sz):
    if vizmas[i] == median and median_i == -1:
        median_i = i+1
    if vizmas[i] == median:
        median_sz += 1
print(median, median_i, median_sz)