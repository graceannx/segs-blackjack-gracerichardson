class Card: 
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        if rank == "Jack" or rank == "Queen" or rank == "King":
            self.score = 10
        elif rank == "Ace":
            self.score = 11
        else:
            self.score = int(rank)
            
    # def __str__(self):
    #     return self.rank + " of " + self.suit
