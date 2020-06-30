import numpy as np

'''
  The MCTS node implementation
'''


class MctsNode:

    def __init__(self, state, parent=None):
        # the number of visits to this node. As this class would be initialised
        # on first visit so initialising with 1
        self.visits = 1
        # the reward calculated with this node after simulation
        self.reward = 0.0
        # it is the ndArray board of this Node
        self.state = state
        # array storing children of this node
        self.children = []
        # array storing the moves to the children of the node
        self.children_move = []
        # node to store the parent of this node
        self.parent = parent

    def set_children(self, child, move):
        """
        Setter function to set the children and the children_move attributes
        :param child: the child node of the current node
        :param move: the move that leads to the child node
        :return:
        """
        # initialising the child node as it has been visited
        child_node = MctsNode(child, self)
        # appending this child node to the parent node's child attribute
        self.children.append(child_node)
        # appending the move leading to the child node
        self.children_move.append(move)

    def set_score(self, reward):
        """
        Setter to update the reward and visits
        :return:
        """
        self.reward += reward
        self.visits += 1

    def check_fully_explored(self) -> bool:
        """
        Check if the board has been fully explored
        :return: boolean flag with true if yes otherwise false
        """
