class Ember:
    def __init__(self, vezeteknev,keresztnev,magassag):
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.magassag = magassag

        self.nev = f'{vezeteknev} {keresztnev}'

    def __repr__(self):
        return f'{self.nev} ({self.magassag} cm)'
    
    def __gt__(self, other):
        return self.nev> other.nev
    

geza = Ember('Kövér','Géza', 209)
gizi= Ember('Szabó', 'Gizella', 167)

paros = [geza,gizi]
paros.sort()

print(paros)