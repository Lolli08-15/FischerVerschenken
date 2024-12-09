from AIQ_Files.QimportEverything import *

class Qvar:
    def __init__(self):
        self.shotFields = None
        self.aimXY
        self.lastHits
        self.offset, self.xOffset, self.tuple_aimXY, self.possibleDirections, self.shotCount, self.gridChoice, self.blackGrid, self.whiteGrid, self.freeGrid, self.cleanMode, self.hitFields = None

    def resetAIQ(self):

        self.shotFields = []
        self.aimXY = [0, 0]
        self.lastHits = []
        self.offset = int
        self.xOffset = True
        self.tuple_aimXY = tuple()
        self.possibleDirections = [1, 2, 3, 4]
        self.shotCount = 0
        self.whiteGrid = []
        self.blackGrid = []
        self.freeGrid = []
        self.gridChoice = bool
        self.cleanMode = False
        self.hitFields = []

        for x in range(10): # generiere grid
            for y in range(10):
                if y % 2 == 0:
                    if x % 2 == 1:
                        self.whiteGrid.append((x, y))
                    else:
                        self.blackGrid.append((x, y))
                else:
                    if x % 2 == 0:
                        self.whiteGrid.append((x, y))
                    else:
                        self.blackGrid.append((x, y))

        self.gridChoice = random.choice([True, False]) # random ob das white grid ausgewählt wird

        toggleGridMode = True

        if toggleGridMode == False: # wenn gridmode aus ist, dann setze die beiden grids zu einem zusammen
            self.freeGrid = self.whiteGrid + self.blackGrid
        else: # wenn nicht, wähle eines der beiden der grids aus
            if self.gridChoice:
                self.freeGrid = self.whiteGrid
            else:
                self.freeGrid = self.blackGrid