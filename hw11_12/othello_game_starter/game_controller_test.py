from game_controller import GameController
from board import Board
from players import Players


def test_constructor():
    board = Board(300, 300)
    players = Players(board)
    gc = GameController(board, players, 300, 300)
    assert gc.WIDTH == 300
    assert gc.HEIGHT == 300
    assert gc.TEXT_X == 150
    assert gc.GO_Y == 140
    assert gc.RESULT_Y == 160
    assert gc.RESTART_Y == 180
    assert gc.bd is board
    assert gc.pl is players
    assert gc.RECT_W == 150
    assert gc.RECT_H == 300
    assert gc.RECT_C == 7
    assert gc.player_b_wins is False
    assert gc.player_w_wins is False
    assert gc.tie is False
