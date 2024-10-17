def place(player1,posX,posY,direction,length):
    from test_game import Fish
    used = []
    for fish in player1.fishes:
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
        #print(used)
    
    for i in range(length):
            if i == 0:
                pass
            elif direction == 0:
                used.append((posX*10)+(posY-i))
            elif direction == 1:
                used.append(((posX+i)*10)+posY)
            elif direction == 2:
                used.append((posX*10)+(posY+i))
            else:
                used.append(((posX-i)*10)+posY)

    if len(used) == len(set(used)):
        fish = Fish(posX,posY,direction,length)
        player1.addFish(fish)
        return True
    else: return False
