import random

# The board is represented as a list of cells
# 0 represents an empty cell, 1 represents 'X', and -1 represents 'O'
board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

# The is to select str(x or o) from the symbols list.. i.e the number would be used for the indexing
AI_PLAYER = 2
HUMAN_PLAYER = 1
# this is just used for indexing in the list below

# Function to print the board
def print_board(board):
    symbols = ['-', 'X', 'O']
    for i in range(0, 9, 3):     # any other number greater than 6 and <= 9 would work perfectly fine for the range
        row = [symbols[cell] for cell in board[i:i + 3]]  # try understanding the logic in the listcomp here
        print('|'.join(row))



# Function to check if a player has won
def check_winner(board, player):
    winning_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
                        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
                        [0, 4, 8], [2, 4, 6]]  # Diagonals
    for pattern in winning_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False


# Function to check if the game is over
def game_over(board):
    return check_winner(board, AI_PLAYER) or check_winner(board, HUMAN_PLAYER) or all(cell != 0 for cell in board)
# notice how it was implemented in the main game funtion 

# Function for the AI player to make a move using the minimax algorithm
def ai_move(board):
    # add an if statement here for random in a case where the ai player is the first player
    best_score = float('-inf')  
    best_move = None           # look for another number that can replace (-inf) above as the min possible score 
    for i in range(9):
        if board[i] == 0:
            board[i] = AI_PLAYER
            score = minimax(board, 0, False)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = AI_PLAYER
    # this just keeps iterating to get the best score

# The minimax function
def minimax(board, depth, is_maximizing):  
    # see how the depth varies   and  note is_maximixing is a boolean for turn handling
    scores = {
        AI_PLAYER: 1,
        HUMAN_PLAYER: -1,
        'DRAW': 0     # look for a better key to represent the draw  i.e change the 0 to 'draw'
    }

    if check_winner(board, AI_PLAYER):
        return scores[AI_PLAYER]
    elif check_winner(board, HUMAN_PLAYER):
        return scores[HUMAN_PLAYER]
    elif game_over(board):
        return scores['DRAW']

    if is_maximizing:
        best_score = float('-inf')  # this is just an initial minimum val that would change after the first iteration
        for i in range(9):
            if board[i] == 0:
                board[i] = AI_PLAYER
                score = minimax(board, depth + 1, False)
                board[i] = 0
                best_score = max(score, best_score)
        return best_score

    else:  # else here stands for minimizing case >> i.e if is_maximizing is set to false
        best_score = float('inf')
        for i in range(9):
            if board[i] == 0:
                board[i] = HUMAN_PLAYER
                score = minimax(board, depth + 1, True)
                board[i] = 0
                best_score = min(score, best_score)
        return best_score


# Function for the human player to make a move and catch any erros
def human_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == 0:
                board[move] = HUMAN_PLAYER
                break
            print('pls check that your input is bw (1-9) or space is already taking')
        else:
            print("Invalid move. Please enter a number.")


def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not game_over(board):
        if not any(cell == 0 for cell in board):
            print("It's a tie!")
            return

        print("your turn")
        human_move(board)
        # ai_move(board)
        print_board(board)

        if check_winner(board, HUMAN_PLAYER):
            print("player one wins !")
            return

        if not any(cell == 0 for cell in board):
            print("It's a tie!")
            return

        print("AI's turn")
        ai_move(board)
        # human_move(board)       # you can use this to try switching btw players
        print_board(board)

        if check_winner(board, AI_PLAYER):
            print("player2 wins!")
            return

    print("It's a tie!")


# Start the game
play_game()

# Todo: set x and o input based on player1 and player 2 later on instead of having static alphabeths
# make player turn dynamic 
