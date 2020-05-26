import agents.agent_minimax as agent
import connectn.common as cm
import math


def test_score_center():
    board = cm.initialize_game_state()
    board[0, 3] = cm.PLAYER1
    assert 4 == agent.score_center(board, cm.PLAYER1)


def test_score_horizontal():
    board = cm.initialize_game_state()
    board[0, 3] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 1] = cm.PLAYER2
    assert 4 == agent.score_horizontal(board, cm.PLAYER1)


def test_score_vertical():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 0] = cm.PLAYER1
    board[3, 0] = cm.PLAYER2
    assert 2 == agent.score_vertical(board, cm.PLAYER1)


def test_score_right_diagonal():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[1, 1] = cm.PLAYER1
    board[3, 3] = cm.PLAYER2
    assert 2 == agent.score_positive_diagonal(board, cm.PLAYER1)


def test_score_left_diagonal():
    board = cm.initialize_game_state()
    board[0, 6] = cm.PLAYER1
    board[1, 5] = cm.PLAYER1
    board[3, 3] = cm.PLAYER2
    assert 2 == agent.score_negative_diagonal(board, cm.PLAYER1)


def test_heuristic_scoring():
    board = cm.initialize_game_state()
    board[0, 3] = cm.PLAYER1
    board[1, 3] = cm.PLAYER2
    assert 4 == agent.heuristic_scoring(board, cm.PLAYER1)


def test_minimax():
    board = cm.initialize_game_state()
    print(agent.minimax(board, 3, -math.inf, math.inf, cm.PLAYER1))
