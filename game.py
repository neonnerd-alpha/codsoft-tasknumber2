EMPTY = ' '
AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'
def initialize_board():
    return [EMPTY] * 9
def print_board(board):
    for i in range(3):
        print(' | '.join(board[i * 3:i * 3 + 3]))
        if i < 2:
            print('---------')
def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]
def check_winner(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        return True
    return False
import math

def evaluate_board(board):
    if check_winner(board, AI_PLAYER):
        return 1
    elif check_winner(board, HUMAN_PLAYER):
        return -1
    else:
        return 0

def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate_board(board)
    
    # Base cases
    if score == 1 or score == -1:
        return score
    if len(available_moves(board)) == 0:
        return 0
    
    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move] = AI_PLAYER
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move] = HUMAN_PLAYER
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
def get_best_move(board):
    best_move = -1
    best_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for move in available_moves(board):
        board[move] = AI_PLAYER
        eval = minimax(board, 0, alpha, beta, False)
        board[move] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move in available_moves(board):
                board[move] = HUMAN_PLAYER
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number (1-9).")

def play_game():
    board = initialize_board()
    print_board(board)
    
    while True:
        human_move(board)
        print_board(board)
        if check_winner(board, HUMAN_PLAYER):
            print("Congratulations! You won!")
            break
        if len(available_moves(board)) == 0:
            print("It's a tie!")
            break
        
      
        print("AI is thinking...")
        ai_move = get_best_move(board)
        board[ai_move] = AI_PLAYER
        print(f"AI chose move {ai_move + 1}")
        print_board(board)
        if check_winner(board, AI_PLAYER):
            print("AI wins! Better luck next time.")
            break
        if len(available_moves(board)) == 0:
            print("It's a tie!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
