import sys
import math

# 6 Degrees of Kevin Bacon!

# adatok beolvasása
actor_name = input()
n = int(input())
movies = []             # kell egy lista, amiben a filmek szereplőit tároljuk
for i in range(n):
    movie_cast = input()
    actors = [] # alakítsuk ezt át úgy, hogy az adott film szereplői legyenek egy listában
    movies.append(actors)

# a BFS-hez szükséges változók
visited = []        # már meglátogatott színészek listája
queue = []          # a bejárás során felfedezett, de még nem meglátogatott színészek listája
queue_dist = []     # a bejárási mélység
distance = 0        # ez lesz a válaszunk, de kell neki egy kezdőérték, hogy ne reklamáljon a python

while len(queue) > 0:
    # kivesszük a sorból a legrégebben bekerült színészt
    
    neighbours = []
    # kigyűjtjük a szomszédait, azaz azokat a színészeket, akikkel együtt szerepelt egy filmben
    # ehhez végig kell mennünk a filmek listáján
    # ha a filmben szerepel a kivett színész, akkor az összes többi szereplőt hozzáadjuk a szomszédok listájához
    # persze csak akkor, ha még nincs benne a szomszédok között
    # ehhez kell majd egy belső ciklus is a film szereplőin


    # ha a szomszédok között van Kevin Bacon, akkor vége a keresésnek
    # kiürítjük a sort, hogy a külső ciklus is véget érjen
    
    
    # egyébként megnézzük a szomszédokat egyesével
    # ha a szomszéd nincs se a sorban, se a meglátogatottak között, akkor a sor végére tesszük
    # és a bejárás mélységét is elmentjük a queue_dist listában


    # végül a kivett színészt áthelyezzük a meglátogatottak közé
    # és eltávolítjuk a sorból és a mélységlistából is

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(distance)
