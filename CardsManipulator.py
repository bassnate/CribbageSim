'''
Created on Sep 22, 2016

@author: nate
'''

class Man:
    def makeDeck(self, x):
        print(x)
        cards = ["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠",
                "A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣",
                "A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥",
                "A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"]
        return(cards)
    
    def shuffle(self,x):
        import numpy
        x = numpy.random.shuffle(x)
        return(x)
    
    def deal(self, dealer = "player", workingCards = None):
        if workingCards == None:
            print("Sorry. Code bugged out.")
            quit()
        if dealer == "player":
            playerHand = [workingCards[2],workingCards[4],workingCards[6],workingCards[8],workingCards[10],workingCards[12]]
            comHand = [workingCards[1],workingCards[3],workingCards[5],workingCards[7],workingCards[9],workingCards[11]]
        elif dealer == "com":
            playerHand = [workingCards[1],workingCards[3],workingCards[5],workingCards[7],workingCards[9],workingCards[11]]
            comHand = [workingCards[2],workingCards[4],workingCards[6],workingCards[8],workingCards[10],workingCards[12]]
        return(playerHand,comHand)
