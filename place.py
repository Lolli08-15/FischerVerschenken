def place(player,posX,posY,direction,length):
    from classFish import Fish
    used = []
    for fish in player.fishes:
        used.append((fish.posX*10)+fish.posY)
        for i in range(fish.length):
            if i == 0:
                pass
            elif fish.direction == 0:
                used.append(((fish.posX*10)+(fish.posY-i)))
            elif fish.direction == 1:
                used.append(((fish.posX+i)*10)+fish.posY)
            elif fish.direction == 2:
                used.append((fish.posX*10)+(fish.posY+i))
            else:
                used.append(((fish.posX-i)*10)+fish.posY)
    used.append((posX*10)+(posY-i))
    newFish = [(posX*10)+(posY)]
    for i in range(length):
        if i == 0:
            pass 
        elif direction == 0:
            used.append((posX*10)+(posY-i))
            newFish.append((posX*10)+(posY-i))
            if 10 > (posY-i) >= 0:pass
            else: return False
        elif direction == 1:
            used.append(((posX+i)*10)+posY)
            newFish.append(((posX+i)*10)+posY)
            if 10 > (posX+i) >= 0:pass
            else: return False
        elif direction == 2:
            used.append((posX*10)+(posY+i))
            newFish.append((posX*10)+(posY+i))
            if 10 > (posY+i) >= 0:pass
            else: return False
        else:
            used.append(((posX-i)*10)+posY)
            newFish.append(((posX-i)*10)+posY)
            if 10 > (posX-i) >= 0:pass
            else: return False
    if 10 > posX >= 0 and 10 > posY >= 0:pass
    else: return False
    if len(used) == len(set(used)):
        fish = Fish(posX,posY,direction,length,newFish)
        player.addFish(fish)
        return True
    else: return False
