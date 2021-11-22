from tictactoe import TicTacToe
from dummy import Dummy
from human import Human

game = TicTacToe(first='O')
dummy = Dummy(name='O')
human = Dummy(name='X')

def print_board(board):
    print("\n{} {} {}\n{} {} {}\n{} {} {}\n______\n".format(*board))

if __name__ == "__main__":
    for i in range(9):
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
        
        