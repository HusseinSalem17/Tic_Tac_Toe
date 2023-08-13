import random


def setup_game():
    return [[" "] * 3 for _ in range(3)]


class WrongIndex(Exception):
    pass


def print_board(board):
    for i in board:
        print("|".join(i))


def move(board, player):
    while True:
        try:
            row = int(input("Enter row index (1 => 3): ")) - 1
            col = int(input("Enter column index (1 => 3): ")) - 1
            if (row > 2 or row < 0) or (col > 2 or col < 0):
                raise WrongIndex
            else:
                if board[row][col] == " ":
                    board[row][col] = player
                    break
                else:
                    print("Invalid move. Try again.")
        except WrongIndex:
            print("Wrong index, Please try again with these index (1 => 3)")
        except:
            print("their is error, please try again")


def check_win(board, player):
    # Check rows
    for row in board:
        if all(square == player for square in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == player) or (
        board[0][2] == board[1][1] == board[2][0] == player
    ):
        return True

    return False


def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True


def check_repeat():
    repeat = input("Want to play again? (y/n):")
    if repeat == "y" or repeat == "Y":
        return True
    else:
        return False


def game():
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)
    res = False
    while True:
        print_board(board)
        print("Your Turn", current_player)
        move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print("Player ", current_player, " have won ✨👏")
            res = True
        if check_tie(board):
            print_board(board)
            print("Tie!")
            res = True

        if res:
            res = False
            if not check_repeat():
                return
            else:
                board = setup_game()

        # change player
        current_player = players[1] if current_player == players[0] else players[0]


# Start playing
game()
