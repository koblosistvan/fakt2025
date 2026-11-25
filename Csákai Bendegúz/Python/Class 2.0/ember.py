import os
os.system('cls')
class Ember:
    def __init__(self, veznev, kernev, mag):
        self.veznev = veznev
        self.kernev = kernev
        self.mag = mag
        self.nev = f'{veznev} {kernev}'
    def __repr__(self):
        return f'{self.nev} ({self.mag} cm)'

    def __gt__(self, other):
        return self.nev > other.nev

geza = Ember('Kövér','Géza', 209)
gizi = Ember('Szabó','Gizella', 167)
feri = Ember('Tátra','Ferenc', 198)
trio = [geza, gizi, feri]
trio.sort()
print(trio)