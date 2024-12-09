from AIQ_Files.QimportEverything import *


def shootLine(qVar):

    qVar.shotCount = len(qVar.lastHits)


    while qVar.shotCount > 0: # wieerhole für die anzahl der hits
        qVar.possibleDirections = [1, 2, 3, 4]

        qVar.shotCount -= 1 # gehe ein feld zurück

        lineTry = shootAllWay() # führe ein 2 way auf feld x aus

        if lineTry[0] != 100:
            break

    if lineTry[0] == 100:
        return shootRandom(qVar)

    return lineTry