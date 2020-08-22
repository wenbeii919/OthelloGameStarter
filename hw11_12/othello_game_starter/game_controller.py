RECT_CORNER = 7
RECT_H = 10
GO_Y = -10
RESULT_Y = 10
RESTART_Y = 30


class GameController:
    """Maintains the state of the game."""
    def __init__(self, board, players, WIDTH, HEIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TEXT_X = self.WIDTH/2
        # y_coordinate for announcing 'game over'
        self.GO_Y = self.HEIGHT/2 + GO_Y
        # y_coordinate for announcing the winner
        self.RESULT_Y = self.HEIGHT/2 + RESULT_Y
        # y_coordinate for restart
        self.RESTART_Y = self.HEIGHT/2 + RESTART_Y
        self.bd = board
        self.RECT_W = self.WIDTH / 2
        self.RECT_H = self.HEIGHT
        self.RECT_C = RECT_CORNER
        self.RECT_Y = self.HEIGHT / 2
        self.player_b_wins = False
        self.player_w_wins = False
        self.tie = False
        self.pl = players
        self.score_recorded = False

    def update(self):
        """Carries out necessary actions if either player wins"""
        fill(0)
        textSize(20)
        rectMode(CENTER)

        if self.pl.game_over:
            player_b_tile = self.bd.count['black']
            player_w_tile = self.bd.count['white']
            if player_b_tile > player_w_tile:
                fill(255)
                rect(self.TEXT_X, self.RECT_Y, self.RECT_W, self.RECT_H, self.RECT_C)
                fill(0)
                text("GAME OVER!", self.TEXT_X, self.GO_Y)
                self.show_score()
                text("BLACK WINS", self.TEXT_X, self.RESULT_Y)
                text("CLICK TO RESTART", self.TEXT_X, self.RESTART_Y)
            elif player_b_tile < player_w_tile:
                fill(255)
                rect(self.TEXT_X, self.RECT_Y, self.RECT_W, self.RECT_H, self.RECT_C)
                fill(0)
                text("GAME OVER!", self.TEXT_X, self.GO_Y)
                self.show_score()
                text("WHITE WINS", self.TEXT_X, self.RESULT_Y)
                text("CLICK TO RESTART", self.TEXT_X, self.RESTART_Y)
            else:
                fill(255)
                rect(self.TEXT_X, self.RECT_Y, self.RECT_W, self.RECT_H, self.RECT_C)
                fill(0)
                text("GAME OVER!", self.TEXT_X, self.GO_Y)
                self.show_score()
                text("IT'S A TIE", self.TEXT_X, self.RESULT_Y)
                text("CLICK TO RESTART", self.TEXT_X, self.RESTART_Y)
            if not self.score_recorded:
                pl_name = self.input('enter your name')
                if pl_name:
                    print('hi ' + pl_name)
                elif pl_name == '':
                    pl_name = 'Dummy_player'
                    print('[empty string]')
                else:
                    pl_name = 'Dummy_player'
                    print(pl_name)  # Canceled dialog will print None
                self.pl.record_scores(pl_name)
                self.score_recorded = True

        if self.pl.take_turns == 1 and self.pl.ai and not self.pl.game_over:
            if self.pl.ai_counter > 0:
                self.pl.ai_counter -= 1
            else:
                self.pl.play()

    def show_score(self):
        """Display the current score."""
        fill(0)
        textSize(20)
        textAlign(CENTER)
        txt = 'black: ' + str(self.bd.count['black']) + \
              '        ' + \
              'white: ' + str(self.bd.count['white'])
        text(txt, self.WIDTH / 2, self.HEIGHT - 10)

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
