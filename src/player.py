from src.card import Card
from src.deck import Deck

class Player(Deck):
    def __init__(self, Deck):
        self.hand = []
        self.name = ""
        self.score = 0
        self.hit(2, Deck)
        f"blah {self.hand}"

    def __str__(self):
        return f"{self.name} has {self.score} points."
    
    def hit(self, number_of_cards, Deck):
        for i in range(number_of_cards):
            self.hand.append(Deck.cards.pop())
    

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
        