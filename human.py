from absgamer import ABSGamer
from tictactoe import TicTacToe

class Human(ABSGamer):
    def __init__(self, name:str):
        self.name = name

    def getName(self):
        return self.name

    def getType(self):
        return "HUMAN"

    def playStep(self, game:TicTacToe, pos=-1):
        r = game.attack(self.name, pos)
        return r, game