import QimportEverything

def shootRandom():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, shotCount, gridChoice, blackGrid, whiteGrid, freeGrid, cleanMode, hitFields

    if len(freeGrid) == 0: # wenn das grid der unbeschossenen felder leer ist, wechsle auf das andere
        #cleanMode = True # aktiviere aufräum modus

        if gridChoice:
            freeGrid = blackGrid
        else:
            freeGrid = whiteGrid
    
    pickedField = [0, 0]

    while len(freeGrid) > 0:
        pickedField = random.choice(freeGrid) # nehme eine zufällige position

        if pickedField not in shotFields:
            break
    
    if freeGrid.count(pickedField) > 0:
        freeGrid.remove(pickedField)

    aimXY[0] = pickedField[0]
    aimXY[1] = pickedField[1]



    if cleanMode == True:
        lastHits = hitFields.copy()
        return shootLine()

    possibleDirections = [1, 2, 3, 4]
    shotCount = 0
    shotFields.append(aimXY.copy()) # setzte aim XY auf geschossene Felder
    tuple_aimXY = (aimXY[0], aimXY[1]) # wandele aimXY liste in tuple um
    return tuple_aimXY # gebe den schuss zurück