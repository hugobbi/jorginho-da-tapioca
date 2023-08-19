import random
from typing import Tuple, Union

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

class Node():
    def __init__(self, state, previous_move=None, parent=None) -> None:
        self.state = state
        self.previous_move = previous_move
        self.parent = parent
        self.visits = 0
        self.value = 0
        self.children = set()

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def is_root(self) -> bool:
        return self.parent is None

def selection(node: Node) -> Node:
    while not node.is_leaf():
        node = max(node.children, key=lambda child: child.value / child.visits)
    return node

def expansion(node: Node) -> Union[Node, None]: # plays one random move and creates a child node in the tree
    if not node.state.is_terminal(): # doesnt expand terminal node
        unexplored_moves = [move for move in node.state.legal_moves() if move not in [child_node.previous_move for child_node in node.children]]
        if unexplored_moves:
            move = random.choice(unexplored_moves)
            new_state = node.state.next_state(move)
            child_node = Node(new_state, move, node)
            node.children.add(child_node)
            return child_node
    return None


def simulation(node: Node) -> int: # simulates a game randomly, returning 1 if won, 0 if lost or 0.5 if tied
    state = node.state.copy()
    player = node.state.player
    while not state.is_terminal():
        legal_moves = list(state.legal_moves())
        next_move = random.choice(legal_moves)
        state = state.next_state(next_move)
    winner = state.winner()
    if winner is None: # returns 0.5 if tied
        return 0.5
    else:
        return 1 if winner == player else 0
    
def backpropagation(node: Node, result: int) -> None: # propagates the result of the game along the tree
    while not node.is_root():
        node.value += result
        node.visits += 1
        node = node.parent

def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    root_node = Node(state)
    iterations = 1000 # "depth" of search
    for _ in range(iterations): # we will have 5 seconds to make a play (i hope so)
        selected_node = selection(root_node)
        leaf_node = expansion(selected_node)
        if leaf_node is not None:
            result = simulation(leaf_node)
            backpropagation(leaf_node, result)
        else:
            result = simulation(selected_node)
            backpropagation(selected_node, result)
    best_child = max(root_node.children, key=lambda child: child.value / child.visits)
    return best_child.previous_move
