import QimportEverything

def shootAllWay():
    global shotFields, aimXY, lastHits, offset, xOffset, tuple_aimXY, possibleDirections, shotCount, cleanMode, hitFields, freeField
    


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