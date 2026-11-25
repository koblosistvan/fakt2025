class ember:
    def __init__(self,veznev,keresztnev,mag):
        self.veznev = veznev
        self.keresztnev = keresztnev
        self.mag = mag
        self.nev = f'{veznev} {keresztnev}'

    def __repr__(self):
        return f'{self.nev} {self.mag}'


    def __gt__(self, other):
        return self.nev > other.nev

géza = ember("Kövér", "Géza", 200)
gizi = ember('Szabó', "Gizella", 167)
paros = [géza, gizi]
paros.sort()


print(paros)