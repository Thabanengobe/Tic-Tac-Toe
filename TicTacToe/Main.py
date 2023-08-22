import re
import Game
import platform
from os import system
from MiniMaxAlgorythm import MiniMax

def insertMove(board):

    sqaure_to_play = input("Enter the number you want to play (q:to quit): ")

    if re.fullmatch("[1-9]", sqaure_to_play):
        
        if board[int(sqaure_to_play)] not in ["O", "X"]:
            return int(sqaure_to_play)
        else:
            print("Sqaure already played try a different square!!!")
            return insertMove(board)
            
    elif sqaure_to_play in ['q', 'Q']:
        exit()
    else:
        print("Invalid number!!!")
        return insertMove(board)
    
def goFirst():
    
    choose = input("Would you like  to go first? (y/n)\n->")
    return 1 if re.fullmatch('y|Y', choose) else 0

def clean_screen():
    
    system('cls') if platform.system().lower() == 'windows' else system('clear')

def startGame():

    board = {
        1:"1", 2:"2", 3:"3",
        4:"4", 5:"5", 6:"6",
        7:"7", 8:"8", 9:"9"
    }

    game = Game.game(board)
    cpu = MiniMax(game)
    turns = 1
    symbol = ""

    while turns < 10:
        
        clean_screen()

        game.showGameBoard()
        
        if turns % 2 == 0:
            move=insertMove(game.getBoard)
            symbol = "O"   
        else:
            move = cpu.generateGameState()
            symbol ="X"

        game.updateGameBoard(move,symbol)

        if game.isgameOver(symbol): break
        turns += 1

    clean_screen()
    game.showGameBoard()

if __name__ == "__main__":
    startGame()