import re
import Game
import platform
import time
from os import system
from MiniMaxAlgorythm import MiniMax

def insertMove(board:dict):

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
            move = insertMove(game.getBoard)  
            symbol = "O"   
        else:
            symbol ="X"
            move = cpu.generateGameState()
           

        game.updateGameBoard(move,symbol)
        gameState = game.isgameOver(symbol)

        if gameState != None:
            clean_screen()
            game.showGameBoard()
            print(gameState)
            break

        turns += 1
   

if __name__ == "__main__":
    startGame()