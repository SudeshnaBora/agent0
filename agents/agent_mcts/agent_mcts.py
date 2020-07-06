import numpy as np
from agents.common import common as cn
import agents.agent_mcts.mcts_node as mcts_node
from typing import Optional
import time

PLAYER = cn.NO_PLAYER
OPPONENT = cn.NO_PLAYER
GLOBAL_TIME = 5


def generate_move(board: np.ndarray, player: cn.BoardPiece, saved_state: Optional[cn.SavedState]) \
        -> object:
    """
    Generate move function for the mcts agent

    :parameter board: the playing board of type np.ndarray
    :parameter player: the player making the move
    :parameter saved_state : Optional parameter to use the SavedState

    :return: a tuple containing column number and \
     maximizing score for next move
    """
    global PLAYER
    global OPPONENT

    # assuming that this will always get called by PLAYER
    PLAYER = player
    if PLAYER == cn.PLAYER1:
        OPPONENT = cn.PLAYER2
    else:
        OPPONENT = cn.PLAYER1

    action = MCTS(board)
    return cn.PlayerAction(action), cn.SavedState()


def select_node(node: mcts_node.mcts_node) -> mcts_node.mcts_node:
    """
    Selects the node for exploration
    :param node: The MCTS node structure to expand
    :return: The selected node which is either a leaf node or an unexpanded node
    """
    # This will go down the tree till a leaf node or an unexpanded node is found
    while not np.any(node.open_moves) and node.children != []:
        node = node.selection()
    return node


def explore_node(node: mcts_node.mcts_node) -> mcts_node.mcts_node:
    """
    This is the second stage of MCTS algorithm. Here we will explore the\
    node thus selected.
    :param node: The node to be explored
    :return: The node which is not yet explored
    """
    if np.any(node.open_moves):
        # Choose a random action from available moves
        action = np.random.choice(node.open_moves)
        node = node.expansion(action)
    return node


def simulate_game(node: mcts_node.mcts_node) -> tuple:
    """
    Simulate the game of the current node
    :param node: The MCTS node
    :return:
    """
    board = node.state.copy()
    win = False
    current_player = node.player
    while np.any(cn.get_free_columns(board)) and not win:
        if current_player == cn.PLAYER2:
            current_player = cn.PLAYER1
        else:
            current_player = cn.PLAYER2
        # Choose a random action
        action = np.random.choice(cn.get_free_columns(board))
        # Apply the action
        board,_ = cn.apply_player_action(board, action, current_player)
        # Check if the game is won
        win = cn.connected_four(board, current_player)

    return win, current_player


def backpropagation(node:mcts_node.mcts_node, current_player: np.int8, win: bool):
    """

    :param node: The MCTS node
    :param current_player: The current player that made the node
    :param win: The flag signifying if this player has won
    """
    if win:
        if current_player == PLAYER:
            result = 1  # The player won
        else:
            result = -1  # The player lost against the opponent
    else:
        result = 0  # Game ended in a draw
    # Go up the tree until reaching the root node and update the visits and wins property of
    # each node on the way using the result
    while node is not None:
        node.set_visit_and_win(result)
        node = node.parent


def MCTS(board: np.ndarray) -> cn.PlayerAction:
    """
    The monte carlo tree search algorithm
    :param board: The board against which to calculate the simulation
    :return: Column in which player wants to make his move (chosen using MCTS)
    """
    # initialise root node to start the algorithm
    root_node = mcts_node.mcts_node(state=board, player=PLAYER)

    # set a limit to MCTS simulation
    global GLOBAL_TIME
    end_time = time.time() + GLOBAL_TIME
    while time.time() < end_time:

        # Start at the root node at each iteration
        node = root_node

        # Step 1: selection - this selects a terminal node or an unexplored node
        node = select_node(node)

        # Step 2: Explore the node that is selected
        node = explore_node(node)

        # Step 3 : Simulation
        win, current_player = simulate_game(node)

        # Step 4: Back propagation
        backpropagation(node, win, current_player)

    best_score = -np.infty
    for child in root_node.children:
        # Check if one child is a win --> If so return the action (make sure that the agent takes the
        # immediate win possibility)
        if cn.connected_four(child.state, child.player):
            return child.move
        # If no child is a win, compute the win/visit ratio and return the action of the child with the
        # highest ratio
        else:
            score = child.num_wins / child.total_visits
            if score > best_score:
                best_action = child.move
                best_score = score
    return best_action
