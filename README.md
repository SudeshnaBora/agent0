# Connect 4

Algorithms used :-
1. Minimax algorithm
2. Monte Carlo Tree Search.

### Author<br>
Sudeshna Bora

### Minimax Algorithm

The minimax algorithm is a recursive algorithm whose goal is to minimise the potential loss for the worst case scenario for the player and maximise the minimum gain for the player. The output of the minimax algorithm is to give us the column and the probable maximum gain we can get by making that move. The scoring in the minimax algorithm depends on a heuristic scoring algorithm (described below).

#### Algorithm for heuristic

The heuristic scoring is divided into the following categories :-

1. Possibility of connecting 4 either horizontally, vertically or diagonally.
This is given a very high value (in my case a 100).

2. Possibility of connecting 3 with an open slot near it (in any direction). 

3. Possibility of connecting 2 with an open slot near it.

4. Scores are deducted if the opponent has a connect4 or connect3. 
Though connect 4 scenario should not occur. Keeping it as I would latter forget
why I didn't keep a check for connected 4

### Monte Carlo Tree Search 

The Monte Carlo method is a heuristic search algorithm. In case of connect4 it analyses the most promising column expanding the search tree for the probable moves search space. The selection of the next move for expansion is based on randomness. The application of Monte Carlo tree search in games is based on many playouts. The game is played out to the very end by selecting moves at random. By the end of the playout, a weight is assigned to the node. This algorithm does away with the necessity of using a heuristic algorithm. The MCTS backs on the principle of **exploration** and **exploitation**.

#### Steps in MCTS algorithm 

1. **Selection:**  Select a node and expand it till a Leaf node is reached. A leaf node is a not yet expanded node. 
2. **Expansion:**  Expand the leaf node by taking into account all possible child nodes of this node and choosing one in random from that.
3. **Simulation:** This is the playout portion of the MCTS algorithm.
4. **Backpropagation:** After the playout, the information of the win/loss is propagated back up. 

A important aspect of MCTS is to balance the exploration and exploitation of prior knowledge. I have used the **Upper Confidence bound** function for this. This is defined as :-

**(no.of win of this node/ no. of simulation of this node) + exploration parameter * square root (ln(no.of total simulation)/no. of simulation of this node)**

A known disadvantage of MCTS is sometimes a good move can be ignored due to lack of exploration.

### Code Quality 

pep8 

### Code Coverage<br>

Please check the following files (in htmlcov folder) for code coverage:
1. [Complete overview](https://htmlpreview.github.io/?https://github.com/SudeshnaBora/agent0/blob/master/htmlcov/index.html)<br>
2. [Coverage for common.py](https://htmlpreview.github.io/?https://github.com/SudeshnaBora/agent0/blob/master/htmlcov/agents_common_common_py.html)<br>
3. [Coverage for agent_minimax.py](https://htmlpreview.github.io/?https://github.com/SudeshnaBora/agent0/blob/master/htmlcov/agents_agent_minimax_py.html)<br> 

<b>To run coverage locally</b>

pip install coverage <br>
pip install pytest-cov<br> 
pytest --cov --cov-report html


### Sources

1. https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
2. https://www.researchgate.net/publication/331552609_Research_on_Different_Heuristics_for_Minimax_Algorithm_Insight_from_Connect-4_Game
3. Took help for the left diagonal heuristic scoring if condition. I am not able to find the blog for the same.
