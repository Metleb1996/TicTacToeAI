from kivy.app import App
from kivy.uix.gridlayout import  GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from tictactoe import TicTacToe
from human import Human
from agent import Agent

Window.size = (400, 400)

bg_normal = '31419F'
bg_gamer = '5BAF51'
bg_rival = 'AE3557'

class Box(Button):
    id = None

class TicTacToeApp(App):
    boxes = []
    def build(self):
        self.human = Human(name='X')
        self.agent = Agent(name='O')
        self.game = TicTacToe(first=self.human.getName())
        self.isEnd = False
        self.base = self.agent.base
        board = GridLayout(cols=3)
        for i in range(9):
            b = Box(text=' ', background_color=bg_normal, on_press=self.onClick, font_size=27)
            b.id = i
            self.boxes.append(b)
            board.add_widget(b)
        self.root = board
        return board

    def onClick(self, i):
        if self.isEnd:
            exit()
        if not i.disabled:
            msg, self.game = self.human.playStep(self.game, pos=i.id)
            print(msg)
            self.updateBoard()
            self.controlEnd()
            if not self.isEnd:
                msg, self.game = self.agent.playStep(self.game)
                print(msg)
                self.updateBoard()
                self.controlEnd()
            
    def updateBoard(self):
        for box in self.boxes:
            b = self.game.getBoard()[box.id]
            if b == '-':
                box.text = ""
                box.background_color = bg_normal
                box.disabled = False
            elif b == self.human.getName():
                box.text = self.human.getName()
                box.background_color = bg_gamer
                box.disabled = True
            elif b == self.agent.getName():
                box.text = self.agent.getName()
                box.background_color = bg_rival
                box.disabled = True
    def controlEnd(self):
        msg = ''
        if self.game.isWinned(gamer=self.human.getName()):
            msg = "{} qalibdir".format(self.human.getName())
            self.isEnd = True
        elif self.game.isWinned(gamer=self.agent.getName()):
            msg = "{} qalibdir".format(self.agent.getName())
            self.isEnd = True
        elif self.game.isBoardFilled():
            msg = "The game is tied."
            self.isEnd = True
        if self.isEnd:
            popup = Popup(title='Game Over',
                content=Label(text=msg, font_size=29),
                size_hint=(None, None), size=(200, 200))
            popup.bind(on_dismiss=self.onClick)
            popup.open()
        

if __name__ == "__main__":
    TicTacToeApp().run()

            