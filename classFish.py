class Fish:
    def __init__(self, posX, posY, direction, length,occupied):
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.length = length
        self.hits = 0
        self.occupied = occupied