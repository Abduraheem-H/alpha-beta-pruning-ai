"""
Alpha–Beta Pruning Demonstration
Department of Computer Science
Introduction to Artificial Intelligence

This program implements Alpha–Beta Pruning for a simple Tic-Tac-Toe game.
It shows how the algorithm searches game states efficiently by pruning
branches that cannot influence the final Minimax decision.

Rules followed:
- Pure Python
- Recursive implementation
- Depth limit
- Clear evaluation logic
"""

import math

MAX_PLAYER = "X"
MIN_PLAYER = "O"

node_count = 0


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        print()
        for i in range(3):
            row = self.board[i * 3 : (i + 1) * 3]
            print(" | ".join(row))
            if i < 2:
                print("--+---+--")
        print()

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v == " "]

    def make_move(self, index, player):
        self.board[index] = player

    def undo_move(self, index):
        self.board[index] = " "

    def winner(self):
        win_states = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in win_states:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]

        if " " not in self.board:
            return "DRAW"

        return None


def evaluate(board: TicTacToe):
    winner = board.winner()

    if winner == MAX_PLAYER:
        return 1
    elif winner == MIN_PLAYER:
        return -1
    else:
        return 0


def alphabeta(board: TicTacToe, depth, alpha, beta, maximizing):
    global node_count
    node_count += 1

    result = board.winner()
    if depth == 0 or result is not None:
        return evaluate(board), None

    if maximizing:
        best_value = -math.inf
        best_move = None

        for move in board.available_moves():
            board.make_move(move, MAX_PLAYER)

            value, _ = alphabeta(board, depth - 1, alpha, beta, False)

            board.undo_move(move)

            if value > best_value:
                best_value = value
                best_move = move

            alpha = max(alpha, best_value)
            if alpha >= beta:
                break  # prune

        return best_value, best_move

    else:
        best_value = math.inf
        best_move = None

        for move in board.available_moves():
            board.make_move(move, MIN_PLAYER)

            value, _ = alphabeta(board, depth - 1, alpha, beta, True)

            board.undo_move(move)

            if value < best_value:
                best_value = value
                best_move = move

            beta = min(beta, best_value)
            if beta <= alpha:
                break

        return best_value, best_move


if __name__ == "__main__":
    game = TicTacToe()
    current_player = MAX_PLAYER

    print("Initial Board")
    game.print_board()

    while True:
        result = game.winner()
        if result is not None:
            if result == "DRAW":
                print("Game ended in a draw.")
            else:
                print(f"Winner: {result}")
            break

        node_count = 0

        if current_player == MAX_PLAYER:
            value, move = alphabeta(
                game, depth=9, alpha=-math.inf, beta=math.inf, maximizing=True
            )
            game.make_move(move, MAX_PLAYER)
            print(f"MAX (X) chooses move {move}")
        else:
            value, move = alphabeta(
                game, depth=9, alpha=-math.inf, beta=math.inf, maximizing=False
            )
            game.make_move(move, MIN_PLAYER)
            print(f"MIN (O) chooses move {move}")

        print(f"Nodes evaluated this turn: {node_count}")
        game.print_board()

        current_player = MIN_PLAYER if current_player == MAX_PLAYER else MAX_PLAYER
