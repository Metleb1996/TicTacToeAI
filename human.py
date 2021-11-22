from absgamer import ABSGamer
from tictactoe import TicTacToe

class Human(ABSGamer):
    def __init__(self, name:str):
        self.name = name


    def playStep(self, game:TicTacToe, pos=-1):
        r = game.attack(self.name, pos)
        return r, game