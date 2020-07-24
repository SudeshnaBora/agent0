import numpy as np
from agents.common import common

'''
  The MCTS node implementation
'''


class mcts_node:

    def __init__(self, move=None, parent=None, state=None, player=None):
        # the parent of this node
        self.parent = parent
        # the move leading to this state
        self.move = move
        # the board associated with this state
        self.state = state
        # the player connected with this board
        self.player = player
        self.num_wins = 0
        self.total_visits = 0
        self.children = []
        self.open_moves = self.get_open_moves()

    def get_open_moves(self) -> np.ndarray:
        """
        Getter function to obtain possible open columns
        :return:
        An array of column numbers
        """

        if common.check_end_state(self.state, self.player) == common.GameState.IS_WIN:
            return np.array([])
        else:
            return np.array(common.get_free_columns(self.state))

    def set_visit_and_win(self, result: int):
        """
        Update the win and visits value of a node
        :param result: 0 if the game ended in a draw, 1 if the player won adn -1 if the opponent won
        """
        self.total_visits += 1
        self.num_wins += result

    def select_next_node(self):
        """
        Selects the next node to expand
        :return:
        The child node with the largest UCB1 value
        """
        candidate_child_node = None
        candidate_child_score = - 1000000
        for child in self.children:
            score = child.num_wins / child.total_visits + np.sqrt(2) * np.sqrt(
                np.log(self.total_visits) / child.total_visits)
            if score > candidate_child_score:
                candidate_child_node = child
                candidate_child_score = score

        return candidate_child_node

    def expand_node(self, action: common.PlayerAction):
        """
        :param action: Action to apply in order to expand a node
        :return: Child after node expand_node (The board of the child node
        corresponds to the board of the parent after the action was applied)
        """
        # Apply the action to the board of the parent node
        opponent = common.PLAYER1
        if self.player == common.PLAYER1:
            opponent = common.PLAYER2
        new_board, original_board = common.apply_player_action(self.state.copy(), action, opponent)
        # Create a new child node with that action and board
        child = mcts_node(move=action, parent=self, state=new_board, player=opponent)
        # Append the created child to the children of the parent
        self.children.append(child)
        # Remove the action from the untried actions from the parent
        self.open_moves = np.setdiff1d(self.open_moves, action)

        return child
