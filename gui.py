from kivy.app import App
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from tictactoe import TicTacToe
from human import Human
from agent import Agent

Window.size = (400, 400)

bg_normal = '31419F'
bg_gamer = '5BAF51'
bg_rival = 'AE3557'

class Box(Button):
    id = None
    clickable = True

class TicTacToeApp(App):
    boxes = []
    def build(self):
        self.first_gamer = Human(name='X')
        self.second_gamer = Agent(name='O')
        self.game = TicTacToe(first=self.first_gamer.getName())
        self.isEnd = False
        self.gamers = [self.first_gamer, self.second_gamer]
        board = GridLayout(cols=3)
        for i in range(9):
            b = Box(text=' ', background_color=bg_normal, on_press=self.onClick, font_size=27)
            b.id = i
            self.boxes.append(b)
            board.add_widget(b)
        return board
    def onClick(self, i):
        if self.isEnd:
            exit()
        if i.clickable:
            msg, self.game = self.first_gamer.playStep(self.game, pos=i.id)
            print(msg)
            self.updateBoard()
            self.controlEnd()
            if not self.isEnd:
                msg, self.game = self.second_gamer.playStep(self.game)
                print(msg)
                self.updateBoard()
                self.controlEnd()
            
    def updateBoard(self):
        for box in self.boxes:
            b = self.game.getBoard()[box.id]
            if b == '-':
                box.text = ""
                box.background_color = bg_normal
            elif b == self.first_gamer.getName():
                box.text = self.first_gamer.getName()
                box.background_color = bg_gamer
            elif b == self.second_gamer.getName():
                box.text = self.second_gamer.getName()
                box.background_color = bg_rival
    def controlEnd(self):
        if self.game.isWinned(gamer=self.first_gamer.getName()):
            print("{} qalibdir".format(self.first_gamer.getName()))
            self.isEnd = True
        elif self.game.isWinned(gamer=self.second_gamer.getName()):
            print("{} qalibdir".format(self.second_gamer.getName()))
            self.isEnd = True
        elif self.game.isBoardFilled():
            print("Hec-hece")
            self.isEnd = True
        

if __name__ == "__main__":
    TicTacToeApp().run()


    while True:
        if isEnd:
            break
        for g in gamers:
            if g.getType() == "HUMAN":
                b = game.getBoard()
                print_board(b)
                p = int(input("(1-9)>>>"))
                _, game = g.playStep(game=game, pos=(p-1))
            else:
                _, game = g.playStep(game=game)
            