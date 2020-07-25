from unittest.mock import patch

import agents.common.common as cm
import agents.agent_mcts.mcts_node as node
import agents.agent_mcts.agent_mcts as agent


def test_generate_move():
    board = cm.initialize_game_state()
    action, _ = agent.generate_move(board, cm.PLAYER1, {})
    assert type(action) == cm.PlayerAction


@patch('agents.agent_mcts.agent_mcts.PLAYER', cm.PLAYER2)
@patch('agents.agent_mcts.agent_mcts.OPPONENT', cm.PLAYER1)
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
    action = agent.MCTS(board)
    print(action)


def test_back_propagation():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board)
    agent.back_propagation(current_node, cm.PLAYER1, False)
    assert current_node.total_visits == 1




