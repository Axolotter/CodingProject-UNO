import random
class card:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        if color == "Red":
            self.code = "\x1b[0;38;2;255;0;0;49m"
        elif color == "Yellow":
            self.code = "\x1b[0;38;2;255;255;0;49m"
        elif color == "Blue":
            self.code = "\x1b[0;38;2;0;0;255;49m"
        elif color == "Green":
            self.code = "\x1b[0;38;2;0;255;0;49m"
    def view(self):
        return(self.code + self.color + " " + str(self.number) + "\x1b[0m")
    def play(self, pos):
        game.activeCard = game.turns[0].hand[pos-1]
        del game.turns[0].hand[pos-1]
        game.turns.append(game.turns.pop(0))        
        
class wild(card):
    def __init__(self, number, color):
        super().__init__(number, color)
        self.code = "\x1b[0;38;2;114;19;209;49m"
    def view(self):
        return(self.code + self.color + "\x1b[0m")
    def play(self, pos):
        print("")
        print("What color would you like to make it?")
        print("\x1b[0;38;2;255;0;0;49m1: Red")
        print("\x1b[0;38;2;255;255;0;49m2: Yellow")
        print("\x1b[0;38;2;0;0;255;49m3: Blue")
        print("\x1b[0;38;2;0;255;0;49m4: Green\x1b[0m")
        n = int(input())
        if n == 1:
            game.turns[0].hand[pos-1].color = ("Red")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;255;0;0;49m"
        elif n == 2:
            game.turns[0].hand[pos-1].color = ("Yellow")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;255;255;0;49m"
        elif n == 3:
            game.turns[0].hand[pos-1].color = ("Blue")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;0;0;255;49m"
        elif n == 4:
            game.turns[0].hand[pos-1].color = ("Green")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;0;255;0;49m"
        game.activeCard = game.turns[0].hand[pos-1]
        del game.turns[0].hand[pos-1]
        game.turns.append(game.turns.pop(0))

class draw4(card):
    def __init__(self, number, color):
        super().__init__(number, color)
        self.code = "\x1b[0;38;2;114;19;209;49m"
    def view(self):
        return(self.code + self.color + "\x1b[0m")
    def play(self, pos):
        print("")
        print("What color would you like to make it?")
        print("\x1b[0;38;2;255;0;0;49m1: Red")
        print("\x1b[0;38;2;255;255;0;49m2: Yellow")
        print("\x1b[0;38;2;0;0;255;49m3: Blue")
        print("\x1b[0;38;2;0;255;0;49m4: Green\x1b[0m")
        n = int(input())
        if n == 1:
            game.turns[0].hand[pos-1].color = ("Red")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;255;0;0;49m"
        elif n == 2:
            game.turns[0].hand[pos-1].color = ("Yellow")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;255;255;0;49m"
        elif n == 3:
            game.turns[0].hand[pos-1].color = ("Blue")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;0;0;255;49m"
        elif n == 4:
            game.turns[0].hand[pos-1].color = ("Green")
            game.turns[0].hand[pos-1].code = "\x1b[0;38;2;0;255;0;49m"
        game.activeCard = game.turns[0].hand[pos-1]
        del game.turns[0].hand[pos-1]
        game.turns.append(game.turns.pop(0))
        game.turns[0].drawCard(4)
        space()
        input(f"{game.turns[0].name}, you drew 4 cards. Press enter to move to the next player.")
        game.turns.append(game.turns.pop(0)) 
class skip(card):
    def __init__(self, number, color):
        super().__init__(number, color)
    def view(self):
        return(self.code + self.color + " Skip" + "\x1b[0m")
    def play(self, pos):
        game.activeCard = game.turns[0].hand[pos-1]
        del game.turns[0].hand[pos-1]
        game.turns.append(game.turns.pop(0))
        space()
        input(f"{game.turns[0].name}, your turn was skipped. Press enter to move to the next player.")
        game.turns.append(game.turns.pop(0)) 
    
