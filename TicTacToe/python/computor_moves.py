

def find_win(board, symbol):
    
    if board[1] == board[2] and board[2] == board[3] and board[3] == symbol:
        return True
    elif board[4] == board[5] and board[5] == board[6] and board[6] == symbol:
        return True
    elif board[7] == board[8] and board[8] == board[9] and board[9] == symbol:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[7] == symbol:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[8] == symbol:
        return True
    elif board[3] == board[6] and board[6] == board[9] and board[9] == symbol:
        return True
    elif board[1] == board[5] and board[5] == board[9] and board[9] == symbol:
        return True
    elif board[7] == board[5] and board[5] == board[3] and board[3] == symbol:
        return True
    else:
        return False


def find_draw(board):
    
    for i in board:
        if board[i] not in ["O", "X"]:
            return False
    return True


def generate_game_states(board_state):
    
    min_score = -20
    bestMove = 0
    for move in board_state:
        
        if board_state[move] not in ['O', 'X']:
            board_state[move] = 'X'
            max_score = play_generated_game_state(board_state,False)
            board_state[move] = str(move)
            
            if (max_score > min_score):
                min_score = max_score
                bestMove = move
 
    return bestMove

def play_generated_game_state(board_state,pc_plays):
    
    if find_win(board_state, 'X'):
        return 10
    elif find_win(board_state, 'O'):
        return -10
    elif find_draw(board_state):
        return 0
    
    if pc_plays:
        bestScore = -20
        
        for i in board_state:
            if board_state[i] not in ['O', 'X']:
                board_state[i] = 'X'
                score = play_generated_game_state(board_state, False)
                board_state[i] = str(i)
                if (score > bestScore):
                    bestScore = score
                    
        return bestScore
    else:
        bestScore = 20
        for i in board_state:
            if board_state[i] not in ['O', 'X']:
                board_state[i] = 'O'
                score = play_generated_game_state(board_state, True)
                board_state[i] = str(i)
                if (score < bestScore):
                    bestScore = score
        return bestScore

