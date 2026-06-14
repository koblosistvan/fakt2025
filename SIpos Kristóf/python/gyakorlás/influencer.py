#1.Fájl
forras=open("Sipos Kristóf\\python\\gyakorlás\\influencer_format_a.txt", mode='r', encoding="Utf-8")
year=[]
month=[]
day=[]
date=[]
name=[]
views=[]
likes=[]
share=[]
comments=[]
for sor in forras:
    adat=sor.strip().split('\t')
    date.append(str(adat[0]))
    name.append(str(adat[1]))
    views.append(int(adat[2]))
    likes.append(int(adat[3]))
    share.append(int(adat[4]))
    comments.append(int(adat[5]))
    datum = adat[0].split('-')
    year.append(int(datum[0]))
    month.append(int(datum[1]))
    day.append(int(datum[2]))  
forras.close

#2.Fájl

#3.Fájl

#4.Fájl
