from typing import Tuple, Callable
import time

class Timer():
    def __init__(self, max_time: float) -> None:
        self.start_time = time.time()
        self.max_time = max_time
    
    def check_timer(self) -> bool:
        return time.time() - self.start_time >= self.max_time

def minimax(state, player: str, alpha: float, beta: float, max_depth: int, eval_function: Callable, timer: Timer, is_max: bool):
    # verify depth and time
    if max_depth == 0 or state.is_terminal() or timer.check_timer():
        return eval_function(state, player), None

    # max
    if is_max:
        max_value = float("-inf")
        max_action = None
        for action in state.legal_moves():
            child_state = state.next_state(action)
            evaluation, x = minimax(child_state, player, alpha, beta, max_depth - 1, eval_function, timer, is_max=False)
            if evaluation > max_value:
                max_value = evaluation
                max_action = action
            alpha = max(alpha, max_value)
            if alpha >= beta:
                break
        return max_value, max_action
    
    # min
    else: 
        min_value = float("+inf")
        min_action = None
        for action in state.legal_moves(): 
            child_state = state.next_state(action)
            evaluation, x = minimax(child_state, player, alpha, beta, max_depth - 1, eval_function, timer, is_max=True)
            if evaluation < min_value:
                min_value = evaluation
                min_action = action
            beta = min(beta, min_value)
            if alpha >= beta:
                break
        return min_value, min_action


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

    timer = Timer(4.5) # maximum time that minimax algorithm can execute
    player = state.player
    is_max = True
    infinity = float("inf")
    value, action = minimax(state, player, -infinity, infinity, max_depth, eval_func, timer, is_max)
    return action