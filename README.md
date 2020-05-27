# Connect 4 with minimax algorithm using alpha beta pruning

### Author<br>
Sudeshna Bora

### Algorithm for heuristic

The heuristic scoring is divided into the following categories :-

1. Possibility of connecting 4 either horizontally, vertically or diagonally.
This is given a very high value (in my case a 100).

2. Possibility of connecting 3 with an open slot near it (in any direction). 

3. Possibility of connecting 2 with an open slot near it.

4. Special value is given to the center column. 

5. Scores are deducted if the opponent has a connect4 or connect3. 
Though connect 4 scenario should not occur. Keeping it as I would latter forget
why I didn't keep a check for connected 4

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

1. https://en.wikipedia.org/wiki/Minimax#Pseudocode
2. https://www.researchgate.net/publication/331552609_Research_on_Different_Heuristics_for_Minimax_Algorithm_Insight_from_Connect-4_Game
