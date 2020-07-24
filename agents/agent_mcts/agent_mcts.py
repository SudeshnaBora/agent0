import numpy as np
from agents.common import common as cn
import agents.agent_mcts.mcts_node as mcts_node
from typing import Optional
import time

PLAYER = cn.NO_PLAYER
OPPONENT = cn.NO_PLAYER
GLOBAL_TIME = 50


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
        node = node.select_next_node()
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
        node = node.expand_node(action)
    return node


def simulate_game(node: mcts_node.mcts_node) -> tuple:
    """
    Simulate the game of the current node
    :param node: The MCTS node
    :return: tuple containing details if a player has won the game during simulation
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


def back_propagation(node:mcts_node.mcts_node, current_player: np.int8, win: bool):
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
    # update each node in this tree expansion with the results
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
    root = mcts_node.mcts_node(state=board, player=PLAYER)

    global GLOBAL_TIME
    # defining the limiting factor to get out of the loop
    end = time.time() + GLOBAL_TIME
    while time.time() < end:

        # Start at the root node at each iteration
        node = root

        # Step 1: select_next_node - this selects a terminal node or an unexplored node
        node = select_node(node)

        # Step 2: Explore the node that is selected
        node = explore_node(node)

        # Step 3 : Simulation
        win_game_flag, current_player = simulate_game(node)

        # Step 4: Back propagation
        back_propagation(node, win_game_flag, current_player)

    max_score = - 10000000
    selected_column = - 1
    for child in root.children:
        if cn.connected_four(child.state, child.player):
            return child.move
        else:
            score = child.num_wins / child.total_visits
            if score > max_score:
                selected_column = child.move
                max_score = score
    return selected_column
