Forrás_1=open('Sipos Kristóf\\python\\CS\\cs.csv',mode='r',encoding='utf-8')
Forrás_2=open('Sipos Kristóf\\python\\CS\\match_results.csv',mode='r',encoding='utf-8')

for sor in Forrás_1:
    adat=sor.strip().split(';')
    