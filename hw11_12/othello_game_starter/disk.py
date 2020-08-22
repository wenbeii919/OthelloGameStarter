CIR_WH = 65
SPACING = 75
SQUARE = 65


class Disk:
    """A disk"""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.SPACING = SPACING
        self.SQUARE = SQUARE
        self.CIR_WH = CIR_WH
        self.color = color

    def display(self):
        """Draws the disk"""
        if self.color == 'white':
            fill(255)
        elif self.color == 'black':
            fill(0)
        ellipse(self.x, self.y, self.CIR_WH, self.CIR_WH)

    def invisible_disk(self):
        """Draws disks with no color filled"""
        stroke(153, 255, 51)
        noFill()
        rect(self.x + 1, self.y + 1, self.SQUARE, self.SQUARE)
