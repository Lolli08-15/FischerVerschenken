shotlist = []
shots = -1
def initAI(player):
    global shotlist, shots
    for fish in player.fishes:
        for slot in fish.occupied:
            shotlist.append(slot)

def shootAI(player):
    global shotlist, shots
    if len(shotlist) < 1:
        initAI(player)
    shots +=1
    return shotlist[shots]

def resetAI():
    global shotlist, shots
    shotlist = []
    shots=-1