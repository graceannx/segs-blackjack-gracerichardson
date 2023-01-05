import unittest
from src.deck import Deck
from src.card import Card
from src.player import Player


class PlayerTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.player = Player(self.deck)
        

    def tearDown(self):  # this method will be run after each tests
        self.player.reset_hand()
        self.player.reset_score()
        pass

    def test_number_of_cards_after_deal(self):  # any method beginning with 'test' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 50)
        self.assertEqual(len(self.player.hand), 2)

    def test_scenario_2(self):  # Given I have a valid hand of cards, When I choose to ‘hit’, Then I receive another card, And my score is updated
        number_of_cards = len(self.deck.cards)
        init_score = self.player.score
        self.player.hit(1, self.deck)
        self.assertEqual(len(self.player.hand), 3) 
#        print(self.player.score)
#       for i in range(len(self.player.hand)):
#            print(self.player.hand[i].rank)
#            print(self.player.hand[i].suit)
    
    def test_scenario_3(self):  # Given I have a valid hand of cards, When I choose to ‘stand’, Then I receive no further cards, And my score is evaluated
        number_of_cards = len(self.player.hand)
        if self.player.validate_hand() == True:
            self.player.stand(self.deck)
            self.assertEqual(len(self.player.hand), number_of_cards)
            self.assertEqual(self.player.score, self.player.stand_score)

    def test_scenario_4(self):  # Given my score is updated or evaluated, When it is 21 or less, Then I have a valid hand
        self.player.hit(1, self.deck)
        if self.player.validate_hand() == True:
            self.assertEqual(self.player.bustflag, False)
            self.assertLessEqual(self.player.score, 21)


    def test_scenario_5(self): #Given my score is updated, When it is 22 or more, Then I am ‘bust’ and do not have a valid hand
        self.player.hit(22, self.deck) #if there are 22 cards in the hand, there is no way to get a score of less than 22
        self.assertEqual(self.player.bustflag, True)

    def test_scenario_6(self): #Given I have a king and an ace,When my score is evaluated, Then my score is 21
        self.player.reset_hand()
        self.player.reset_score()
        self.player.hand.append(Card("Spades", "Ace"))
        self.player.hand.append(Card("Spades", "King"))
        score1 = self.player.check_score()
        self.assertEqual(score1, 21) 
#        print(score1)

    def test_scenario_7(self): #Given I have a king, a queen, and an ace, When my score is evaluated, Then my score is 21
        #In the play method, this validation is triggered by the hit method, but here I want to use a custom hand. 
        # To bypass this, I create a hand and then pass it to the add_score method, where the validation occurs within the hit method.
        self.player.reset_hand()
        self.player.reset_score()
        self.player.hand.append(Card("Spades", "King"))
        self.player.hand.append(Card("Spades", "Queen"))
        self.player.hand.append(Card("Spades", "Ace"))
        self.player.acecount = 1 #the aces are counted in my hit method, so this is hardcoded here to bypass for testing.
        self.player.add_score(self.player.check_score()) #here, check_score is used to sum the hand custom hand, and return its score. The score and, by proxy, hand is passed into add_score which adjusts the scores of the aces in the hand (from 11 to 1) if necessary.
        score2 = self.player.check_score() #check_score is used again to sum the new hand, and return the score of the hand.
#        self.player.show_hand()
        self.assertEqual(score2, 21) 
 #       print(score2)
    
    def test_scenario_8(self): #Given I have a king, a queen, and an ace, When my score is evaluated, Then my score is 21
        #the same procedure as scenario 7 is used to test this custom hand.
        self.player.reset_hand()
        self.player.reset_score()
        self.player.hand.append(Card("Spades", "Ace"))
        self.player.hand.append(Card("Hearts", "Ace"))
        self.player.hand.append(Card("Clubs", "Jack"))
        self.player.hand.append(Card("Diamonds", "Ace"))
        self.player.hand.append(Card("Diamonds", "7"))
        self.player.hand.append(Card("Clubs", "Ace"))
        self.player.acecount = 4
        self.player.add_score(self.player.check_score())
        score3 = self.player.check_score()
        self.assertEqual(score3, 21)
 #       print(score3)

    def test_scenario_9(self): # Given that I have a nine, an ace, and another ace,When my score is evaluated, Then my score is 21
        #the same procedure as scenario 7 is used to test this custom hand.
        self.player.reset_hand()
        self.player.reset_score()
        self.player.hand.append(Card("Spades", "9"))
        self.player.hand.append(Card("Hearts", "Ace"))
        self.player.hand.append(Card("Diamonds", "Ace"))
        self.player.acecount = 2
        self.player.add_score(self.player.check_score())
        score4 = self.player.check_score()
        self.assertEqual(score4, 21)
#        print(score4)


if __name__ == '__main__':
    unittest.main()
