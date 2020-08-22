from collections import defaultdict
from line import Line
from disk import Disk

EDGE = 0
SPACING = 75


class Board:
    """Draws the playing board"""
    def __init__(self, WIDTH, HEIGHT):
        """Draws the board with its initial setup"""
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.EDGE = EDGE
        self.SPACING = SPACING
        self.HALF_SPACE = self.SPACING / 2
        self.size = self.WIDTH // self.SPACING
        self.count = {'black': 0, 'white': 0}
        self.directions = [(0, -1), (0, 1),
                           (-1, 0), (1, 0),
                           (-1, -1), (-1, 1),
                           (1, -1), (1, 1)]
        self.valid_moves = defaultdict(list)

        # Initialize lines
        self.vert_lines = [Line(self.SPACING * i, self.EDGE,
                                self.SPACING * i, self.HEIGHT)
                           for i in range(1, self.WIDTH//self.SPACING)]
        self.horz_lines = [Line(self.EDGE, self.SPACING * i,
                                self.WIDTH, self.SPACING * i,)
                           for i in range(1, self.WIDTH//self.SPACING)]

        # Initialize rows and columns of disks
        # based on spacing and width of the board
        self.disks = [[None for c in range(self.size)]
                      for r in range(self.size)]

        # Initialize four disks in the center of the board
        half_size = self.size // 2
        x1 = self.WIDTH // 2 - self.HALF_SPACE
        y1 = self.HEIGHT // 2 - self.HALF_SPACE
        x2 = self.WIDTH // 2 + self.HALF_SPACE
        y2 = self.HEIGHT // 2 + self.HALF_SPACE

        self.disks[half_size - 1][half_size - 1] = Disk(x1, y1, 'white')
        self.disks[half_size - 1][half_size] = Disk(x2, y1, 'black')
        self.disks[half_size][half_size - 1] = Disk(x1, y2, 'black')
        self.disks[half_size][half_size] = Disk(x2, y2, 'white')

        self.update_counts()
        self.avail_moves('black')

    def display(self):
        """Displays all the graphical objects"""
        self.display_lines()
        self.display_disks()
        self.draw_valid_moves()

    def display_lines(self):
        """Calls each line's display method"""
        for i in range(len(self.vert_lines)):
            self.vert_lines[i].display()
        for i in range(len(self.horz_lines)):
            self.horz_lines[i].display()

    def display_disks(self):
        """Calls each disk's display method"""
        for row in self.disks:
            for disk in row:
                if disk:
                    disk.display()

    def update_counts(self):
        """Update the counts for black and white tiles"""
        self.count = {'black': 0, 'white': 0}
        for row in self.disks:
            for disk in row:
                if disk:
                    self.count[disk.color] += 1

    def input_tile(self, x, y, color):
        """According to the players' moves, input tiles into the board"""
        row = y // self.SPACING
        col = x // self.SPACING
        self.avail_moves(color)
        if (row, col) in self.valid_moves:
            tile_x, tile_y = self.get_center(x, y)
            self.disks[row][col] = Disk(tile_x, tile_y, color)
            self.flip_tiles(row, col, color)
            self.update_counts()
            return True

    def get_center(self, x, y):
        """
        Based on the player's mouseX and mouseY
        return circle center position
        """
        x = ((x // self.SPACING) * self.SPACING) + self.HALF_SPACE
        y = ((y // self.SPACING) * self.SPACING) + self.HALF_SPACE
        return x, y

    def avail_moves(self, color):
        """Store available tile movements into valid_moves dictionary"""
        self.valid_moves = defaultdict(list)
        for row in range(self.size):
            for col in range(self.size):
                if (self.disks[row][col] and
                        self.disks[row][col].color == color):
                    for dir in self.directions:
                        steps = 0
                        next_r, next_c = row + dir[0], col + dir[1]
                        if self.is_movable(next_r, next_c, color):
                            while self.is_movable(next_r, next_c, color):
                                steps += 1
                                next_r = next_r + dir[0]
                                next_c = next_c + dir[1]
                            if (self.within_edges(next_r, next_c) and
                                    not self.disks[next_r][next_c]):
                                if self.valid_moves[(next_r, next_c)]:
                                    self.valid_moves[(
                                        next_r, next_c)][0] += steps
                                    self.valid_moves[(next_r, next_c)][1].append([(row, col),(-dir[0], -dir[1])])
                                else:
                                    self.valid_moves[(next_r, next_c)] = [steps, [[(row, col), (-dir[0], -dir[1])]]]

    def is_movable(self, r, c, color):
        """
        Checks if the move is within the board edges
        and the other two criteria
        """
        if (self.within_edges(r, c) and self.disks[r][c]
                and self.disks[r][c].color != color):
            return True

    def flip_tiles(self, row, col, color):
        """
        According to the start and end tile position, and the direction
        switches the tile color
        """
        for item in self.valid_moves[(row, col)][1]:
            start_r, start_c = item[0]
            end_r, end_c = row, col
            dir_r, dir_c = item[1]
            while ((end_r, end_c) != (start_r, start_c) and
                    self.within_edges(end_r, end_c)):
                end_r += dir_r
                end_c += dir_c
                self.disks[end_r][end_c].color = color

    def within_edges(self, row, col):
        """Test if the valid tile is within the limit of board size"""
        if 0 <= row < self.size and 0 <= col < self.size:
            return True

    def draw_valid_moves(self):
        """Displays the available moves for players"""
        for row, col in self.valid_moves:
            x = self.HALF_SPACE + self.SPACING * col
            y = self.HALF_SPACE + self.SPACING * row
            Disk(x, y, None).invisible_disk()
