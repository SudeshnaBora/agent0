from unittest.mock import patch

import agents.common.common as cm
import agents.agent_mcts.mcts_node as node
import agents.agent_mcts.agent_mcts as agent


def test_generate_move():
    board = cm.initialize_game_state()
    action, _ = agent.generate_move(board, cm.PLAYER1, {})
    assert type(action) == cm.PlayerAction


@patch('agents.agent_mcts.agent_mcts.GLOBAL_TIME', 30)
def test_generate_move_winning():
    """
    This test is to check if the winning action is returned by the algorithm
    :return:
    """
    board = cm.initialize_game_state()
    board[0, 0] = agent.PLAYER
    board[0, 1] = agent.PLAYER
    board[0, 2] = agent.PLAYER
    action, _ = agent.generate_move(board, cm.PLAYER2, {})
    assert type(action) == cm.PlayerAction


def test_back_propagation():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board)
    agent.back_propagation(current_node, cm.PLAYER1, False)
    assert current_node.total_visits == 1


def test_select_node():
    board = cm.initialize_game_state()
    child_board = cm.initialize_game_state()
    child_board[0, 0] = cm.PLAYER1
    current_node = node.mcts_node(state=board)
    child_node = node.mcts_node(state=child_board, parent=current_node)
    current_node.open_moves = [0, 3, 4]
    current_node.children = [child_node]
    selected_node = agent.select_node(current_node)
    # since it has unexpanded node, hence it will return the current node
    assert selected_node == current_node


def test_explore_node():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board)
    current_node.open_moves = [0, 3, 4]
    explored_node = agent.explore_node(current_node)
    # explore a new open node
    assert len(current_node.open_moves) == 2
    assert explored_node != current_node


def test_simulate_game():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board, player=cm.PLAYER1)
    win, player = agent.simulate_game(current_node)
    # simulated till a win is encountered
    assert win







