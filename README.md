# Tic-Tac-Toe
🎮 Tic Tac Toe Game (X-O)
📌 Game Idea:
A classic 2-player game where each player takes turns placing their symbol ("X" or "O") on a 3×3 board, trying to form a row of three matching symbols horizontally, vertically, or diagonally.

🧠 How to Play:
The game is played on a 3x3 grid.

Players take turns entering two numbers: the row and column (from 0 to 2).

If the selected cell is already occupied or the input is invalid → the player is asked to enter again.

🎯 Game End Conditions:
A player gets 3 symbols in a row → Win.

The board is full with no winner → Draw.

🧩 Function Descriptions:
Function	Purpose
print_board(board)	Displays the current board in a nice format
check_winner(board, player)	Checks if the current player has won
is_full(board)	Checks if all cells are filled (draw)
play_game()	Runs the full game loop: input, turn-switching, and win/draw check

✅ Game Features:
Turn-based play between two players (X and O).

Automatic win and draw detection.

Clear error messages for invalid or duplicate moves.

Easy to expand (e.g., add AI in the future).
