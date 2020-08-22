from players import Players
from board import Board
import pytest


def test_constructor():
    board = Board(300, 300)
    pl = Players(board)
    assert pl.bd is board
    assert pl.tile_colors == ['black', 'white']
    assert pl.take_turns == 0
    assert pl.ai is False
    assert pl.game_over is False
    assert pl.TEXT_X == 150
    assert pl.TEXT_Y == 150


def test_play():
    board = Board(300, 300)
    pl = Players(board)
    pl.take_turns = 0
    x1, y1 = 133, 216
    x2, y2 = 226, 151
    c = 'black'
    pl.bd.avail_moves(c)
    pl.bd.get_center(x1, y1)
    pl.bd.get_center(x2, y2)
    assert pl.bd.input_tile(x1, y1, c) is None
    assert pl.bd.input_tile(x2, y2, c) is True
    assert pl.bd.valid_moves == {(0, 1): [1, [[(2, 1), (1, 0)]]],
                                 (1, 0): [1, [[(1, 2), (0, 1)]]],
                                 (2, 3): [1, [[(2, 1), (0, -1)]]],
                                 (3, 2): [1, [[(1, 2), (-1, 0)]]]}


def test_get_move():
    board = Board(300, 300)
    pl = Players(board)
    assert pl.get_move() == (1, 0)
