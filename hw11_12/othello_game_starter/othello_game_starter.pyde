from board import Board
from players import Players
from game_controller import GameController

WIDTH = 600
HEIGHT = 600

board = Board(WIDTH, HEIGHT)
players = Players(board, ai=True)
game_controller = GameController(board, players, WIDTH, HEIGHT)

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 255)

def draw():
    background(51, 102, 0)
    board.display()
    game_controller.update()

def mousePressed():
    players.play()
