class Fish:
    def __init__(self, posXY, direction, length,occupied):
        self.posXY = posXY
        self.direction = direction
        self.length = length
        self.hits = 0
        self.occupied = occupied