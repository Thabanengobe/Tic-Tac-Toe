import re
import platform
from os import system

def welcome_the_players():
    
    print('*' * 50,'\n','Welcome to  the Tic Tac Toe game\n'.upper())
    print("what would you like to play today\n")
    
    
def choose_game_type():
    
    game_type = input("1: Single player\n2: Multiplayer\n-> ")
    
    if re.match('[1-2]', game_type):
        if game_type == '1':
            return True, who_goes_first()
        return False, ''
    
    else:      
        return  print("Invalid choice\n"), choose_game_type()
    

def who_goes_first():
    
    choose = input("Would you like  to go first? (y/n)\n->")
    
    if re.fullmatch('y|n', choose):
        if choose == 'y':
            return 0
        return 1
    
    return print('Invalid choice try again'), who_goes_first()


def get_user_input(board):
    '''
    gets the players input and validates the move they made
    it check if the move is valid and that it has not been played
    '''
 
    sqaure_to_play = input("Enter the number you want to play (q:to quit): ")
    
    if re.fullmatch("[1-9]", sqaure_to_play):
        
        if board[int(sqaure_to_play)] not in ["O", "X"]:
            return int(sqaure_to_play)
        else:
            print("Number already played try a different number!!!!")
            return get_user_input(board)
            
    elif sqaure_to_play in ['q', 'Q']:
        return exit()
    else:
        print("Invalid number!!!")
        return get_user_input(board)
  
    
def multiplayer(turns, choice):
    
    if turns % 2 == choice:
        print("The computer wins")
    else:
        print("you win") 
    

def singleplayer(turns):
    
    if turns % 2 == 1:
        print("O wins")
    else:
        print("X wins")


def clean_screen():
    
    if platform.system().lower() == 'windows':
        system('cls')
    else:
        system('clear')
