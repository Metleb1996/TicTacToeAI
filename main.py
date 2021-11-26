from tictactoe import TicTacToe
from dummy import Dummy
from human import Human
from agent import Agent

#game = TicTacToe(first='O')
#dummy = Dummy(name='O')
#human = Human(name='X')
#agent = Agent(name="X", baseName="l1.tictactoe")
#agent2 = Agent(name="O", baseName="l2.tictactoe")

def print_board(board):
    print("\n{} {} {}\n{} {} {}\n{} {} {}\n______\n".format(*board))

def train(inagent,  inrival, count=1000000):
    inagent.train(first='O', rival=inrival, count=count)
    inagent.train(first='X', rival=inrival, count=count)

def play(first_gamer, second_gamer):
    game = TicTacToe(first=first_gamer.getName())
    isEnd = False
    gamers = [first_gamer, second_gamer]
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
            if game.isWinned(gamer="X"):
                print("X qalibdir")
                isEnd = True
            elif game.isWinned(gamer="O"):
                print("O qalibdir")
                isEnd = True
            elif game.isBoardFilled():
                print("Hec-hece")
                isEnd = True
            if isEnd:
                b = game.getBoard()
                print_board(b)
                break

if __name__ == "__main__":
    #train(inagent=agent2, inrival=agent, count=100000)
    play(first_gamer=Human(name="X"), second_gamer=Agent(name="O"))
    