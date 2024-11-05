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
    hit=0
    recentHits.clear()
    targetShots.clear()
    gridSquares &= freeSquares
    if not gridSquares:
        for each in alltheHits: 
            gridSquares.add(tuple(map(add, each, (0,-1))))      #up
            gridSquares.add(tuple(map(add, each, (1,0))))       #right
            gridSquares.add(tuple(map(add, each, (0,1))))       #down
            gridSquares.add(tuple(map(add, each, (-1,0))))      #left
        gridSquares &= freeSquares
        
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
            if not targetShots:
                return clearAim()
            else:
                return aiShoot(targetShots)
        elif hit > 1:
            ax, ay = recentHits[0]
            bx, by = recentHits[1]
            dx, dy = (ax-bx,ay-by)
            for each in recentHits:
                targetShots.add(tuple(map(add, each, (dx, dy))))
                targetShots.add(tuple(map(add, each, (-dx, -dy))))
            targetShots &= freeSquares
            if not targetShots:
                return clearAim()
            else:
                return aiShoot(targetShots)
        print("uh oh")
        pass
    elif response == 0:         #if miss
        targetShots &= freeSquares
        if not targetShots:
            return clearAim()
        else:
            return aiShoot(targetShots)
    else:
        return clearAim()
        
        
#the main function
def aiShoot(aim):
    global pickedSquare   
    pickedSquare = random.choice(list(aim))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY     #returns aim coordinates
    