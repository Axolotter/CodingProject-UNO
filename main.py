import random
class card:
    def __init__(self, number, color, reverse, skip, wild, add):
        self.number = number
        self.color = color
        self.reverse = reverse
        self.skip = skip
        self.wild = wild
        self.add = add
        if color == "Red":
            self.code = "\x1b[0;38;2;255;0;0;49m"
        elif color == "Yellow":
            self.code = "\x1b[0;38;2;255;255;0;49m"
        elif color == "Blue":
            self.code = "\x1b[0;38;2;0;0;255;49m"
        elif color == "Green":
            self.code = "\x1b[0;38;2;0;255;0;49m"
        elif color == "Wild":
            self.code = "\x1b[0;38;2;114;19;209;49m"
    def view(self):
        if self.number != -1:
            return(self.code + self.color + " " + str(self.number) + "\x1b[0m")
        elif self.add == 2:
            return(self.code + self.color + " Draw " + str(self.add) + "\x1b[0m")
        elif self.wild == True and self.add == 4:
            return(self.code + self.color + "\x1b[0m")
        elif self.wild == True and self.add == 0:
            return(self.code + self.color + "\x1b[0m")
        elif self.reverse == True:
            return(self.code + self.color + " Reverse" + "\x1b[0m")
        elif self.skip == True:
            return(self.code + self.color + " Skip" + "\x1b[0m")
class game:
    deck = []
    turns = []
    activeCard = None
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

            game.deck.append(card(-1, "Red", True, False, False, 0))
            game.deck.append(card(-1, "Yellow", True, False, False, 0))
            game.deck.append(card(-1, "Blue", True, False, False, 0))
            game.deck.append(card(-1, "Green", True, False, False, 0))

            game.deck.append(card(-1, "Red", False, True, False, 0))
            game.deck.append(card(-1, "Yellow", False, True, False, 0))
            game.deck.append(card(-1, "Blue", False, True, False, 0))
            game.deck.append(card(-1, "Green", False, True, False, 0))
            
        game.deck.append(card(-1, "Wild", False, False, True, 0))
        game.deck.append(card(-1, "Wild", False, False, True, 0))
        game.deck.append(card(-1, "Wild", False, False, True, 0))
        game.deck.append(card(-1, "Wild", False, False, True, 0))
        
        game.deck.append(card(-1, "Wild Draw 4", False, False, True, 4))
        game.deck.append(card(-1, "Wild Draw 4", False, False, True, 4))
        game.deck.append(card(-1, "Wild Draw 4", False, False, True, 4))
        game.deck.append(card(-1, "Wild Draw 4", False, False, True, 4))

    def shuffle(self):
        uDeck = game.deck
        game.deck = []
        l = len(uDeck)
        for i in range(l):
            r = random.randint(0, len(uDeck)-1)
            game.deck.append(uDeck[r])
            del uDeck[r]
    def getStart(self):
        if game.deck[0].number != -1:
            game.activeCard = game.deck[0]
            del game.deck[0]
        else:
            game.deck.insert(random.randint(0, len(game.deck)-1), game.deck.pop(0))
            self.getStart()
    def play(self):
        space()
        input(f"{game.turns[0].name}, Press enter to start your turn.")
        space()
        print(f"==============={game.turns[0].name}===============")
        print("")
        print(f"Top Card: {game.activeCard.view()}")
        print("")
        print("Your Cards:")
        game.turns[0].viewHand()
        print(str(len(game.turns[0].hand)+1) + ": " + "Draw a new card")
        print("")
        def check(pos):
            if game.turns[0].hand[pos-1].wild == True:
                print("")
                print("What color would you like to make it?")
                print("\x1b[0;38;2;255;0;0;49m1: Red")
                print("\x1b[0;38;2;255;255;0;49m2: Yellow")
                print("\x1b[0;38;2;0;0;255;49m3: Blue")
                print("\x1b[0;38;2;0;255;0;49m4: Green\x1b[0m")
                n = int(input())
                if n == 1:
                    game.turns[0].hand[pos-1].color = ("Wild (Red)")
                    game.turns[0].hand[pos-1].code = "\x1b[0;38;2;255;0;0;49m"
                elif n == 2:
                    game.turns[0].hand[pos-1].color = ("Wild (Yellow)")
                    game.turns[0].hand[pos-1].code = "\x1b[0;38;2;255;255;0;49m"
                elif n == 3:
                    game.turns[0].hand[pos-1].color = ("Wild (Blue)")
                    game.turns[0].hand[pos-1].code = "\x1b[0;38;2;0;0;255;49m"
                elif n == 4:
                    game.turns[0].hand[pos-1].color = ("Wild (Green)")
                    game.turns[0].hand[pos-1].code = "\x1b[0;38;2;0;255;0;49m"
                game.activeCard = game.turns.hand[pos-1]
                game.turns.insert(-1, game.turns[0].pop)
                self.play
            elif game.turns[0].hand[pos-1].color == game.activeCard.color or game.turns[0].hand[pos-1].number == game.activeCard.number:
                print("")
                print("Same color or number")
            else:
                print("")
                print(f"\x1b[0;38;2;255;0;0;49mA {game.turns[0].hand[pos-1].view()} \x1b[0;38;2;255;0;0;49mcannot be played on a {game.activeCard.view()}")
        check(int(input("Enter the position of the card you want to play: ")))
class player:
    def __init__(self, name, startsize):
        self.name = name
        self.hand = []
        for i in range(startsize):
            self.hand.append(game.deck[0])
            del game.deck[0]
    def viewHand(self):
        for item in self.hand:
            print(f"{self.hand.index(item)+1}: {item.view()}")

    def drawCard(self, count):
        for i in range(count):    
            self.hand.append(game.deck[0])
            del game.deck[0]
        
a = game()
a.shuffle()
players = int(input("How many players? "))
for y in range(players):
    name = str(input(f"What is Player {(y+1)}'s Name? "))
    game.turns.append(player(name, 20))
a.getStart()
def space():
    for i in range(100):
        print("")
a.play()