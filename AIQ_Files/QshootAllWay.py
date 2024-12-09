from AIQ_Files.QimportEverything import *

def shootAllWay(qVar):

    while len(qVar.possibleDirections) >= 0: # solange noch offsets möglich sind

        if len(qVar.lastHits) >= 2 and qVar.cleanMode == False: # wenn line mode aktiv ist,
            if qVar.xOffset == True: # wenn waagerecht geschossen wird
                if qVar.possibleDirections.count(2) > 0:
                    qVar.possibleDirections.remove(2) # dann lösche oben
                if qVar.possibleDirections.count(4) > 0:
                    qVar.possibleDirections.remove(4) # dann lösche unten
            else: # wenn senkrecht geschossen wird
                if qVar.possibleDirections.count(1) > 0:
                    qVar.possibleDirections.remove(1) # dann lösche rechts
                if qVar.possibleDirections.count(3) > 0:
                    qVar.possibleDirections.remove(3) # dann lösche links
        else:
            qVar.offset = 0

        if len(qVar.possibleDirections) != 0:
            qVar.offset = random.choice(qVar.possibleDirections) # setze qVar.offset richtung auf eine zufällige der 4 verbleibenden richtungen

        if qVar.offset == 1: # wenn nach rechts qVar.offset ist

            if qVar.lastHits[qVar.shotCount][0] + 1 > 9: # wenn der qVar.offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem qVar.offset und versuch es erneut
                qVar.possibleDirections.remove(1) # lösche ihn aus dem qVar.offset
            elif qVar.lastHits[qVar.shotCount][0] + 1 in qVar.shotFields: # wenn versuch schon vorhanden
                qVar.possibleDirections.remove(1) # lösche ihn aus dem qVar.offset

            else:

                qVar.xOffset = True # stelle waagerechten qVar.offset ein
                qVar.aimXY[0] = qVar.lastHits[qVar.shotCount][0] + 1
                qVar.aimXY[1] = qVar.lastHits[qVar.shotCount][1]

            
        elif qVar.offset == 2: # wenn nach unten qVar.offset ist

            if qVar.lastHits[qVar.shotCount][1] + 1 > 9: # wenn der qVar.offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem qVar.offset
                qVar.possibleDirections.remove(2) # lösche ihn aus dem qVar.offset
            elif qVar.lastHits[qVar.shotCount][1] + 1 in qVar.shotFields: # wenn versuch schon vorhanden
                qVar.possibleDirections.remove(2) # lösche ihn aus dem qVar.offset

            else:

                qVar.xOffset = False # stelle waagerechten qVar.offset aus
                qVar.aimXY[0] = qVar.lastHits[qVar.shotCount][0]
                qVar.aimXY[1] = qVar.lastHits[qVar.shotCount][1] + 1


        elif qVar.offset == 3: # wenn nach links qVar.offset ist

            if qVar.lastHits[qVar.shotCount][0] - 1 < 0: # wenn der qVar.offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem qVar.offset und versuch es erneut
                qVar.possibleDirections.remove(3) # lösche ihn aus dem qVar.offset
            elif qVar.lastHits[qVar.shotCount][0] - 1 in qVar.shotFields:
                qVar.possibleDirections.remove(3) # lösche ihn aus dem qVar.offset

            else:

                qVar.xOffset = True # stelle waagerechten qVar.offset ein
                qVar.aimXY[0] = qVar.lastHits[qVar.shotCount][0] - 1
                qVar.aimXY[1] = qVar.lastHits[qVar.shotCount][1]

        elif qVar.offset == 4: # wenn nach oben qVar.offset ist

            if qVar.lastHits[qVar.shotCount][1] - 1 < 0: # wenn der qVar.offset versuch außerhalb des spielfeldes liegt, lösche ihn aus dem qVar.offset
                qVar.possibleDirections.remove(4) # lösche ihn aus dem qVar.offset
            elif qVar.lastHits[qVar.shotCount][1] - 1 in qVar.shotFields:
                qVar.possibleDirections.remove(4) # lösche ihn aus dem qVar.offset

            else:

                qVar.xOffset = False # stelle waagerechten qVar.offset aus
                qVar.aimXY[0] = qVar.lastHits[qVar.shotCount][0]
                qVar.aimXY[1] = qVar.lastHits[qVar.shotCount][1] - 1
                


        if qVar.aimXY not in qVar.shotFields:
            break
        else:
            if qVar.offset in qVar.possibleDirections:
                qVar.possibleDirections.remove(qVar.offset) # lösche ihn aus dem qVar.offset

        if len(qVar.possibleDirections) == 0:
            return (100, 100)



    qVar.shotFields.append(qVar.aimXY.copy()) # setzte aim XY auf geschossene Felder
    qVar.tuple_aimXY = (qVar.aimXY[0], qVar.aimXY[1]) # wandele qVar.aimXY liste in tuple um
    if qVar.freeGrid.count(qVar.tuple_aimXY) > 0:
        qVar.freeGrid.remove(qVar.tuple_aimXY)
    return qVar.tuple_aimXY # gebe den schuss zurück    