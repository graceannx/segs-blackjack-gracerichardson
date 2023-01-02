from src.deck import Deck
from src.card import Card
from src.player import Player
import time


def play():
    print('Hello, Welcome to Graces BlackJack Game')  # execution starts here!
    deck = Deck()
    player = Player(deck) # initialise a new player
    dealer = Player(deck)  # initialise a new dealer
    
    player.player_set_name() #set name
    print("\n")
   
    print("hello", player.name, "! \n") #greet player
    time.sleep(1)
    
    print("Your hand is: ") #show player hand
    time.sleep(1)
    player.show_hand()
    time.sleep(1)
    
    print("Your score is: ", player.score, "\n") #show player score
    time.sleep(1)
    
    print("The dealer is showing: ") #show dealer hand (1st card only)
    time.sleep(1)
    print (f"{dealer.hand[0].rank} of {dealer.hand[0].suit}")
    time.sleep(1)
    
    print("Dealers score is: ", dealer.hand[0].score) #show dealer score (1st card only)
    print("\n")
    time.sleep(1)
    
    
    while player.ingame == True:      #while loop to keep asking player for input until they stand or bust
        player_choice = input("Would you like to hit or stand?\n Enter h for hit or s for stand") #ask player for input
        if player_choice == "h": #if player chooses hit, call hit method - will set flag to false if player busts
            print("\n")
            time.sleep(1)
            print("You decided to hit!")
            time.sleep(1)
            player.hit(1, deck)
            print("\n")
            time.sleep(1)
        elif player_choice == "s": #if player chooses stand, call stand method - will set ingame flag to false
            print("\n")
            time.sleep(1)
            print("You decided to stand!")
            time.sleep(1)
            player.stand(deck)
            print("\n")
        else:
            print("Please enter a valid choice")
        print("Your hand is: ") #show player hand and score after most recent play
        player.show_hand()
        time.sleep(1)
        print("Your score is: ", player.score, "\n")
        print("\n")
        if player.bustflag == True: #if player has busted, display message
            print("You Busted!")
            print("\n")
            time.sleep(1)
        
    while dealer.ingame == True: #while loop to keep asking dealer for input until they stand or bust
        print("Dealers turn!")
        time.sleep(1)
        print("\n")
        print("Dealers hand is: ") #show dealer full hand
        dealer.show_hand()
        time.sleep(1)
        print("\n")
        dealer.dealer_play(deck) #call dealer play method - will set flag to false if dealer busts
        if dealer.bustflag == True:
            print("Dealer busted!") #if dealer has busted, display message
            time.sleep(1)
        elif dealer.stand_score != 0: 
            print("Dealer stands!") #if dealer has stood, display message
            time.sleep(1)
        else: 
            print("Dealer hits!")  #if dealer has hit, display message
            time.sleep(1)
        
        
        print("Dealers hand is: ") #show dealer hand after 1 play
        time.sleep(1)
        dealer.show_hand()
        print("\n")
        time.sleep(1)
        print("Dealers score is: ", dealer.score, "\n")
        time.sleep(1)
    
    
    #conditionals for the end of the game - could shorten for code efficiency
    if player.bustflag == True and dealer.bustflag == True:
        print("You both busted!")
        print("\n")
        print("You tied!")
        print("\n")
    
    elif player.bustflag == True and dealer.bustflag == False:
        print("You lose!")
        print("\n")
        

    elif dealer.bustflag == True and player.bustflag == False:
        print("You win!")
        print("\n")

    elif player.score > dealer.score:
        print("You win!")
        print("\n")
    
    elif player.score < dealer.score:
        print("You lose!")
        print("\n")

    elif player.score == dealer.score:
        print("You tie!")
        print("\n")

        



if __name__ == '__main__':
    play()
