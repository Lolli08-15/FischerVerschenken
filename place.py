def place(player,posXY,direction,length):
    from classFish import Fish

    used = []   # erstelle "used" array

    for fish in player.fishes: # wiederhole für anzahl der fische
        used.append(fish.posXY) # merke welche position bereits verwendet wurde

        for i in range(fish.length): # wiederhole für die länge
            if i == 0: # skippe den ersten Durchlauf
                pass

            elif fish.direction == 0: # wenn der fisch nach oben ausgerichtet ist,
                used.append((fish.posXY[0])+(fish.posXY[1]-i)) # merke den offset des fisches
            elif fish.direction == 1: # wenn der fisch nach rechts ausgerichtet ist,
                used.append(((fish.posXY[0]+i))+fish.pposXY[1]) # merke den offset des fisches
            elif fish.direction == 2: # wenn der fisch nach unten ausgerichtet ist,
                used.append((fish.posXY[0])+(fish.posXY[1]+i)) # merke den offset des fisches
            else: # wenn keins von oben, dann muss er links sein, also
                used.append(((fish.posXY[0]-i))+fish.posXY[1]) # merke den offset des fisches

    used.append((posXY))
    newFish = [(posXY)] # speicher position des versuchs in "newFish"

    for i in range(length): # wiederhole für die länge
        if i == 0: # skippe den ersten Durchlauf
            pass

        elif direction == 0: # wenn der fisch nach oben ausgerichtet ist,
            used.append((fish.posXY[0])+(fish.posXY[1]-i)) # merke den offset des versuches
            newFish.append((fish.posXY[0])+(fish.posXY[1]-i)) # merke offset  des versuches im aktuellem fisch
            if 10 > (posXY[1]-i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False # gebe False als nicht plazierbar aus

        elif direction == 1: # wenn der fisch nach rechts ausgerichtet ist,
            used.append(((fish.posXY[0]+i))+fish.posXY[1]) # merke den offset des versuches
            newFish.append(((fish.posXY[0]+i))+fish.posXY[1]) # merke offset  des versuches im aktuellem fisch
            if 10 > (posXY[0]+i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False

        elif direction == 2: # wenn der fisch nach oben ausgerichtet ist,
            used.append((fish.posXY[0])+(fish.posXY[1]+i)) # merke den offset des versuches
            newFish.append((fish.posXY[0])+(fish.posXY[1]+i)) # merke offset  des versuches im aktuellem fisch
            if 10 > (posXY[1]+i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False # gebe False als nicht plazierbar aus

        else: # wenn keins von oben, dann muss er links sein, also
            used.append(((fish.posXY[0]-i))+fish.posXY[1]) # merke den offset des versuches
            newFish.append(((fish.posXY[0]-i))+fish.posXY[1]) # merke offset  des versuches im aktuellem fisch
            if 10 > (posXY[0]-i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False # gebe False als nicht plazierbar aus

    if 10 > posXY[0] >= 0 and 10 > posXY[1] >= 0:pass # wenn position außerhalb des spielbereichs liegt:
    else: return False # gebe False als nicht plazierbar aus

    if len(used) == len(set(used)): # überprüfe nach duplikaten?
        fish = Fish(posXY,direction,length,newFish) # erstelle neuen fisch
        player.addFish(fish) # füge Fish in das player objekt ein
        return True # gebe True als plazierbar aus
    else: return False # wenn nicht dann gebe False als nicht plazierbar aus
