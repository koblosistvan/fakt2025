import random


COLOR = ["pikk", "káró", "kör", "treff"]
VAULE = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]


class Cards:
    def __init__(self, color, vaule):
        if color.lower() not in COLOR:
            raise Exception("Nem megfelelő szín")
        if vaule.upper() not in VAULE:
            raise Exception("Nem megfelelő érték")
        
        self.color = color
        self.vaule = vaule

    
    def __repr__(self):
        return f"{self.color} {self.vaule}"


class Deck:
    def __init__(self):
        self.cards = []
        for s in VAULE:
            for c in COLOR:
                self.cards.append(Cards(vaule = s, color = c))


    def __repr__(self):
        return f"{len(self.cards)}/52 lap"


    def shuffle(self):
        for _ in range(100):
            a = random.randint(0, len(self.cards)-1)
            b = random.randint(0, len(self.cards)-1)
            self.cards[a], self.cards[b] = self.cards[b], self.cards[a]

        
    def draw(self):
        c = self.cards[0]
        self.cards = self.cards[1:]
        return c


class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []


    def __repr__(self):
        return f"{self.vaule()} {self.cards} "


    def add_cards(self, c: Cards):
        self.cards.append(c)


    def vaule(self):
        v = 0
        a_count = 0
        for c in self.cards:
            if c.vaule in ("A"):
                v += 11
                a_count += 1
            elif c.vaule in ("J", "D", "K", "10"):
                v += 10
            else:
                v += int(c.vaule)
        
        sub_a = min((v-12)//10, a_count)

        return v - sub_a*10 if sub_a > 0 else v
jatek = True

while jatek:
    d = Deck()
    d.shuffle()
    print(d)
    oszto = Hand(name="Dealer")
    player = Hand(name="Kertész József")
    for _ in range(2):
        oszto.add_cards(c= d.draw())
        player.add_cards(c= d.draw())
    print("Osztó:", oszto.cards[0])
    print("Játékos:", player)

    if oszto.vaule() == 21:
        winner = oszto
    else:
        player_draws = input("Kérsz még lapot? (i/n): ")

        while player_draws == "i":
            player.add_cards(c=d.draw())
            print("Játékos:", player)
            if player.vaule() > 21:
                break
            player_draws = input("Kérsz még lapot? (i/n): ")
            

        winner  = None

        if player.vaule() > 21:
            winner = oszto

        else:
            while oszto.vaule() <17:
                oszto.add_cards(c= d.draw())
                print("Dealer:",oszto)

            if player.vaule() > oszto.vaule() or oszto.vaule() > 21:
                winner = player
            elif player.vaule() < oszto.vaule():
                winner = oszto

    print("A játéknak vége.")

    print("Dealer:",oszto)
    print("Játékos:",player)
    if winner:
        print(f"A győztes: {winner.name}")
    else:
        print("Döntetlen")

    uj_kor = input("Akarsz újra játszani? (i/n): ")
    if uj_kor == "i":
        jatek = True
    else:
        jatek = False