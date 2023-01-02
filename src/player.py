from src.card import Card
from src.deck import Deck

class Player(Deck):
    def __init__(self, Deck):
        self.hand = []
        self.name = ""
        self.score = 0
        self.aceflag = False
        self.ingame = True
        self.bustflag = False
        self.hit(2, Deck)

    def __str__(self):
        return f"{self.name} has {self.score} points."
    
    def hit(self, number_of_cards, Deck):
        if self.ingame == True:
            for i in range(number_of_cards):
                    popcard = Deck.cards.pop()
                    if popcard.rank == "Ace":
                        self.aceflag = True 
                        if self.score > 10:
                            popcard.score = 1
                    self.hand.append(popcard)
                    if self.add_score(popcard.score) == False:
                        print("You have busted!")
                        self.bustflag = True
                        self.ingame = False
                        break
        else: 
            print("You are out of the game!")

            
    def stand(self, Deck):
        self.stand_score = self.score
        self.ingame = False
        print("You have chosen to stand!")
        print("Your score is: ", self.stand_score)
        print("Your hand is: ")
        for i in range(len(self.hand)):
            print(self.hand[i].rank)
            print(self.hand[i].suit)

    def discard(self):
        return self.hand.pop()

    def add_score(self, score):
        self.score += score
        if self.aceflag == True and self.score > 21:
            self.ace_adjust()
        return self.validate_hand()
        

    def reset_score(self):
        self.score = 0

    def reset_hand(self):
        self.hand = []
   
    def player_set_name(self):
        self.name = input("What is your name? ")

    def validate_hand(self):
       # if self.score != self.check_score():
      #      print("ERROR: Score is not equal qto the sum of the cards in the hand!")
     #       return False

        if self.score > 21:
            
            self.ace_adjust()
            return False
        else:
            return True
    
    def check_score(self):
        checkscore = 0
        for checkcard in self.hand: 
            checkscore += checkcard.score
        return checkscore
    
    def ace_adjust(self):
        if self.score > 10:
            for i in range(len(self.hand)):
                if self.hand[i].rank == "Ace" and self.hand[i].score == 11 and self.score > 21:
                    self.hand[i].score = 1
                    self.score -= 10
        