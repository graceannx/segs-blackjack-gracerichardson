from src.card import Card
from src.deck import Deck

class Player(Deck):
    def __init__(self, Deck):
        self.hand = []
        self.name = ""
        self.score = 0
        self.Aceflag = False
        self.ingame = True
        self.hit(2, Deck)

    def __str__(self):
        return f"{self.name} has {self.score} points."
    
    def hit(self, number_of_cards, Deck):
        if self.ingame == True:
            for i in range(number_of_cards):
                    popcard = Deck.cards.pop()
                    if popcard.rank == "Ace":
                        Aceflag = True 
                        if self.score > 10:
                            popcard.score = 1
                    self.score += popcard.score
                    self.hand.append(popcard)
                    if self.validate_hand() == False:
                        print("You have busted!")
                        self.ingame = False
                        break
        else: 
            print("You are out of the game!")

            
    

    def discard(self):
        return self.hand.pop()

    def add_score(self, score):
        self.score += score

    def reset_score(self):
        self.score = 0

    def reset_hand(self):
        self.hand = []
   
    def player_set_name(self):
        self.name = input("What is your name? ")

    def validate_hand(self):
        if self.score > 21:
            return False
        else:
            return True
        