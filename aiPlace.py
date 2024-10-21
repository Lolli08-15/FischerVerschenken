import settings
import random

def aiPlace(ai):
    for x in settings.fish_lengths: # wiederhole für die anzahl der verschiedenen fische

        canPlace = False
        while canPlace == False: # wiederhole bis ein fisch plaziert werden kann

            posXY = (0, 0)
            posXY[0] = random.randint(0, 9) # random bs go
            posXY[1] = random.randint(0, 9) # random bs go
            direction = random.randint(0, 3) # random bs go
            fishLength = x # generiere fisch länge
            canPlace = ai.place(ai, posXY, direction, fishLength) # überprüfe ob man plazieren kann
        