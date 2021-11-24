import os
import datetime
import random
from absgamer import ABSGamer
from dummy import Dummy
from tictactoe import TicTacToe

class Agent(ABSGamer):
    def __init__(self, name:str, baseName:str = ".tictactoe"):
        self.name = name
        if not os.path.isfile('./'+baseName):
            baseName = str(datetime.datetime.utcnow().timestamp())+".tictactoe"
        self.baseName = baseName
        self.base = {} # example {'iiirrr---':{6:50, 7:50, 8:50}} i - men , r - rival(reqib)

    def getName(self):
        return self.name

    def boardToKey(self, board, i, r):
        s = str()
        empty = []
        for index in range(len(board)):
            if(board[index]==i):
                s = s+'i'
            elif(board[index]==r):
                s = s+'r'
            else:
                s = s+'-'
                empty.append(index)
        return s, empty

    def gameStateControl(self, game):
        if game.isWinned(gamer="X"):
            return "X", True
        if game.isWinned(gamer="O"):
            return "O", True
        if game.isBoardFilled():
            return "H", True
        return "msg", False

    def playStep(self, game:TicTacToe):
        pass

    def train(self, first:str, dum: Dummy, count:int):
        self.base.clear()
        self.game_history = {}
        for iii in range(count): # count sayda oyun
            game = TicTacToe(first=first)
            gamers = [dum, self]
            isEnd = False
            msg = str()
            empty = [*range(9)]
            key, _ = self.boardToKey(game.getBoard(), self.name, dum.name)
            while True: 
                if isEnd:
                    for game_step in self.game_history:
                        key = game_step
                        empty = self.game_history[key][0]
                        my_change = self.game_history[key][1]
                        if key not in list(self.base.keys()):
                            values = {}
                            for emp_box in empty:
                                values.update({emp_box: 50.0})
                            self.base.update({key: values})
                        if msg == self.name:
                            self.base[key][my_change] += ((100.0 - self.base[key][my_change])/2) 
                        if msg == dum.name:
                            self.base[key][my_change] = (self.base[key][my_change]/2) 
                    self.game_history.clear()
                    break
                for gamer in gamers:
                    if gamer == self:
                        my_change = empty[random.randrange(len(empty))]
                        _ = game.attack(gamer=self.name, pos=my_change)
                        step = {key:[empty,my_change]}
                        self.game_history.update(step)
                    else:
                        _, game = gamer.playStep(game=game);
                    b = game.getBoard()
                    key, empty = self.boardToKey(b, self.name, dum.name)
                    msg, isEnd = self.gameStateControl(game)
                    if(isEnd):
                        break
        for key in self.base:
            print(key, self.base[key])
