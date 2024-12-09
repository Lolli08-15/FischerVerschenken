from AIQ_Files.QimportEverything import *

def shootRandom(qVar):

    if len(qVar.freeGrid) == 0: # wenn das grid der unbeschossenen felder leer ist, wechsle auf das andere
        #cleanMode = True # aktiviere aufräum modus

        if qVar.gridChoice:
            qVar.freeGrid = qVar.blackGrid
        else:
            qVar.freeGrid = qVar.whiteGrid
    
    pickedField = [0, 0]

    while len(qVar.freeGrid) > 0:
        pickedField = random.choice(qVar.freeGrid) # nehme eine zufällige position

        if pickedField not in qVar.shotFields:
            break
    
    if qVar.freeGrid.count(pickedField) > 0:
        qVar.freeGrid.remove(pickedField)

    qVar.aimXY[0] = pickedField[0]
    qVar.aimXY[1] = pickedField[1]



    if qVar.cleanMode == True:
        lastHits = qVar.hitFields.copy()
        return shootLine(qVar)

    qVar.possibleDirections = [1, 2, 3, 4]
    qVar.shotCount = 0
    qVar.shotFields.append(qVar.aimXY.copy()) # setzte aim XY auf geschossene Felder
    qVar.tuple_aimXY = (qVar.aimXY[0], qVar.aimXY[1]) # wandele aimXY liste in tuple um
    return qVar.tuple_aimXY # gebe den schuss zurück