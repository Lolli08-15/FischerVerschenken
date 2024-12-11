# Hai AIQ

import random

# init alle variablen
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

# generiere beide grids
for x in range(10):
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

toggleGridMode = True #  <------------------------ manuelle Einstelung um grid mode ein oder auszuschalten

if toggleGridMode == False: # wenn gridmode aus ist, dann setze die beiden grids zu einem zusammen
    freeGrid = whiteGrid + blackGrid
else: # wenn nicht, wähle eines der beiden der grids aus
    if gridChoice:
        freeGrid = whiteGrid
    else:
        freeGrid = blackGrid


def resetAI():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, shotCount, gridChoice, blackGrid, whiteGrid, freeGrid, cleanMode, hitFields

    # setze alle variablen zurück
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

    # generiere beide grids
    for x in range(10):
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

    if toggleGridMode == False: # wenn gridmode aus ist, dann setze die beiden grids zu einem zusammen
        freeGrid = whiteGrid + blackGrid
    else: # wenn nicht, wähle eines der beiden der grids aus
        if gridChoice:
            freeGrid = whiteGrid
        else:
            freeGrid = blackGrid



def shootRandom():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, shotCount, gridChoice, blackGrid, whiteGrid, freeGrid, cleanMode, hitFields

    if len(freeGrid) == 0: # wenn das grid der unbeschossenen felder leer ist, wechsle auf das andere
        #cleanMode = True # aktiviere aufräum modus

        if gridChoice:
            freeGrid = blackGrid
        else:
            freeGrid = whiteGrid
    
    pickedField = [0, 0]

    while len(freeGrid) > 0: # wenn noch felder verfügbar sind
        pickedField = random.choice(freeGrid) # nehme eine zufällige position

        if pickedField not in shotFields:
            break
    
    if freeGrid.count(pickedField) > 0:
        freeGrid.remove(pickedField)

    aimXY[0] = pickedField[0]
    aimXY[1] = pickedField[1]



    if cleanMode == True: # wenn aufräum modus aktiv ist,
        lastHits = hitFields.copy() # setze die letzen schüsse in hit fields, sodass die im allway modus abgeschossen werden
        return shootLine()

    possibleDirections = [1, 2, 3, 4]
    shotCount = 0
    shotFields.append(aimXY.copy()) # setzte aim XY auf geschossene Felder
    tuple_aimXY = (aimXY[0], aimXY[1]) # wandele aimXY liste in tuple um
    return tuple_aimXY # gebe den schuss zurück

