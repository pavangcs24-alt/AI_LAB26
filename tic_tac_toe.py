board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()


def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


def is_draw():
    return " " not in board


def minimax(is_maximizing):
    # Computer wins
    if check_winner("O"):
        return 1

    # Human wins
    if check_winner("X"):
        return -1

    # Draw
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move():
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def player_move():
    while True:
        try:
            position = int(input("Choose a position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number from 1 to 9.")
                continue

            index = position - 1

            if board[index] != " ":
                print("That position is already taken.")
                continue

            board[index] = "X"
            break

        except ValueError:
            print("Please enter a valid number.")


def play_game():
    print("================================")
    print("     TIC-TAC-TOE: YOU vs AI")
    print("================================")
    print()
    print("You are X.")
    print("Computer is O.")
    print()
    print("Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    while True:

        # Player's turn
        print("\nYour turn!")
        player_move()

        if check_winner("X"):
            print_board()
            print("🎉 Congratulations! You win!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        # Computer's turn
        print("\nComputer is thinking...")
        computer_move()

        if check_winner("O"):
            print_board()
            print("🤖 The computer wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        print_board()


play_game()