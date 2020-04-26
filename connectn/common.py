from enum import Enum
from typing import Optional
import numpy as np

BoardPiece = np.int8  # The data type (dtype) of the board
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
    return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in input_board[::-1]])


def string_to_board(pp_board: str) -> np.ndarray:
    pass


def apply_player_action(board: np.ndarray, action: PlayerAction, player: BoardPiece, copy: bool = False) -> np.ndarray:
    pass


def connected_four(board: np.ndarray, player: BoardPiece, last_action: Optional[PlayerAction] = None) -> bool:
    pass
