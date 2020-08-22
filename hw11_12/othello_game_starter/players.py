import time


class Players:
    def __init__(self, board, ai=False):
        """Represents the human player and AI player"""
        self.bd = board
        self.tile_colors = ['black', 'white']
        self.take_turns = 0
        self.ai = ai
        self.game_over = False
        self.TEXT_X = self.bd.WIDTH / 2
        self.TEXT_Y = self.bd.HEIGHT / 2
        self.ai_counter = 60

    def play(self):
        """
        Human player plays by mouse clicking
        AI player plays by get_move method
        """
        if self.game_over:
            self.bd.__init__(self.bd.WIDTH, self.bd.HEIGHT)
            self.game_over = False
            self.take_turns = 0
            return

        if self.ai and self.take_turns == 1:
            row, col = self.get_move()
            x = self.bd.HALF_SPACE + col * self.bd.SPACING
            y = self.bd.HALF_SPACE + row * self.bd.SPACING
        else:
            x, y = mouseX, mouseY

        if self.take_turns == 0:
            succeed = self.bd.input_tile(x, y, self.tile_colors[0])
            if succeed:
                self.take_turns = 1

        else:
            succeed = self.bd.input_tile(x, y, self.tile_colors[1])            
            if succeed:
                self.take_turns = 0
                self.ai_counter = 60

        # If one player runs out of valid moves, switch to the other player
        self.bd.avail_moves(self.tile_colors[self.take_turns])
        if not self.bd.valid_moves:
            self.take_turns ^= 1
            self.bd.avail_moves(self.tile_colors[self.take_turns])
            # If neither player has valid moves, game's over
            if not self.bd.valid_moves:
                self.game_over = True
        self.bd.display()

    def get_move(self):
        """
        Sorts the valid_moves dictionary according to the steps
        returns the valid move with the most steps
        """
        max_steps = sorted(
            self.bd.valid_moves.items(),
            key=lambda x: x[1][0],
            reverse=True
        )
        if max_steps:
            return max_steps[0][0]

    def record_scores(self, pl_name):
        """
        Compare the current player's score with the top player's score
        Records the score accordingly
        """
        name_score = []
        curr_score = self.bd.count['black']
        with open('scores.txt', 'r') as f:
            for line in f:
                line = line.rsplit(' ', 1)
                name_score.append((int(line[1]), line[0]))

        if name_score:
            if curr_score >= name_score[0][0]:
                name_score.insert(0, (curr_score, pl_name))
        else:
            name_score.append((curr_score, pl_name))

        with open('scores.txt', 'w') as f:
            for score, name in name_score:
                f.write(name + ' ' + str(score) + '\n')
