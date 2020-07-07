import agents.agent_minimax.agent_minimax as agent
from agents.common import common as cm
import numpy as np


def test_score_row():
    board = cm.initialize_game_state()
    board[0, 3] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 1] = cm.PLAYER2
    assert 4 == agent.score_row(board, cm.PLAYER1)


def test_score_column():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 0] = cm.PLAYER1
    board[3, 0] = cm.PLAYER2
    assert 2 == agent.score_column(board, cm.PLAYER1)


def test_score_right_diagonal():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 1] = cm.PLAYER1
    board[3, 3] = cm.PLAYER2
    assert 2 == agent.score_right_diagonal(board, cm.PLAYER1)


def test_score_left_diagonal():
    board = cm.initialize_game_state()
    board[0, 6] = cm.PLAYER1
    board[1, 5] = cm.PLAYER1
    board[3, 3] = cm.PLAYER2
    assert 2 == agent.score_left_diagonal(board, cm.PLAYER1)


def test_heuristic_scoring():
    board = cm.initialize_game_state()
    board[0, 3] = cm.PLAYER1
    board[1, 3] = cm.PLAYER2
    assert 0 == agent.heuristic_scoring(board, cm.PLAYER1)


def test_minimax():
    board = cm.initialize_game_state()
    print(agent.minimax(board, 3, -100000000, 100000000, cm.PLAYER1))


# leveraging the fact that the initial move will be center column
def test_generate_move():
    board = cm.initialize_game_state()
    col, state = agent.generate_move(board, cm.PLAYER1, {})
    assert 3 == col


# to check the criteria when agent and human interchange
def test_generate_move_player_toggled():
    board = cm.initialize_game_state()
    col, state = agent.generate_move(board, cm.PLAYER2, {})
    assert 3 == col


def test_minimax_win():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[0, 1] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER1
    agent.HUMAN = cm.PLAYER2
    col, score = agent.minimax(board, 0, -100000000, 100000000, True)
    assert None == col
    assert 10000 == score


def test_minimax_loss():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[0, 1] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    col, score = agent.minimax(board, 0, -100000000, 100000000, True)
    assert None == col
    assert -10000 == score


def test_minimax_draw():
    board = 5 * np.ones((6, 7), dtype=cm.BoardPiece)
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    col, score = agent.minimax(board, 0, -100000000, 100000000, True)
    assert None == col
    assert 0 == score


def test_score_left_diagonal_full():
    board = cm.initialize_game_state()
    board[0, 6] = cm.PLAYER1
    board[1, 5] = cm.PLAYER1
    board[2, 4] = cm.PLAYER1
    board[3, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER1
    agent.HUMAN = cm.PLAYER2
    score = agent.score_left_diagonal(board, cm.PLAYER1)
    assert score == 105


def test_score_left_diagonal_opponent():
    board = cm.initialize_game_state()
    board[0, 6] = cm.PLAYER1
    board[1, 5] = cm.PLAYER1
    board[2, 4] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    score = agent.score_left_diagonal(board, cm.PLAYER2)
    assert score == -4


def test_score_column_full():
    board = cm.initialize_game_state()
    board[0, 6] = cm.PLAYER1
    board[1, 6] = cm.PLAYER1
    board[2, 6] = cm.PLAYER1
    board[3, 6] = cm.PLAYER1
    agent.AGENT = cm.PLAYER1
    agent.HUMAN = cm.PLAYER2
    score = agent.score_column(board, cm.PLAYER1)
    assert score == 105


def test_score_column_opponent():
    board = cm.initialize_game_state()
    board[0, 6] = cm.PLAYER1
    board[1, 6] = cm.PLAYER1
    board[2, 6] = cm.PLAYER1
    board[3, 6] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    score = agent.score_column(board, cm.PLAYER2)
    assert score == -104


def test_score_right_diagonal_full():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 1] = cm.PLAYER1
    board[2, 2] = cm.PLAYER1
    board[3, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER1
    agent.HUMAN = cm.PLAYER2
    score = agent.score_right_diagonal(board, cm.PLAYER1)
    assert score == 105


def test_score_right_diagonal_opponent():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 1] = cm.PLAYER1
    board[2, 2] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    score = agent.score_right_diagonal(board, cm.PLAYER2)
    assert score == -4


def test_score_row_full():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[0, 1] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER1
    agent.HUMAN = cm.PLAYER2
    score = agent.score_row(board, cm.PLAYER1)
    assert score == 105


def test_score_row_opponent():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[0, 1] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    score = agent.score_row(board, cm.PLAYER2)
    assert score == -4


def test_score_left_diagonal_opponent_full():
    board = cm.initialize_game_state()
    board[0, 6] = cm.PLAYER1
    board[1, 5] = cm.PLAYER1
    board[2, 4] = cm.PLAYER1
    board[3, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    score = agent.score_left_diagonal(board, cm.PLAYER2)
    assert score == -104


def test_score_row_opponent_full():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[0, 1] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    score = agent.score_row(board, cm.PLAYER2)
    assert score == -104


def test_score_right_diagonal_opponent_full():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 1] = cm.PLAYER1
    board[2, 2] = cm.PLAYER1
    board[3, 3] = cm.PLAYER1
    agent.AGENT = cm.PLAYER2
    agent.HUMAN = cm.PLAYER1
    score = agent.score_right_diagonal(board, cm.PLAYER2)
    assert score == -104
