class TicTacToe:
    def __init__(self, first='X'):
        self.board = ['-','-','-','-','-','-','-','-','-']
        self.gamers = ['X', 'O']
        self.step = 'X'
        if first in self.gamers:
            self.step = first # 'X' or 'O'
        self.affordable = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def isBoardFilled(self):
        for item in self.board:
            if item == '-':
                return False
        return True

    def getBoard(self):
        return self.board

    def attack(self, gamer='Y', pos=9):
        if self.isBoardFilled():
            return "Board is filled"
        if pos not in range(9):
            return "{} not a valid position".format(str(pos))
        if gamer not in self.gamers:
            return "{} not a valid gamer".format(gamer)
        if gamer is not self.step:
            return "This is not a your ({}) step".format(gamer)
        if self.board[pos] != '-':
            return "{} is already filled".format(str(pos+1))
        else:
            self.board[pos] = gamer
            self.step = 'X' if self.step == 'O' else  'O'
            return "OK"
        
        
    def isWinned(self,gamer='X'):
        if gamer not in self.gamers:
            return False
        for variant in self.affordable:
            win = 0
            for pos in variant:
                if  self.board[pos] is gamer:
                    win+=1
            if win == 3:
                return True
        return False
        