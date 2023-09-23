# Tic-Tac-Toe Game with Min-Max AI

This is a command-line-based Tic-Tac-Toe game implemented in Python, featuring an AI opponent that uses the Min-Max algorithm to make intelligent moves. The game allows two players to take turns, with one player being the human and the other being the AI.

## Installation

There are no special dependencies required to run this game. You just need Python 3.x installed on your computer.

## Usage

1. Clone the repository or download the project files to your local machine.

2. Open a terminal or command prompt.

3. Navigate to the project directory using the `cd` command.

4. Run the game by executing the following command: pyhon3 Main.py


5. Follow the on-screen instructions to play the game.

## Gameplay

- The game starts with an empty 3x3 grid.

- Player 1 (Human) is "X", and Player 2 (AI) is "O".

- Players take turns to make their moves by entering the row and column where they want to place their symbol.

- The game will display the current state of the board after each move.

- The AI uses the Min-Max algorithm to calculate its moves and make the best possible move.

- The game ends when one player wins, there is a draw, or a player quits the game.

## AI (Min-Max Algorithm)

The AI player uses the Min-Max algorithm to evaluate the best possible moves. This algorithm explores all possible future moves and selects the one that minimizes the maximum possible gain for the opponent (hence, the name Min-Max). The AI makes its moves based on this evaluation, aiming to win the game or prevent the opponent from winning.

## Rules

- To win the game, a player must have three of their symbols (X or O) in a row, column, or diagonal.

- The game ends in a draw if all cells are filled, and no player has won.

## Contributing

Contributions are welcome! If you want to improve the game or fix any issues, please fork this repository, make your changes, and submit a pull request.

## Acknowledgments

This game was created as a learning exercise in Python and AI programming. Special thanks to the open-source community for valuable resources and inspiration.

Have fun playing Tic-Tac-Toe with the Min-Max AI!
