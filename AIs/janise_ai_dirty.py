import random
from operator import add


def resetAI():
    global hit, recentHits, freeSquares, gridSquares, targetShots, shotToSink, alltheHits
    gridCounter = random.randint(0,2)
    hit     = 0     #resolving hits
    recentHits = list()             #list of shots since the last sink
    alltheHits = list()
    shotToSink = list()
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
    hit=0                           #reset vars
    recentHits.clear()
    targetShots.clear()
    gridSquares &= freeSquares      #remove hit squares from grid
    if not gridSquares:             #if gridSquares are empty
        for each in alltheHits:     #check squares surrounding hits
            gridSquares.add(tuple(map(add, each, (0,-1))))      #up
            gridSquares.add(tuple(map(add, each, (1,0))))       #right
            gridSquares.add(tuple(map(add, each, (0,1))))       #down
            gridSquares.add(tuple(map(add, each, (-1,0))))      #left
        gridSquares &= freeSquares  #remvoe hit squares
        if not gridSquares:         #if still empty
            gridSquares = freeSquares   #shoot at remaining squares
        
    return aiShoot(gridSquares)
 
def shootAI(response):
    global hit, targetShots, gridSquares
    if response==1: 
        hit += 1
        recentHits.append(pickedSquare)
        alltheHits.append(pickedSquare)
        targetShots = set()
        if hit <= 1:  #only 1st hits
            for each in recentHits:  
                targetShots.add(tuple(map(add, each, (0,-1))))      #up
                targetShots.add(tuple(map(add, each, (1,0))))       #right
                targetShots.add(tuple(map(add, each, (0,1))))       #down
                targetShots.add(tuple(map(add, each, (-1,0))))      #left
            targetShots &= freeSquares
            return clearAim() if not targetShots else aiShoot(targetShots)     #if target shots are empty
        elif hit > 1:
            ax, ay = recentHits[0]
            bx, by = recentHits[1]
            dx, dy = (ax-bx,ay-by)      #get direction (difference recent 1 to 0)
            for each in recentHits:
                targetShots.add(tuple(map(add, each, (dx, dy))))    #add direction one way
                targetShots.add(tuple(map(add, each, (-dx, -dy))))  #add the other way
            targetShots &= freeSquares  #removes previously hit squares
            return clearAim() if not targetShots else aiShoot(targetShots)     #if target shots are empty
        print("uh oh")
        pass
    elif response == 0:         #if miss
        targetShots &= freeSquares
        return clearAim() if not targetShots else aiShoot(targetShots)     #if target shots are empty
    else:                       #if sink
        return clearAim()
        
def aiShoot(aim):
    global pickedSquare   
    pickedSquare = random.choice(list(aim))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY     #returns aim coordinates
    