def shootAllWay():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, shotCount, cleanMode, hitFields
    


    while len(possibleDirections) >= 0: # solange noch offsets möglich sind

        if len(lastHits) >= 2 and cleanMode == False: # wenn line mode aktiv ist,
            if xOffset == True: # wenn waagerecht geschossen wird
                if possibleDirections.count(2) > 0:
                    possibleDirections.remove(2) # dann lösche oben
                if possibleDirections.count(4) > 0:
                    possibleDirections.remove(4) # dann lösche unten
            else: # wenn senkrecht geschossen wird
                if possibleDirections.count(1) > 0:
                    possibleDirections.remove(1) # dann lösche rechts
                if possibleDirections.count(3) > 0:
                    possibleDirections.remove(3) # dann lösche links
        else:
            offset = 0

        if len(possibleDirections) != 0:
            offset = random.choice(possibleDirections) # setze offset richtung auf eine zufällige der 4 verbleibenden richtungen

        if offset == 1: # wenn nach rechts offset ist

            if lastHits[shotCount][0] + 1 > 9: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset und versuch es erneut
                possibleDirections.remove(1) # lösche ihn aus dem offset
            elif lastHits[shotCount][0] + 1 in shotFields: # wenn versuch schon vorhanden
                possibleDirections.remove(1) # lösche ihn aus dem offset

            else:

                xOffset = True # stelle waagerechten offset ein
                aimXY[0] = lastHits[shotCount][0] + 1
                aimXY[1] = lastHits[shotCount][1]

            
        elif offset == 2: # wenn nach unten offset ist

            if lastHits[shotCount][1] + 1 > 9: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset
                possibleDirections.remove(2) # lösche ihn aus dem offset
            elif lastHits[shotCount][1] + 1 in shotFields: # wenn versuch schon vorhanden
                possibleDirections.remove(2) # lösche ihn aus dem offset

            else:

                xOffset = False # stelle waagerechten offset aus
                aimXY[0] = lastHits[shotCount][0]
                aimXY[1] = lastHits[shotCount][1] + 1


        elif offset == 3: # wenn nach links offset ist

            if lastHits[shotCount][0] - 1 < 0: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset und versuch es erneut
                possibleDirections.remove(3) # lösche ihn aus dem offset
            elif lastHits[shotCount][0] - 1 in shotFields:
                possibleDirections.remove(3) # lösche ihn aus dem offset

            else:

                xOffset = True # stelle waagerechten offset ein
                aimXY[0] = lastHits[shotCount][0] - 1
                aimXY[1] = lastHits[shotCount][1]

        elif offset == 4: # wenn nach oben offset ist

            if lastHits[shotCount][1] - 1 < 0: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset
                possibleDirections.remove(4) # lösche ihn aus dem offset
            elif lastHits[shotCount][1] - 1 in shotFields:
                possibleDirections.remove(4) # lösche ihn aus dem offset

            else:

                xOffset = False # stelle waagerechten offset aus
                aimXY[0] = lastHits[shotCount][0]
                aimXY[1] = lastHits[shotCount][1] - 1
                


        if aimXY not in shotFields:
            break
        else:
            if offset in possibleDirections:
                possibleDirections.remove(offset) # lösche ihn aus dem offset

        if len(possibleDirections) == 0:
            return (100, 100)



    shotFields.append(aimXY.copy()) # setzte aim XY auf geschossene Felder
    tuple_aimXY = (aimXY[0], aimXY[1]) # wandele aimXY liste in tuple um
    if freeGrid.count(tuple_aimXY) > 0:
        freeGrid.remove(tuple_aimXY)
    return tuple_aimXY # gebe den schuss zurück    


def shootLine():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, shotCount, cleanMode, hitFields

    shotCount = len(lastHits)


    while shotCount > 0: # wieerhole für die anzahl der hits
        possibleDirections = [1, 2, 3, 4]

        shotCount -= 1 # gehe ein feld zurück

        lineTry = shootAllWay() # führe ein 2 way auf feld x aus

        if lineTry[0] != 100:
            break

    if lineTry[0] == 100:
        return shootRandom()

    return lineTry




    # START -----------------------------------------------------------------------------------------

def shootAI(shotData):
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, shotCount, cleanMode, hitFields

    if shotData == 2: # wenn der letzte schuss versenkt hat,
        lastHits.append(shotFields[-1].copy()) # trage zuletzt geschossenes feld in letzte hits ein
        hitFields.append(lastHits[-1].copy()) # setzte letzen treffer auf treffer liste
        lastHits.clear() # lösche letzt getroffene hits

        return shootRandom() # schieße zufällig

    if shotData == 1: # wenn treffer
        lastHits.append(shotFields[-1].copy()) # trage zuletzt geschossenes feld in letzte hits ein
        
        hitFields.append(lastHits[-1].copy()) # setzte letzen treffer auf treffer liste
        possibleDirections = [1, 2, 3, 4]

    if len(lastHits) == 1: # wenn nur ein treffer registriert wurde
        return shootAllWay() # versuche alle umliegenden felder zu schießen

    if len(lastHits) >= 2: # wenn mehrere treffer registriert wurden
        return shootLine() # dann schieße nur auf einer linie

    if shotData == 0 & len(lastHits) == 0:
        return shootRandom()
    return "error"
