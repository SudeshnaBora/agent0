import agents.common.common as cm
import agents.agent_mcts.mcts_node as node
import agents.agent_mcts.agent_mcts as agent


def test_generate_move():
    board = cm.initialize_game_state()
    action, _ = agent.generate_move(board, cm.PLAYER1, {})
    assert type(action) == cm.PlayerAction


def test_generate_move_winning():
    """
    This test is to check if the winning action is returned by the algorithm
    :return:
    """
    agent.GLOBAL_TIME = 20
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER2
    board[0, 1] = cm.PLAYER2
    board[0, 2] = cm.PLAYER2
    action, _ = agent.generate_move(board, cm.PLAYER2, {})
    assert action == 3


def test_backpropagation():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board)
    agent.back_propagation(current_node, cm.PLAYER1, False)




