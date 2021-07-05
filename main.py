# Simple text-based TicTacToe game.
print("*********   Tic Tac Toe   ***********")

# Initialise variables
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
moves_played = []
game_over = False


def print_board():
    for row in board:
        line = ''
        for letter in row:
            line += letter + ' | '
        print(line[:-2])


def check_game_over():
    if len(moves_played) == 9:
        global game_over
        game_over = True
        print("It's a draw this time.")


def check_winner(player):
    # check for three in a row: rows then columns then diagonals
    if board[0][0] != ' ' and board[0][0] == board[0][1] == board[0][2] or \
            board[1][0] != ' ' and board[1][0] == board[1][1] == board[1][2] or \
            board[2][0] != ' ' and board[2][0] == board[2][1] == board[2][2] or \
            board[0][0] != ' ' and board[0][0] == board[1][0] == board[2][0] or \
            board[0][1] != ' ' and board[0][1] == board[1][1] == board[2][1] or \
            board[0][2] != ' ' and board[0][2] == board[1][2] == board[2][2] or \
            board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2] or \
            board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        print(f'{player} wins!')
        global game_over
        game_over = True


def update_board(player):
    check_game_over()
    move_made = False
    while not move_made:
        move = input(f'{player} to play: (1-9)\n')
        try:
            if move not in moves_played and isinstance(int(move), int):
                if move == '1':
                    board[2][0] = player
                if move == '2':
                    board[2][1] = player
                if move == '3':
                    board[2][2] = player
                if move == '4':
                    board[1][0] = player
                if move == '5':
                    board[1][1] = player
                if move == '6':
                    board[1][2] = player
                if move == '7':
                    board[0][0] = player
                if move == '8':
                    board[0][1] = player
                if move == '9':
                    board[0][2] = player
                moves_played.append(move)
                move_made = True
                check_winner(player)
            else:
                print('Move has already been played, please try again')
        except ValueError:
            print("Please only enter a number from 1-9")


while True:
    update_board('O')
    print_board()
    if game_over:
        break
    update_board('X')
    print_board()
    if game_over:
        break
