'''
Created on Sep 22, 2016

@author: bassist314
'''

class AI1:
    
    def chooseCrib(self, setOfCards):
        playingHand = dict()
        for i in range(3):
            for u in range((i+1),4):
                for o in range((u+1),5):
                    for p in range((o+1),6):
                        HandID = [i,u,o,p]
                        playingHand[HandID] = 0
        print(playingHand)
        
        for setofCards in playingHand:
            for card in setofCards:
                card = card.split("")
                if card[0] == "A":
                    card[0] = "1"
                if card[0] == "J":
                    card[0] = "11" 
                if card[0] == "Q":
                    card[0] = "12"
                if card[0] == "K":
                    card[0] = "13"
                    
        points = {}
        for setofCards in playingHand:
            points[setofCards] = points[setofCards] + AI1.checkFor15(self, setofCards)
            points[setofCards] = points[setofCards] + AI1.checkForPairs(self,setofCards)
            points[setofCards] = points[setofCards] + AI1.checkForRuns(self, setofCards)
        
        #print(playingHand) 
#        cribCards = []
#        for card in goodHand:
#            cribCards = setOfCards.__delitem__(card)
        cribCard1 = playingHand[0][0]
        cribCard2 = playingHand[0][1]
        return(cribCard1,cribCard2)
    
    def checkFor15(self, hand):
        addpoints = 0
        for card in hand:
            card = int(card[0])
            if card > 10:
                card = 10
        if hand[0] + hand[1] + hand[2] + hand[3] < 15:
            addpoints = 0
        elif hand[0] + hand[1] + hand[2] + hand[3] == 15:
            addpoints = 2
        else:
            if(hand[0]+hand[1] == 15):addpoints = addpoints + 2
            if(hand[1]+hand[2] == 15):addpoints = addpoints + 2
            if(hand[2]+hand[3] == 15):addpoints = addpoints + 2
            if(hand[0]+hand[2] == 15):addpoints = addpoints + 2
            if(hand[0]+hand[3] == 15):addpoints = addpoints + 2
            if(hand[1]+hand[3] == 15):addpoints = addpoints + 2
        return(addpoints)
    
    def checkForPairs(self, hand):
        addpoints = 0
        for i in range(1,4):
            if hand[0] == hand[i]: addpoints = addpoints + 2
        for i in range(2,4):
            if hand[1] == hand[i]: addpoints = addpoints + 2
        for i in range(3,4):
            if hand[2] == hand[i]: addpoints = addpoints + 2
        
    #def checkForRuns(self, hand):
        #modhand = hand.sort()
