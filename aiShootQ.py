import random

shotFields = []
aimXY = [0, 0]
lastHits = []
offset = int
xOffset = True
tuple_aimXY = tuple()
possibleDirections = [1, 2, 3, 4]
tries = 0
grid = random.random
searchMode = False
shotCount = 0
allWayFailed = False
whiteGrid = []
blackGrid = []
freeGrid = []
gridChoice = bool

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

if gridChoice:
    freeGrid = whiteGrid
else:
    freeGrid = blackGrid



def shootRandom():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, tries, grid, searchMode, shotCount, gridChoice, blackGrid, whiteGrid, freeGrid

    if len(freeGrid) == 0:

        if gridChoice:
            freeGrid = blackGrid
        else:
            freeGrid = whiteGrid

    pickedField = random.choice(freeGrid)
    freeGrid.remove(pickedField)

    aimXY[0] = pickedField[0]
    aimXY[1] = pickedField[1]

    possibleDirections = [1, 2, 3, 4]
    shotCount = 0
    shotFields.append(aimXY.copy()) # setzte aim XY auf geschossene Felder
    tuple_aimXY = (aimXY[0], aimXY[1]) # wandele aimXY liste in tuple um
    return tuple_aimXY # gebe den schuss zurück

def shootAllWay():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, tries, grid, searchMode, shotCount

    while len(possibleDirections) >= 0: # solange noch offsets möglich sind

        if len(lastHits) >= 2: # wenn line mode aktiv ist,
            if xOffset == True: # wenn waagerecht geschossen wird
                if 2 in possibleDirections:
                    possibleDirections.remove(2) # dann lösche oben
                if 4 in possibleDirections:
                    possibleDirections.remove(4) # dann lösche unten
            else: # wenn senkrecht geschossen wird
                if 1 in possibleDirections:
                    possibleDirections.remove(1) # dann lösche rechts
                if 3 in possibleDirections:
                    possibleDirections.remove(3) # dann lösche links

        offset = random.choice(possibleDirections) # setze offset richtung auf eine zufällige der 4 verbleibenden richtungen

        if offset == 1: # wenn nach rechts offset ist

            if lastHits[shotCount][0] + 1 > 9: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset und versuch es erneut
                possibleDirections.remove(1) # lösche ihn aus dem offset
            elif lastHits[shotCount][0] + 1 in shotFields: # wenn versuch schon vorhanden
                possibleDirections.remove(1) # lösche ihn aus dem offset

                xOffset = True # stelle waagerechten offset ein
                aimXY[0] = lastHits[shotCount][0] + 1
                aimXY[1] = lastHits[shotCount][1]
            
        elif offset == 2: # wenn nach unten offset ist

            if lastHits[shotCount][1] + 1 > 9: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset
                possibleDirections.remove(2) # lösche ihn aus dem offset
            elif lastHits[shotCount][1] + 1 in shotFields: # wenn versuch schon vorhanden
                possibleDirections.remove(2) # lösche ihn aus dem offset

                xOffset = False # stelle waagerechten offset aus
                aimXY[0] = lastHits[shotCount][0]
                aimXY[1] = lastHits[shotCount][1] + 1

        elif offset == 3: # wenn nach links offset ist

            if lastHits[shotCount][0] - 1 < 0: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset und versuch es erneut
                possibleDirections.remove(3) # lösche ihn aus dem offset
            elif lastHits[shotCount][0] - 1 in shotFields:
                possibleDirections.remove(3) # lösche ihn aus dem offset

                xOffset = True # stelle waagerechten offset ein
                aimXY[0] = lastHits[shotCount][0] - 1
                aimXY[1] = lastHits[shotCount][1]

        elif offset == 4: # wenn nach oben offset is

            if lastHits[shotCount][1] - 1 < 0: # wenn der offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem offset
                possibleDirections.remove(4) # lösche ihn aus dem offset
            elif lastHits[shotCount][1] - 1 in shotFields:
                possibleDirections.remove(4) # lösche ihn aus dem offset

                xOffset = False # stelle waagerechten offset aus
                aimXY[0] = lastHits[shotCount][0]
                aimXY[1] = lastHits[shotCount][1] - 1
                
        if aimXY not in shotFields:
            break
        else:
            possibleDirections.remove(offset) # lösche ihn aus dem offset

        if len(possibleDirections) == 0:
            return False


    shotFields.append(aimXY.copy()) # setzte aim XY auf geschossene Felder
    tuple_aimXY = (aimXY[0], aimXY[1]) # wandele aimXY liste in tuple um
    if freeGrid.count(tuple_aimXY) > 0:
        freeGrid.remove(tuple_aimXY)
    return tuple_aimXY # gebe den schuss zurück    

def shootLine():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, tries, grid, searchMode, shotCount

    shotCount = len(lastHits) # setze 

    while shotCount > 0: # wieerhole für die anzahl der hits
        possibleDirections = [1, 2, 3, 4]

        shotCount -= 1 # gehe ein feld zurück

        lineTry = shootAllWay() # führe ein 2 way auf feld x aus

        if lineTry != False:
            break

    if lineTry == False:
        return shootRandom()

    return lineTry



    # START -----------------------------------------------------------------------------------------


def aiAimQ(shotData):
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, tries, grid, searchMode, shotCount

    if shotData == 2: # wenn der letzte schuss versenkt hat,
        lastHits.clear() # lösche letzt getroffene hits

        return shootRandom() # schieße zufällig

    if shotData == 1: # wenn treffer
        lastHits.append(shotFields[-1].copy()) # trage zuletzt geschossenes feld in letzte hits ein
        possibleDirections = [1, 2, 3, 4]

    if len(lastHits) == 1: # wenn nur ein treffer registriert wurde
        return shootAllWay() # versuche alle umliegenden felder zu schießen

    if len(lastHits) >= 2: # wenn mehrere treffer registriert wurden
        return shootLine() # dann schieße nur auf einer linie

    if shotData == 0 & len(lastHits) == 0:
        return shootRandom()
    return "error"