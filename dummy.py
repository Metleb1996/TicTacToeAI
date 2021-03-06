from absgamer import ABSGamer
from tictactoe import TicTacToe
from random import randrange

class Dummy(ABSGamer):
    def __init__(self, name:str):
        self.name = name

    def getName(self):
        return self.name

    def getType(self):
        return "DUMMY"
        
    def playStep(self, game:TicTacToe, pos=-1):
        tryAgain = True
        while tryAgain:
            if pos not in range(9):
                p = randrange(9)
            else:
                p = pos
                tryAgain = False
            r = game.attack(self.name, p)
            if "is already filled" not in r:
                tryAgain = False
        return r, game