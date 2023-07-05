import time
import TicTacToe.computor_moves as computor_moves
import TicTacToe.xo_game_display_info as xo_game_display_info


def check_win(board):
    '''
    Checks if the is a winner in the current game state
    '''
    
    if board[1] == board[2] and board[2] == board[3] :
        return True
    elif board[4] == board[5] and board[5] == board[6]:
        return True
    elif board[7] == board[8] and board[8] == board[9] :
        return True
    elif board[1] == board[4] and board[4] == board[7] :
        return True
    elif board[2] == board[5] and board[5] == board[8] :
        return True
    elif board[3] == board[6] and board[6] == board[9] :
        return True
    elif board[1] == board[5] and board[5] == board[9] :
        return True
    elif board[3] == board[5] and board[5] == board[7] :
        return True


def check_draw(board):
    '''
    Checks if the are no other moves left to play
    '''   
    
    for moves in board:
        if board[moves] not in ["O", "X"]:
            return False
    return True


def deslay_the_XO_board(board):
    '''
    Creates the game grid or board and Desplays  the game state to the player
    '''
    
    print("\t\t+----+----+----+")
    
    for sqaure in board:
        
        if sqaure == 1 or sqaure == 4 or sqaure == 7:
            print(end="\t\t|")
            
        print(end= f" {board[sqaure]}  |")
        
        if sqaure == 3 or sqaure == 6 or sqaure == 9:
            print("\n\t\t+----+----+----+")


def update_game_board(board, sqaure, turns, choice):
    '''
    Updates the game board by the move made by the player in their turn
    '''
    
    if turns % 2 == choice[1]:
        board[sqaure] = "X"
    else:
        board[sqaure] = "O"

             
def find_the_game_state(board, turns, multiplayer):
    '''
    Finds out who is the winner in the current game state X or O
    Also it checks if it is a Draw
    '''  
    
    xo_game_display_info.clean_screen()
    deslay_the_XO_board(board) 
          
    if check_win(board):       
        if multiplayer[0]: 
            xo_game_display_info.multiplayer(turns, multiplayer[1])
        else: 
            xo_game_display_info.singleplayer(turns)
        
    elif check_draw(board): 
        print("Draw")
    else:
        return True
    
    return exit()

def get_sqaure_number(turns, board, multiplayer):
    
    if multiplayer and turns % 2 == multiplayer[1]:
        return computor_moves.generate_game_states(board)
    else:
        return xo_game_display_info.get_user_input(board)    
    
    
def play_tic_tac_toe():
    '''
    It allows the players to play the game
    It desplays the move that each player made in the game board
    '''
    
    turns, game_type, board = 0, xo_game_display_info.choose_game_type(),  { 

    1 : "1",  2 : "2", 3 : "3",
    4 : "4",  5 : "5", 6 : "6",
    7 : "7",  8 : "8", 9 : "9",
    }   
    
    while find_the_game_state(board, turns, game_type):
        
        time.sleep(.5)     
        turns += 1     
        sqaure = get_sqaure_number(turns, board, game_type)      
        update_game_board(board, sqaure, turns, game_type)
                 

if __name__ == "__main__":
    
    xo_game_display_info.clean_screen()
    xo_game_display_info.welcome_the_players()
    play_tic_tac_toe()