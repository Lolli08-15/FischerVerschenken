from AIQ_Files.QimportEverything import *

shotFields = []
aimXY = [0, 0]
lastHits = []
offset = int
xOffset = True
tuple_aimXY = tuple()
possibleDirections = [1, 2, 3, 4]
shotCount = 0
whiteGrid = []
blackGrid = []
freeGrid = []
gridChoice = bool
cleanMode = False
hitFields = []

for x in range(10): # generiere grid
    for y in range(10):
        if y % 2 == 0:
            if x % 2 == 1:
                whiteGrid.append((x, y))
            else:
                blackGrid.append((x, y))
        else:
            if x % 2 == 0:
                whiteGrid.append((x, y))
            else:
                blackGrid.append((x, y))

gridChoice = random.choice([True, False]) # random ob das white grid ausgewählt wird

toggleGridMode = False # manuelle Einstelung um grid mode ein oder auszuschalten <------------------------

if toggleGridMode == False: # wenn gridmode aus ist, dann setze die beiden grids zu einem zusammen
    freeGrid = whiteGrid + blackGrid
else: # wenn nicht, wähle eines der beiden der grids aus
    if gridChoice:
        freeGrid = whiteGrid
    else:
        freeGrid = blackGrid