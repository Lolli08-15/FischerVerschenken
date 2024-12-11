import random
from operator import add


def resetAI():
    global hit, recentHits, freeSquares, gridSquares, targetShots
    gridCounter = random.randint(0,2)
    hit     = 0     #resolving hits
    recentHits = list()             #list of shots since the last sink
    freeSquares = set()             #generate possible squares, to keep track of shots
    gridSquares = set()             #squares to shoot if not aiming
    targetShots = set()             #squares to shoot if yes aiming
    for x in range(10):
        gridCounter += 1
        for y in range(10):
            gridCounter += 1
            freeSquares.add((x,y))   
            if gridCounter % 2:
                gridSquares.add((x,y))
        
def clearAim():     #clear up and shoot at grid
    global hit, gridSquares
    hit=0                   #reset Vars
    recentHits.clear
    gridSquares &= freeSquares      #remove hit squares from grid
    if not gridSquares:     #if grid squares are empty
        gridSquares = freeSquares
    return aiShoot(gridSquares)
     
def shootAI(response):
    global hit, targetShots, gridSquares
    if response == 0 and hit == 0:      #misses
        return clearAim()
    elif response == 1 or response == 2:    #1st hit
        hit = 1
        recentHits.append(pickedSquare)
        targetShots = set()
        for each in recentHits:   #up, right, left, down
            targetShots.add(tuple(map(add, each, (0,-1))))      #up
            targetShots.add(tuple(map(add, each, (1,0))))       #right
            targetShots.add(tuple(map(add, each, (0,1))))       #down
            targetShots.add(tuple(map(add, each, (-1,0))))      #left
        targetShots &= freeSquares      #remove hit squares from grid
        return clearAim() if not targetShots else aiShoot(targetShots)     #if target shots are empty
    elif hit == 1:                      #miss after hit
        targetShots &= freeSquares      #remove hit squares from grid
        return clearAim() if not targetShots else aiShoot(targetShots)     #if target shots are empty
        
def aiShoot(aim):
    global pickedSquare   
    pickedSquare = random.choice(list(aim))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)            
    return aimX, aimY     #returns aim coordinates
    