class reverse(card):
    def __init__(self, number, color):
        super().__init__(number, color)
    def view(self):
        return(self.code + self.color + " Reverse" + "\x1b[0m")
    def play(self, pos):
        if len(game.turns) == 2:
            game.activeCard = game.turns[0].hand[pos-1]
            del game.turns[0].hand[pos-1]
        else:
            game.activeCard = game.turns[0].hand[pos-1]
            del game.turns[0].hand[pos-1]
            game.turns.reverse()
class draw2(card):
    def __init__(self, number, color):
        super().__init__(number, color)
    def view(self):
        return(self.code + self.color + " Draw 2" + "\x1b[0m")
    def play(self, pos):
        game.activeCard = game.turns[0].hand[pos-1]
        del game.turns[0].hand[pos-1]
        game.turns.append(game.turns.pop(0))
        game.turns[0].drawCard(2)
        space()
        input(f"{game.turns[0].name}, you drew 2 cards. Press enter to move to the next player.")
        game.turns.append(game.turns.pop(0)) 
class game:
    deck = []
    turns = []
    activeCard = None
    def __init__(self):
        for x in range(2):
            for i in range(1, 10):
                game.deck.append(card(i, "Red"))
            for i in range(1, 10):
                game.deck.append(card(i, "Yellow"))
            for i in range(1, 10):
                game.deck.append(card(i, "Blue"))
            for i in range(1, 10):
                game.deck.append(card(i, "Green"))
        game.deck.append(card(0, "Red"))
        game.deck.append(card(0, "Yellow"))
        game.deck.append(card(0, "Blue"))
        game.deck.append(card(0, "Green"))
        for i in range(2):
            game.deck.append(reverse(-1, "Red"))
            game.deck.append(reverse(-1, "Yellow"))
            game.deck.append(reverse(-1, "Blue"))
            game.deck.append(reverse(-1, "Green"))

            game.deck.append(skip(-1, "Red"))
            game.deck.append(skip(-1, "Yellow"))
            game.deck.append(skip(-1, "Blue"))
            game.deck.append(skip(-1, "Green"))

            game.deck.append(draw2(-1, "Red"))
            game.deck.append(draw2(-1, "Yellow"))
            game.deck.append(draw2(-1, "Blue"))
            game.deck.append(draw2(-1, "Green"))
            
        game.deck.append(wild(-1, "Wild"))
        game.deck.append(wild(-1, "Wild"))
        game.deck.append(wild(-1, "Wild"))
        game.deck.append(wild(-1, "Wild"))
        
        game.deck.append(draw4(-1, "Wild Draw 4"))
        game.deck.append(draw4(-1, "Wild Draw 4"))
        game.deck.append(draw4(-1, "Wild Draw 4"))
        game.deck.append(draw4(-1, "Wild Draw 4"))

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
        if(len(game.turns[1].hand) == 0):
            print("=============================================")
            print(f"Game over! {game.turns[1].name} won!")
            return True
        
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
            if pos == (len(game.turns[0].hand)+1):
                game.turns[0].drawCard(1)
                self.play()
            elif isinstance(game.turns[0].hand[pos-1], wild) or isinstance(game.turns[0].hand[pos-1], draw4):
                game.turns[0].hand[pos-1].play(pos)
                self.play()
                return True
            elif game.turns[0].hand[pos-1].color == game.activeCard.color or game.turns[0].hand[pos-1].number == game.activeCard.number:
                game.turns[0].hand[pos-1].play(pos)
                self.play()
                return True
            else:
                print("")
                print(f"\x1b[0;38;2;255;0;0;49mA {game.turns[0].hand[pos-1].view()} \x1b[0;38;2;255;0;0;49mcannot be played on a {game.activeCard.view()}")
                return False
        
        while True:
            try: 
                cardPlay = check(int(input("Enter the position of the card you want to play: ")))
                while cardPlay == False:
                    cardPlay = check(int(input("Enter the position of the card you want to play: ")))
                break
            except:
                print("Enter a valid number.")
        
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
while True:
    try: 
        players = int(input("How many players? "))
        break
    except:
        print("Enter a valid number.")

for y in range(players):
    name = str(input(f"What is Player {(y+1)}'s Name? "))
    game.turns.append(player(name, 7))
a.getStart()
def space():
    for i in range(100):
        print("")
a.play()