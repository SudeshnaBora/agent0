from enum import Enum
import numpy as np

BoardPiece = np.int8  # The data type of the board
NO_PLAYER = BoardPiece(0)  # board[i, j] == NO_PLAYER where the position is empty
PLAYER1 = BoardPiece(1)  # board[i, j] == PLAYER1 where player 1 has a piece
PLAYER2 = BoardPiece(2)  # board[i, j] == PLAYER2 where player 2 has a piece

PlayerAction = np.int8  # The column to be played


class GameState(Enum):
    IS_WIN = 1
    IS_DRAW = -1
    STILL_PLAYING = 0


def initialize_game_state() -> np.ndarray:
    return np.zeros((6, 7), dtype=BoardPiece)


board = initialize_game_state()
board[0, 0] = 2


def pretty_print_board(input_board: np.ndarray) -> str:
    return '\n'.join([str(row) for row in input_board[::-1]])


def string_to_board(pp_board: str) -> np.ndarray:
    pass


def apply_player_action(d_board, action, player, copy=False) -> tuple:
    placed = False
    if copy:
        copied_board = d_board
    else:
        copied_board = np.zeros((6, 7), dtype=BoardPiece)

    for row in d_board:
        if row[action] == NO_PLAYER:
            d_board[row, action] = player
            placed = True
            break
    if not placed:
        raise Exception('Cannot place player in that particular position')

    return copied_board, d_board


def connected_four(d_board, player, last_action=None) -> bool:
    rows = d_board.shape[0]
    cols = d_board.shape[1]
    if not (last_action in np.arange(rows)):
        for i in range(rows):
            for j in range(cols):
                element = player
                # check row
                if j <= 3 and element == d_board[i, j + 1] and element == d_board[i, j + 2] and element == d_board[
                    i, j + 3]:
                    return True

                # check column
                if i <= 3 and element == d_board[i + 1, j] and element == d_board[i + 2, j] and element == d_board[
                    i + 3, j]:
                    return True

                # right diagonal
                if i <= 2 and j <= 3:
                    if element == d_board[i + 1, j + 1] and element == d_board[i + 2, j + 2] and element == d_board[
                    i + 3, j + 3]:
                        return True

                # left diagonal
                if i <= 2 and j >= 3:
                    if element == d_board[i + 1, j - 1] and element == d_board[i + 2, j - 2] and element == \
                    d_board[i + 3, j - 3]:
                        return True

                return False


def check_end_state(c4_board, player) -> GameState:
    if connected_four(c4_board, player):
        return GameState.IS_WIN
    elif check_board_full(c4_board):
        return GameState.IS_DRAW
    else:
        return GameState.STILL_PLAYING


def check_board_full(c4_board) -> bool:
    for row in range(6):
        for col in range(7):
            if c4_board[row, col] == 0:
                return False

    return True
