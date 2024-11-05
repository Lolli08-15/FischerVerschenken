def place(player,posXY,direction,fish_type):
    from classFish import Fish
    from fish_dict import get_fish_dict
    dic = get_fish_dict()
    if fish_type == 1:
        selected_fish=dic["fred"]
    elif fish_type == 2:
        selected_fish=dic["robin"]
    elif fish_type == 3:
        selected_fish=dic["robert"]
    elif fish_type == 4:
        selected_fish=dic["roland"]
    elif fish_type == 5:
        selected_fish=dic["rochen"]
    elif fish_type == 6:
        selected_fish=dic["lobert"]
    else:
        selected_fish=dic["dontnut"]
    direct= "o"+str(direction)
    selected_fish = selected_fish[direct]
    
    used = []   # erstelle "used" array

    for fish in player.fishes:
        for pos in fish.occupied:
            used.append(pos) # merke welche position bereits verwendet wurde
            
    newFish = [] # speicher position des versuchs in "newFish"
    for offset in selected_fish:
        newFish.append((posXY[0]+offset[0],posXY[1]+offset[1]))

    used += newFish
    for i in used:
        if 0 > i[0] or i[0] > 9 or 0 > i[1] or i[1] > 9:
            return False
    if len(used) == len(set(used)): # überprüfe nach duplikaten?
        fish = Fish(posXY,direction,fish_type,newFish) # erstelle neuen fisch
        player.addFish(fish) # füge Fish in das player objekt ein
        print(newFish)
        return True # gebe True als plazierbar aus
    else: return False # wenn nicht dann gebe False als nicht plazierbar aus