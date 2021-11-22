from abc import ABC, abstractmethod
from tictactoe import TicTacToe

class ABSGamer():
    @abstractmethod
    def __init__(self, name: str):
        pass
    @abstractmethod
    def playStep(self, game: TicTacToe, pos: int):
        pass