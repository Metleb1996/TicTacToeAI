import os
import random
from absgamer import ABSGamer
from tictactoe import TicTacToe

class Agent(ABSGamer):
    def __init__(self, name:str, baseName:str = "l1.tictactoe"):
        self.name = name
        self.baseName = baseName
        self.base = {} # example {'iiirrr---':{6:{'+':0,'-':0,'n':0},7:{'+':0,'-':0,'n':0},8:{'+':0,'-':0,'n':0}}} i - men , r - rival(reqib)
        if os.path.isfile('./'+baseName):
            self.loadFile(baseName)
            

    def loadFile(self, fname):
        lines = []
        with open('./'+fname, 'r') as baseFile:
            lines = baseFile.readlines()
            baseFile.close()
        if len(lines) > 0:
            for line in lines:
                parts = line.split('>')
                key = parts[0]
                value = {}
                for i in range(1, len(parts)):
                    v = parts[i].split(":")
                    value.update({int(v[0]):{'+':int(v[1]),'-':int(v[2]),'n':int(v[3])}})
                self.base.update({key:value})
        
    def saveFile(self):
        with open('./'+self.baseName, 'w') as f:
            for key in self.base:
                line = str(key)
                for vareant in self.base[key]:
                    line = line+">"+str(vareant)+":"+str(self.base[key][vareant]['+'])+":"+str(self.base[key][vareant]['-'])+":"+str(self.base[key][vareant]['n'])
                line += '\n'
                f.write(line)

    def getName(self):
        return self.name
    
    def getType(self):
        return "AGENT"

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

    def playStep(self, game:TicTacToe):
        rival = "X" if self.name == "O" else "O"
        key, empty = self.boardToKey(game.getBoard(), self.name, rival)
        my_change = {"pos":empty[0], "val":-1}
        variants = self.base[key]
        for variant in variants:
            if (variants[variant]['+']+variants[variant]['-']+variants[variant]['n']) == 0:
                val = 0.0
            else:
                val = (variants[variant]['+']-variants[variant]['-'])/(variants[variant]['+']+variants[variant]['-']+variants[variant]['n']); 
            if val > my_change['val']:
                my_change['pos'] = variant
                my_change['val'] = val
        r = game.attack(gamer=self.name, pos=my_change['pos'])
        return r, game

    def train(self, rival: ABSGamer, count:int):
        self.game_history = {}
        for first in ['X', 'O']:
            for iii in range(count): # count sayda oyun
                print("Step:  ", iii)
                game = TicTacToe(first=first)
                gamers = [rival, self]
                isEnd = False
                msg = str()
                empty = [*range(9)]
                key, _ = self.boardToKey(game.getBoard(), self.name, rival.name)
                while True: 
                    if isEnd:
                        for game_step in self.game_history:
                            key = game_step
                            empty = self.game_history[key][0]
                            my_change = self.game_history[key][1]
                            if key not in list(self.base.keys()):
                                values = {}
                                for emp_box in empty:
                                    values.update({emp_box: {'+':0, '-':0, 'n':0}})
                                self.base.update({key: values})
                            if msg == self.name:
                                self.base[key][my_change]['+'] += 1
                            if msg == rival.name:
                                self.base[key][my_change]['-'] += 1 
                            if msg == "H":
                                self.base[key][my_change]['n'] += 1 
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
                        key, empty = self.boardToKey(b, self.name, rival.name)
                        if game.isWinned(gamer="X"):
                            msg = "X"
                            isEnd = True
                        elif game.isWinned(gamer="O"):
                            msg = "O"
                            isEnd = True
                        elif game.isBoardFilled():
                            msg = "H"
                            isEnd = True
                        if(isEnd):
                            break
        self.saveFile()
