from src.card import Card
from src.deck import Deck

class Player(Deck):
    def __init__(self, Deck):
        self.hand = []
        self.name = ""
        self.score = 0
        self.acecount = 0 #list of aces in hand
        self.ingame = True
        self.bustflag = False
        self.hit(2, Deck)

    def __str__(self):
        return f"{self.name} has {self.score} points."
    
    def hit(self, number_of_cards, Deck): #method to hit, takes number of cards to take and deck to take from as arguments
        if self.ingame == True:
            for i in range(number_of_cards):
                    popcard = Deck.cards.pop() #take card from top of deck
                    self.hand.append(popcard) #add card to player's hand
                    if popcard.rank == "Ace": #check if card is an ace and add to count of aces
                        self.acecount += 1
                    if self.add_score(popcard.score) == False: #call addscore method, which adds up score of hand and adjusts for aces if needed, returns false if bust.
                        print("You have busted!")
                        self.bustflag = True
                        self.ingame = False #set end of game flag
                        break
        else: 
            print("You are out of the game!") #failsafe if out of game player tries to hit

            
    def stand(self, Deck): #if player stands, sets current score to end score, sets end of game flag and displays user message
        self.stand_score = self.score
        self.ingame = False #set end of game flag
        print("You have chosen to stand!") #output stand message
        print("Your score is: ", self.stand_score)
        print("Your hand is: ")
        for i in range(len(self.hand)):
            print(self.hand[i].rank)
            print(self.hand[i].suit)

    def discard(self):
        return self.hand.pop() #remove card from hand

    def add_score(self, score):
        self.score += score #adds input score to players score
        while self.acecount > 0 and self.score > 21: #if player has aces and score is over 21, adjust one ace to min value of 1, repeat until either score is under 21 or no aces left
            self.ace_adjust() #adjust one ace to min value of 1
        return self.validate_hand() #call method to check if score is over 21, return bool, method also used for testing and as second score check.
        

    def reset_score(self): #reset score method, used for testing
        self.score = 0

    def reset_hand(self): #reset hand method, used for testing
        self.hand = []
   
    def player_set_name(self): #set name method, not yet used
        self.name = input("What is your name? ")

    def validate_hand(self):
        if self.score != self.check_score(): #testing if statement to double check score to hand sum, could be removed
            print("ERROR: Score is not equal qto the sum of the cards in the hand!")
            return False

        if self.score > 21:     #check if score is over 21, return bool
            return False
        else:
            return True
    
    def check_score(self): #double check score method, also used in testing to sum up cards in hand (could change name to sum_cards)
        checkscore = 0
        for checkcard in self.hand: 
            checkscore += checkcard.score
        return checkscore
    
    def ace_adjust(self): #method to adjust ace value from 11 to 1, adjusts one ace per call.
            for i in range(len(self.hand)):
                if self.hand[i].rank == "Ace" and self.hand[i].score == 11:
                    self.hand[i].score = 1
                    self.score -= 10
                    self.acecount -= 1
                    break

        
