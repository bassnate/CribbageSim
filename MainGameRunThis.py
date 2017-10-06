'''
Created on Sep 22, 2016

@author: nate
'''
import CardsManipulator
import AI
import Board

print("Initializing")
deck = CardsManipulator.Man.makeDeck(CardsManipulator.Man.makeDeck,"Deck Created")
Board.Board.InitializeBoard(Board.Board.InitializeBoard, "Board Initialized")
print("Initialization Complete")
startAffirmation = input("Start Game(Y/N)? \n >>>").lower()
if startAffirmation == "n": quit()
#print(deck)
CardsManipulator.Man.shuffle(CardsManipulator.Man.shuffle, deck)
#print(deck)


dealchoice = input("Who should be dealer first? (player/com) \n >>>")
print()
print("The cards will be formatted a certain way, number then suit.")
print("Since this is a computer and you are playing this in terminal,")
print("please know that the game operates with a zero index, 0 on the left")
print("and ascending to the right. In parenthesis next to the question I will")
print("give you the options that you can choose from, and the format.")
print("Thank you for playing!")


#CardsManipulator.deal returns a list of 2 playerHand then comHand
hands = CardsManipulator.Man.deal(CardsManipulator.Man.deal, dealer = dealchoice, workingCards = deck)
#print the player's hand
print(hands[0])
cribCardsP = input("Which cards to place in the crib? (0-5 from the left) (x,y) \n >>>")
cribCardsP = cribCardsP.strip("(")
cribCardsP = cribCardsP.strip(")")
cribCardsP = cribCardsP.split(",")
cribCardsP[0] = int(cribCardsP[0])
cribCardsP[1] = int(cribCardsP[1])
cribCardsC = AI.AI1.chooseCrib(AI.AI1.chooseCrib,hands[1])
cribCardsC[0] = cribCardsC[0]
cribCardsC[1] = cribCardsC[1]

crib = [hands[0][cribCardsP][0], hands[0][cribCardsP][1], hands[1][cribCardsC][0], hands[1][cribCardsP][1]]
