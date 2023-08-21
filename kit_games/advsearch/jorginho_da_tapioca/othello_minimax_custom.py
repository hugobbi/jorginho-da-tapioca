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

    max_depth = 20
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
            return 500 if winner == player else -500
    else:
        legal_moves = len(list(state.legal_moves()))
        opponent = "W" if player == "B" else "B"
        player_points, player_coins = 0, 0
        points_weight, coins_weight, moves_weight = 0.7, 0.1, 0.2
        board = state.board.tiles
        for line_board, line_mask in zip(board, EVAL_TEMPLATE):
            for tile, value in zip(line_board, line_mask):
                if tile == player:
                    player_coins += 1
                    player_points += value
                elif tile == opponent:
                    player_coins -= 1
                    player_points -= value
        return player_points * points_weight + player_coins * coins_weight + legal_moves * moves_weight
    
