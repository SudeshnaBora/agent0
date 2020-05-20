import numpy as np
import connectn.common as cn
import math
from typing import Optional

#was struggling with switching between agent and user input in players so introduced two variables

AGENT = cn.NO_PLAYER
HUMAN = cn.NO_PLAYER


def generate_move(board: np.ndarray, player: cn.BoardPiece, saved_state: Optional[cn.SavedState]):
    global AGENT
    global HUMAN
    print('HUMAN before setup {}'.format(HUMAN))

    #assuming that this will always get called by AGENT
    AGENT = player
    if AGENT == cn.PLAYER1:
        HUMAN = cn.PLAYER2
    else:
        HUMAN = cn.PLAYER1

    assert not HUMAN == cn.NO_PLAYER
    col, minimax_score = minimax(board, 3, -math.inf, math.inf, True)
    print('For col: {}, the score is {}'.format(col,minimax_score))
    return col, saved_state


def score_center(board, player):
    center_col = board[:, 3]
    count = list(center_col).count(player)
    return count * 4


def score_horizontal(board, player):
    score = 0
    current_player = player
    opposite_player = player
    if current_player == cn.PLAYER1:
        opposite_player = cn.PLAYER2
    for i in range(6):
        row = board[i, :]
        for col in range(4):
            current_slab = list(row[col:col + 4])
            count = current_slab.count(current_player)
            empty_count = current_slab.count(cn.NO_PLAYER)
            opponent_count = current_slab.count(opposite_player)
            if count == 4:
                score += 100
            if count == 3 and empty_count == 1:
                score += 5
            if count == 2 and empty_count == 1:
                count += 2
            if opponent_count == 3 and empty_count == 1:
                count -= 4
    return score


def score_vertical(board, player):
    score = 0
    opposite_player = player
    if player == cn.PLAYER1:
        opposite_player = cn.PLAYER2
    elif player == cn.PLAYER2:
        opposite_player = cn.PLAYER1
    for i in range(7):
        col = board[:, i]
        for j in range(3):
            current_slab = list(col[j:j + 4])
            count = current_slab.count(player)
            empty_count = current_slab.count(cn.NO_PLAYER)
            opponent_count = current_slab.count(opposite_player)
            if count == 4:
                score += 100
            if count == 3 and empty_count == 1:
                score += 5
            if count == 2 and empty_count == 1:
                count += 2
            if opponent_count == 3 and empty_count == 1:
                count -= 4
    return score


def score_positive_diagonal(board, player):
    score = 0
    opposite_player = player
    if player == cn.PLAYER1:
        opposite_player = cn.PLAYER2
    elif player == cn.PLAYER2:
        opposite_player = cn.PLAYER1
    for i in range(3):
        for j in range(4):
            for x in range(4):
                current_slab = [board[i + x][j + x] for x in range(4)]
            count = current_slab.count(player)
            empty_count = current_slab.count(cn.NO_PLAYER)
            opponent_count = current_slab.count(opposite_player)
            if count == 4:
                score += 100
            if count == 3 and empty_count == 1:
                score += 5
            if count == 2 and empty_count == 1:
                count += 2
            if opponent_count == 3 and empty_count == 1:
                count -= 4
    return score


def score_negative_diagonal(board, player):
    score = 0
    opposite_player = player
    if player == cn.PLAYER1:
        opposite_player = cn.PLAYER2
    elif player == cn.PLAYER2:
        opposite_player = cn.PLAYER1
    for i in range(3):
        for j in range(4):
            for x in range(4):
                current_slab = [board[i + 3 - x][j + x] for x in range(4)]
            count = current_slab.count(player)
            empty_count = current_slab.count(cn.NO_PLAYER)
            opponent_count = current_slab.count(opposite_player)
            if count == 4:
                score += 100
            if count == 3 and empty_count == 1:
                score += 5
            if count == 2 and empty_count == 1:
                count += 2
            if opponent_count == 3 and empty_count == 1:
                count -= 4
    return score


def heuristic_scoring(board, player):
    value = 0
    # It is considered that center placement is a very good starting , so I am giving different
    # calculation for center compared to other vertical check
    value += score_center(board, player)

    # check horizontal
    value += score_horizontal(board, player)

    # check vertical
    value += score_vertical(board, player)

    # check positive diagonal
    value += score_positive_diagonal(board, player)

    # check negative diagonal
    value += score_negative_diagonal(board, player)

    return value


def minimax(board, depth, alpha, beta, maximizing_player):

    # if depth is 0 or node is terminal, return heuristic value of the node
    if cn.connected_four(board, AGENT) == cn.GameState.IS_WIN:
        # This checks if the current state of the board is draw for any of the two players
        return None, 10000
    if cn.connected_four(board, HUMAN) == cn.GameState.IS_WIN:
        return None, -10000
    # Check if there is a draw
    if cn.connected_four(board, AGENT) == cn.GameState.IS_DRAW:
        return None, 0
    if depth == 0:
        return None, heuristic_scoring(board, AGENT)

    # get a list of columns open for placement
    col_list = cn.get_free_columns(board)
    if maximizing_player:
        value = -math.inf
        column = np.random.choice(col_list)
        for col in col_list:
            b_copy = board.copy()
            cn.apply_player_action(b_copy, col, AGENT)
            new_score = minimax(b_copy, depth - 1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        print("For col : {}, the score is {}: ".format(col, new_score))
        return column, value

    else:
        value = math.inf
        column = np.random.choice(col_list)
        for col in col_list:
            b_copy = board.copy()
            cn.apply_player_action(b_copy, col, HUMAN)
            new_score = minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
