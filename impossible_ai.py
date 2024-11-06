import random as r
shotlist = []
shots = -1
init = True
def initAI(player):
    global shotlist, shots, init
    init = False
    nofish = []
    fish_here= []
    for fish in player.fishes:
        for slot in fish.occupied:
            fish_here.append(slot)
    
    remove = []
    for x in range(10):
        for y in range(10):
            nofish.append((x,y))
    for i in nofish:
        if i in fish_here:
            remove.append(i)
    for i in remove:
        nofish.remove(i)
    if r.randint(99,99) == 99:
        nofish.extend(fish_here)
        shotlist = nofish
    else:
        fish_here.extend(nofish)
        shotlist = fish_here
    shotlist.append((5,5))

def shootAI(player):
    global shotlist, shots, init
    if len(shotlist) < 1:
        init = True
    if  init:
        initAI(player)
    aim = shotlist[0]
    shotlist.pop(0)
    return aim

def resetAI():
    global shotlist, shots, init
    shotlist = []
    shots=-1
    init = True