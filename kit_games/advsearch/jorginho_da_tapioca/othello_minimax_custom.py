import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    max_depth = 12
    return minimax_move(state, max_depth, evaluate_custom)


def evaluate_custom(state, player:str) -> float: # uses mask + mobility
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    if state.is_terminal():
        winner = state.winner()
        if winner is None:
            return 0
        else:
            return 131 if winner == player else -131
    else:
        opponent = "W" if player == "B" else "B"
        player_pieces = 0
        opponent_pieces = 0
        player_points = 0
        opponent_points = 0
        board = state.board.tiles
        for line_board, line_mask in zip(board, EVAL_TEMPLATE):
            for tile, value in zip(line_board, line_mask):
                if tile == player:
                    player_pieces += 1
                    player_points += value
                elif tile == opponent:
                    opponent_pieces += 1
                    opponent_points += value
        return (player_points + player_pieces) - (opponent_points + opponent_pieces)
