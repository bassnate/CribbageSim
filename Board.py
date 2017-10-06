'''
Created on Sep 22, 2016

@author: nate
'''

class Board:
    
    def InitializeBoard(self, x):
        print(x)
        Board.win = 121
        Board.playerScore = 0
        Board.comScore = 0
        Board.winner = False
        
    def Score(self,opponent,value):
        if opponent == "player":
            Board.playerScore = Board.playerScore + value
        
        if opponent == "com":
            Board.comScore = Board.comScore + value
    
