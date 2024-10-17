def place(player,posX,posY,direction,length):
    from test_game import Fish

    used = []   # erstelle "used" array

    for fish in player.fishes: # wiederhole für anzahl der fische
        used.append((fish.posX*10)+fish.posY) # merke welche position bereits verwendet wurde

        for i in range(fish.length): # wiederhole für die länge
            if i == 0: # skippe den ersten Durchlauf
                pass

            elif fish.direction == 0: # wenn der Fisch nach oben ausgerichtet ist,
                used.append((fish.posX*10)+(fish.posY-i)) # merke den offset des Fisches
            elif fish.direction == 1: # wenn der Fisch nach rechts ausgerichtet ist,
                used.append(((fish.posX+i)*10)+fish.posY) # merke den offset des Fisches
            elif fish.direction == 2: # wenn der Fisch nach unten ausgerichtet ist,
                used.append((fish.posX*10)+(fish.posY+i)) # merke den offset des Fisches
            else: # wenn keins von oben, dann muss er links sein, also
                used.append(((fish.posX-i)*10)+fish.posY) # merke den offset des Fisches

    newFish = [(posX*10)+(posY)] # speicher position des versuchs in "newFish"

    for i in range(length): # wiederhole für die länge
        if i == 0: # skippe den ersten Durchlauf
            pass

        elif direction == 0: # wenn der fisch nach oben ausgerichtet ist,
            used.append((posX*10)+(posY-i)) # merke den offset des versuches
            newFish.append((posX*10)+(posY-i)) # merke offset  des versuches in "newFish"
            if 10 > (posY-i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False # gebe False als nicht plazierbar aus

        elif direction == 1: # wenn der fisch nach oben ausgerichtet ist,
            used.append(((posX+i)*10)+posY) # merke den offset des versuches
            newFish.append(((posX+i)*10)+posY) # merke offset  des versuches in "newFish"
            if 10 > (posX+i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False

        elif direction == 2: # wenn der fisch nach oben ausgerichtet ist,
            used.append((posX*10)+(posY+i)) # merke den offset des versuches
            newFish.append((posX*10)+(posY+i)) # merke offset  des versuches in "newFish"
            if 10 > (posY+i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False # gebe False als nicht plazierbar aus

        else: # wenn keins von oben, dann muss er links sein, also
            used.append(((posX-i)*10)+posY) # merke den offset des versuches
            newFish.append(((posX-i)*10)+posY) # merke offset  des versuches in "newFish"
            if 10 > (posX-i) >= 0:pass # wenn offset außerhalb des spielbereichs liegt:
            else: return False # gebe False als nicht plazierbar aus

    if 10 > posX >= 0 and 10 > posY >= 0:pass # wenn position außerhalb des spielbereichs liegt:
    else: return False # gebe False als nicht plazierbar aus

    if len(used) == len(set(used)): # überprüfe nach duplikaten?
        fish = Fish(posX,posY,direction,length,newFish) # erstelle neuen fisch
        player.addFish(fish) # füge Fish in das player objekt ein
        return True # gebe True als plazierbar aus
    else: return False # wenn nicht dann gebe False als nicht plazierbar aus
