class card:
    def __init__(self, number, color, reverse, skip, wild, add):
        self.number = number
        self.color = color
        self.reverse = reverse
        self.skip = skip
        self.wild = wild
        self.add = add
    def view(self):
        if self.number != -1:
            return(f"{self.color} {self.number}")
        elif self.add == 2:
            return(f"{self.color} +{self.add}")
        elif wild == True and add == 4:
            return("Wild Draw 4")
        elif wild == True and add == 0:
            return("Wild")
        elif self.reverse == True:
            return(f"{self.color} Reverse")
        elif self.skip == True:
            return(f"{self.color} Skip")
class game:
    deck = []
    def __init__(self):
        for x in range(2):
            for i in range(1, 10):
                game.deck.append(card(i, "Red", False, False, False, 0))
            for i in range(1, 10):
                game.deck.append(card(i, "Yellow", False, False, False, 0))
            for i in range(1, 10):
                game.deck.append(card(i, "Blue", False, False, False, 0))
            for i in range(1, 10):
                game.deck.append(card(i, "Green", False, False, False, 0))
            game.deck.append(card(0, "Red", False, False, False, 0))
            game.deck.append(card(0, "Yellow", False, False, False, 0))
            game.deck.append(card(0, "Blue", False, False, False, 0))
            game.deck.append(card(0, "Green", False, False, False, 0))
            for i in range(2):
                game.deck.append(card(-1, "Red", False, False, False, 2))
                game.deck.append(card(-1, "Yellow", False, False, False, 2))
                game.deck.append(card(-1, "Blue", False, False, False, 2))
                game.deck.append(card(-1, "Green", False, False, False, 2))
a = game()
for v in range (len(a.deck)):
    print((a.deck[v]).view())
