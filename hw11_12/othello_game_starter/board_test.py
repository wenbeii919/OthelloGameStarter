import pytest
from board import Board
from disk import Disk
from collections import defaultdict


@pytest.fixture
def bd():
    """Returns a board instance with its width and height"""
    return Board(300, 300)


def test_constructor(bd):
    assert bd.WIDTH == 300
    assert bd.HEIGHT == 300
    assert bd.EDGE == 0
    assert bd.SPACING == 75
    assert bd.HALF_SPACE == 37.5
    assert bd.size == 4
    assert bd.directions == [(0, -1), (0, 1),
                             (-1, 0), (1, 0),
                             (-1, -1), (-1, 1),
                             (1, -1), (1, 1)]
    bd.disks[1][1] = Disk(112.5, 112.5, 'white')
    bd.disks[1][2] = Disk(187.5, 112.5, 'black')
    bd.disks[2][1] = Disk(112.5, 187.5, 'black')
    bd.disks[2][2] = Disk(187.5, 187.5, 'white')
    assert bd.disks[1][1] is not None
    assert bd.disks[1][2] is not None
    assert bd.disks[2][1] is not None
    assert bd.disks[2][2] is not None
    assert bd.count == {'black': 2, 'white': 2}
    assert bd.valid_moves == {(0, 1): [1, [[(2, 1), (1, 0)]]],
                              (1, 0): [1, [[(1, 2), (0, 1)]]],
                              (2, 3): [1, [[(2, 1), (0, -1)]]],
                              (3, 2): [1, [[(1, 2), (-1, 0)]]]}


def test_update_counts(bd):
    bd.update_counts()
    assert bd.count == {'black': 2, 'white': 2}


def test_input_tile(bd):
    # A valid move
    x1, y1 = 250, 156
    c1 = 'black'
    row1, col1 = 3, 2
    # An invalid move
    x2, y2 = 148, 150
    c2 = 'white'
    row2, col2 = 1, 2

    bd.avail_moves(c1)
    bd.avail_moves(c2)
    bd.get_center(x1, y1)
    bd.get_center(x2, y2)
    assert bd.input_tile(x1, y1, c1) is True
    assert bd.input_tile(x2, y2, c2) is None


def test_get_center(bd):
    bd.SPACING == 75
    bd.HALF_SPACE = 37.5
    x, y = 278, 345
    assert bd.get_center(x, y) == (262.5, 337.5)


def test_avail_moves(bd):
    assert bd.valid_moves == {(0, 1): [1, [[(2, 1), (1, 0)]]],
                              (1, 0): [1, [[(1, 2), (0, 1)]]],
                              (2, 3): [1, [[(2, 1), (0, -1)]]],
                              (3, 2): [1, [[(1, 2), (-1, 0)]]]}


def test_is_movable(bd):
    r1, c1 = 1, 1
    r2, c2 = 1, 0
    color = 'black'
    assert bd.is_movable(r1, c1, color) is True
    assert bd.is_movable(r2, c2, color) is None


def test_flip_tiles(bd):
    bd.disks[1][1].color = 'white'
    bd.flip_tiles(1, 0, 'black')
    assert bd.disks[1][1].color == 'black'


def test_within_edges(bd):
    row1, col1 = 3, 3
    row2, col2 = 4, 0
    assert bd.within_edges(row1, col1) is True
    assert bd.within_edges(row2, col2) is None
