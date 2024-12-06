import QimportEverything


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