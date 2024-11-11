# 3x3 Tic Tac Toe board
board = [[""] * 3 for _ in range(3)]

# Display the board
def print_board():
    for row in board:
        print(" | ".join(cell or " " for cell in row))
        print("-" * 9)

# Check if a player wins
def check_winner(player):
    return any(
        all(cell == player for cell in line) for line in [
            [board[0][0], board[0][1], board[0][2]],  # Rows
            [board[1][0], board[1][1], board[1][2]],
            [board[2][0], board[2][1], board[2][2]],
            [board[0][0], board[1][0], board[2][0]],  # Columns
            [board[0][1], board[1][1], board[2][1]],
            [board[0][2], board[1][2], board[2][2]],
            [board[0][0], board[1][1], board[2][2]],  # Diagonals
            [board[0][2], board[1][1], board[2][0]]
        ]
    )

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"): return 1
    if check_winner("X"): return -1
    if all(cell for row in board for cell in row): return 0  # Draw

    scores = []
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                board[i][j] = "O" if is_maximizing else "X"
                scores.append(minimax(not is_maximizing))
                board[i][j] = ""  # Undo move

    return max(scores) if is_maximizing else min(scores)

# Find AI's best move
def best_move():
    move, best_score = None, -float("inf")
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                board[i][j] = "O"
                score = minimax(False)
                board[i][j] = ""
                if score > best_score:
                    best_score, move = score, (i, j)
    return move

# Main game loop
def play_game():
    print("You are X, AI is O")
    while True:
        print_board()
        row, col = map(int, input("Enter row and column (0-2): ").split())
        if board[row][col]: print("Cell taken!"); continue
        board[row][col] = "X"

        if check_winner("X"):
            print_board(); print("You win!"); break
        if all(cell for row in board for cell in row):
            print_board(); print("It's a draw!"); break

        ai_move = best_move()
        if ai_move: board[ai_move[0]][ai_move[1]] = "O"

        if check_winner("O"):
            print_board(); print("AI wins!"); break
        if all(cell for row in board for cell in row):
            print_board(); print("It's a draw!"); break

# Start the game
play_game()
