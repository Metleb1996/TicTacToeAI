from tictactoe import TicTacToe
from dummy import Dummy
from human import Human
from agent import Agent

game = TicTacToe(first='O')
dummy = Dummy(name='O')
human = Dummy(name='X')
agent = Agent(name="X")

def print_board(board):
    print("\n{} {} {}\n{} {} {}\n{} {} {}\n______\n".format(*board))

def train(count=1000000):
    agent.train(first='O', dum=dummy, count=count)
    agent.train(first='X', dum=dummy, count=count)

if __name__ == "__main__":
    train(count=1000)
    """for i in range(9):
        d, game = dummy.playStep(game=game); print(d)
        b = game.getBoard()
        print_board(b)
        p = int(input("(1-9)>>>"))
        h, game = human.playStep(game=game, pos=(p-1)); print(h)
        if game.isWinned(gamer="X"):
            print("X qalibdir")
            break
        if game.isWinned(gamer="O"):
            print("O qalibdir")
            break
        if game.isBoardFilled():
            print("Hec-hece")
            break
        """
    