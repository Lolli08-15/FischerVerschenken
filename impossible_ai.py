shotlist = []
shots = -1
def initAI(player):
    for fish in player.fishes:
        for slot in fish.occupied:
            shotlist.append(slot)

def shootAI(player):
    if len(shotlist) < 1:
        initAI(player)
    shots +=1
    return shotlist[shots]

def resetAI():
    shotlist = []
    shots=-1