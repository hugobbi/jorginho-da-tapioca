import random
from typing import Tuple
import numpy as np
import time

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

class Timer():
    def __init__(self, max_time: float) -> None:
        self.start_time = time.time()
        self.max_time = max_time
    
    def check_timer(self) -> bool:
        return time.time() - self.start_time >= self.max_time

class Node():
    def __init__(self, state, previous_move=None, parent=None) -> None:
        self.state = state # current states
        self.previous_move = previous_move # move that led up to this node 
        self.parent = parent # parent node
        self.visits = 0 # number of visits
        self.value = 0 # number of wins
        self.children = list() # children of this node
        self._untried_moves = self._get_untried_moves() # moves that this node can make

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def is_root(self) -> bool:
        return self.parent is None

    def _get_untried_moves(self) -> list:
        if not self.state.is_terminal():
            return list(self.state.legal_moves())
        else: 
            return list()
    
    def is_fully_expanded(self) -> bool:
        return self.state.is_terminal() or len(self._untried_moves) == 0
    
    def expand(self) -> "Node": # expands one node
        move = self._untried_moves.pop() # selects one move from the node's untried moves
        next_state = self.state.next_state(move)
        child_node = Node(next_state, move, self) # expands node
        self.children.append(child_node) # adds the new child

        return child_node
    
    def select_best_child(self, c=0.1) -> "Node":
        node_visits = 1 if self.visits == 0 else self.visits # so we dont divide by zero, nor do log of zero
        children_ucb_values = []
        for child in self.children:
            child_visits = 1 if child.visits == 0 else child.visits # so we dont divide by zero
            children_ucb_values.append((child.value / child_visits) + c * np.sqrt((2 * np.log(node_visits) / child_visits)))
        return self.children[np.argmax(children_ucb_values)] # gets child with highest ucb value
    
    def selection_and_expansion(self): 
        current_node = self
        while not current_node.state.is_terminal(): # while the node is not terminal (end of game)
            if not current_node.is_fully_expanded(): # if node hasnt been fully expanded yet
                return current_node.expand() # expands node, that is, takes one legal action in the node's state
            else:
                current_node = current_node.select_best_child() # if it is fully expanded, go to the next layer in the tree, selecting the best child
        return current_node # if terminal node is reached, return
    
    def simulation(self, player) -> int: # simulates a game randomly
        state = self.state.copy()
        while not state.is_terminal():
            legal_moves = list(state.legal_moves())
            next_move = random.choice(legal_moves)
            state = state.next_state(next_move)
        winner = state.winner()
        if winner is None: # returns 0 if tied
            return 0
        else:
            return 1 if winner == player else -1
        
    def backpropagation(self, result: int) -> None: # propagates the result of the game along the tree OK
        while not self.is_root():
            self.value += result
            self.visits += 1
            self = self.parent


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state. 
    The game is not specified, but this is MCTS and should handle any game, since
    their implementation has the same interface.

    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    timer = Timer(4.9)
    root_node = Node(state.copy())
    player = root_node.state.player
    while not timer.check_timer(): # while there is time
        explored_node = root_node.selection_and_expansion() # selects node to be simulated
        result = explored_node.simulation(player) # simulates node, given that the player is the root node
        explored_node.backpropagation(result) # propagates the result up the tree
    best_child = root_node.select_best_child(c=0) # selects the best child of the root node to make the move, with no exploration
    return best_child.previous_move
