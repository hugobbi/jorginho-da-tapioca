from typing import Tuple, Callable

class Node():
    def __init__(self, state, action=None, parent=None) -> None:
        self.state = state
        self.action = action # action that led up to this state
        self.parent = parent
        self.children = list()
        self.value = 0 # evaluation of this state


def minimax(node: Node, player: str, alpha: float, beta: float, max_depth: int, eval_function: Callable, is_max: bool):
    # verify depth
    if max_depth == 0 or node.state.is_terminal():
        return eval_function(node.state, player)

    # max
    if is_max:
        max_value = float("-inf")
        legal_actions = list(node.state.legal_moves())
        for action in legal_actions: # if we can order by best move, itll improve algorithm
            new_state = node.state.next_state(action)
            child_node = Node(new_state, action, node) # creates new child node 
            node.children.append(child_node)
            evaluation = minimax(child_node, player, alpha, beta, max_depth - 1, eval_function, is_max=False)
            max_value = max(max_value, evaluation)
            alpha = max(alpha, evaluation)
            if alpha >= beta:
                break
        node.value = max_value
        return max_value
    
    # min
    else: 
        min_value = float("+inf")
        legal_actions = list(node.state.legal_moves())
        for action in legal_actions: # if we can order by best move, itll improve algorithm
            new_state = node.state.next_state(action)
            child_node = Node(new_state, action, node) # creates new child node 
            node.children.append(child_node)
            evaluation = minimax(child_node, player, alpha, beta, max_depth - 1, eval_function, is_max=True)
            min_value = min(min_value, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        node.value = min_value
        return min_value


def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    root_node = Node(state)
    player = state.player
    infinity = float("inf")
    minimax(root_node, player, -infinity, infinity, max_depth, eval_func, is_max=True)
    best_child = max(root_node.children, key=lambda child: child.value) # root_node.children[np.argmax([child.value for child in root_node.children])]
    return best_child.action