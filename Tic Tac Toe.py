
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]) or \
           all(row[i] == player for row in board):
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    else:
        return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
        except ValueError:
            print("Invalid input.")
            continue

        if row not in range(3) or col not in range(3):
            print("Out of range.")
            continue

        if board[row][col] != " ":
            print("Cell already taken.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()