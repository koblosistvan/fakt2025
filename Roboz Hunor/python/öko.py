forras = open('fakt2025\\Roboz Hunor\\python\\ökolábnyom.csv', mode='r', encoding='utf-8')
kód = []
ország=[]
régió = []
év= []
felh=[]
kapacitás = []
lakosság = []
gdp=[]
for sor in range(forras):
    adat = sor.strip().split(',')
    kód.append(adat[0])
    ország.append(adat[1])