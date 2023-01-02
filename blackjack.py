from src.deck import Deck
from src.card import Card
from src.player import Player
import time


def play():
    print('Hello, Welcome to Graces BlackJack Game')  # execution starts here!
    deck = Deck()
    player = Player(deck)
    dealer = Player(deck)
    player.player_set_name()
    print("\n")
    print("hello", player.name, "! \n")
    time.sleep(1)
    print("Your hand is: ")
    time.sleep(1)
    player.show_hand()
    time.sleep(1)
    print("Your score is: ", player.score, "\n")
    time.sleep(1)
    print("The dealer is showing: ")
    time.sleep(1)
    print (f"{dealer.hand[0].rank} of {dealer.hand[0].suit}")
    time.sleep(1)
    print("Dealers score is: ", dealer.hand[0].score)
    print("\n")
    time.sleep(1)
    
    
    while player.ingame == True:    
        player_choice = input("Would you like to hit or stand?\n Enter h for hit or s for stand")
        if player_choice == "h":
            print("\n")
            time.sleep(1)
            print("You decided to hit!")
            time.sleep(1)
            player.hit(1, deck)
            print("\n")
            time.sleep(1)
            
            
            
        elif player_choice == "s":
            print("\n")
            time.sleep(1)
            print("You decided to stand!")
            time.sleep(1)
            player.stand(deck)
            print("\n")
        else:
            print("Please enter a valid choice")
        
        print("Your hand is: ")
        player.show_hand()
        time.sleep(1)
        print("Your score is: ", player.score, "\n")
        print("\n")
        if player.bustflag == True:
                print("You Busted!")
                print("\n")
                time.sleep(1)
        
    while dealer.ingame == True:
        print("Dealers turn!")
        time.sleep(1)
        print("\n")
        print("Dealers hand is: ")
        dealer.show_hand()
        time.sleep(1)
        print("\n")
        dealer.dealer_play(deck)
        if dealer.bustflag == True:
            print("Dealer busted!")
            time.sleep(1)
        elif dealer.stand_score != 0: 
            print("Dealer stands!")
        else: 
            print("Dealer hits!")
        
        
        print("Dealers hand is: ")
        time.sleep(1)
        dealer.show_hand()
        print("\n")
        time.sleep(1)

        time.sleep(1)
        print("Dealers score is: ", dealer.score, "\n")
        time.sleep(1)

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

        



if __name__ == '__main__':
    play()
