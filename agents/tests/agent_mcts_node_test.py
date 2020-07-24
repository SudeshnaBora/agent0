import agents.agent_mcts.mcts_node as node
from agents.common import common as cm


def test_get_open_moves():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board, player=cm.PLAYER1)
    assert current_node.get_open_moves().shape[0] == 7


def test_get_open_moves_connected4():
    board = cm.initialize_game_state()
    board[0, 0] = cm.PLAYER1
    board[0, 1] = cm.PLAYER1
    board[0, 2] = cm.PLAYER1
    board[0, 3] = cm.PLAYER1
    current_node = node.mcts_node(state=board, player=cm.PLAYER1)
    assert current_node.get_open_moves().shape[0] == 0


def test_set_visit_win():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board, player=cm.PLAYER1)
    current_node.set_visit_and_win(result=10)
    assert current_node.num_wins == 10
    assert current_node.total_visits == 1


def test_child_selection():
    board = cm.initialize_game_state()
    child_board01 = board.copy()
    child_board01[0, 0] = cm.PLAYER1
    child_board02 = board.copy()
    child_board02[0, 3] = cm.PLAYER1
    child_node01 = node.mcts_node(state=child_board01, player=cm.PLAYER1)
    child_node02 = node.mcts_node(state=child_board02, player=cm.PLAYER1)
    current_node = node.mcts_node(state=board, player=cm.PLAYER1)
    current_node.total_visits = 100
    child_node01.total_visits = 50
    child_node02.total_visits = 40
    child_node01.num_wins = 35
    child_node02.num_wins = 25
    children_array = [child_node01, child_node02]
    current_node.children = children_array
    assert child_node01.__eq__(current_node.select_next_node())


def test_expansion():
    board = cm.initialize_game_state()
    current_node = node.mcts_node(state=board, player=cm.PLAYER1)
    current_node.total_visits = 100
    current_node.open_moves = [0, 5]
    assert len(current_node.open_moves) == 2
    assert len(current_node.children) == 0
    child_node = current_node.expand_node(5)
    assert len(current_node.open_moves) == 1
    assert len(current_node.children) == 1
    assert current_node.open_moves[0] == 0
    assert child_node.__eq__(current_node.children[0])