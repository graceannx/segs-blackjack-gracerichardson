#from src.card import Card
#from src.deck import Deck

class Player:
    def __init__(self):
        self.hand = []
        self.name = ""
        self.score = 0
       # Deck.deal(self, 2)
        f"{self.hand}"

    def __str__(self):
        return f"{self.name} has {self.score} points."
    
    def hit(self, deck):
        self.hand.append(deck.deal(1))

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
        