from random import choice

board = {
    1: [" ", " ", " "],
    2: [" ", " ", " "],
    3: [" ", " ", " "],
}
cross = {
    "rl": [board[1][2], board[2][1], board[3][0]],
    "tb": [board[1][1], board[2][1], board[3][1]],
    "lr": [board[1][0], board[2][1], board[3][2]],
}
players = {1: "X", 2: "O"}
game_over = False


def display_board():
    print(
        f"""
    {board[1][0]} | {board[1][1]} | {board[1][2]}
    ---------
    {board[2][0]} | {board[2][1]} | {board[2][2]}
    ---------
    {board[3][0]} | {board[3][1]} | {board[3][2]}
"""
    )


def tiktactoe():
    for i in range(1, 4):
        if len(set(board[i])) == 1 and " " not in board[i]:
            return True

    for key in cross.keys():
        if len(set(cross[key])) == 1 and " " not in cross[key]:
            return True

    if all(" " not in board[cell] for cell in board):
        return "Draw"

    return False


def update_cross():
    new_cross = {
        "rl": [board[1][2], board[2][1], board[3][0]],
        "tb": [board[1][1], board[2][1], board[3][1]],
        "lr": [board[1][0], board[2][1], board[3][2]],
    }
    return new_cross


def switch_player(curr_player):
    return players[1] if curr_player == "O" else players[2]


def game(player):
    global cross
    display_board()

    row = int(input("Enter row (1, 2, 3): "))
    col = int(input("Enter column (1, 2, 3): ")) - 1

    if board[row][col] == " ":
        board[row][col] = player
        cross = update_cross()
    else:
        print("Cell already occupied. Try again.")
        return game(player)


first_time = True
first_player = (lambda: players[choice([1, 2])])()


while not game_over:
    if first_time:
        print("Welcome to Tic Tac Toe!")
        player = first_player
    else:
        player = switch_player(player)

    print(f"{player} Turn")

    first_time = False

    game(player)

    if tiktactoe() == True:
        display_board()
        print(f"TicTacToe!! {player} wins!")
        game_over = True
    elif tiktactoe() == "Draw":
        display_board()
        print("It's a draw!")
        game_over = True
