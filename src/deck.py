from src.card import Card



class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = []
        for suit in suits: 
            for rank in ranks: 
                self.cards.append(Card(suit, rank))

    def __str__(self):
        return f"Deck of {self.count()} cards."
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)

        
    






