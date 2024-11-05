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
    hit=0
    recentHits.clear
    gridSquares &= freeSquares
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
            targetShots.add(tuple(map(add, each, (0,-1))))   #add adjacents as targets
            targetShots.add(tuple(map(add, each, (1,0))))   #add adjacents as targets
            targetShots.add(tuple(map(add, each, (0,1))))   #add adjacents as targets
            targetShots.add(tuple(map(add, each, (-1,0))))   #add adjacents as targets
        targetShots &= freeSquares
        if not targetShots:             
            return clearAim()
        return aiShoot(targetShots)                                 #fire
    elif hit == 1:                      #miss after hit
        targetShots &= freeSquares
        if not targetShots:             
            return clearAim()
        return aiShoot(targetShots)                                 #fire
        
        
#the main function
def aiShoot(aim):
    global pickedSquare   
    pickedSquare = random.choice(list(aim))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    print(pickedSquare)
    freeSquares.remove(pickedSquare)
    return aimX, aimY     #returns aim coordinates
    

   
#DEBUG  
 
if __name__ == "__main__":
    '''
        
    shotLines.addLine(1,{{5,7},{4,7},{6,7},{7,7}})
    print(shotLines.lines[0][1]*2)
    exit'''
    resetAI()
    print(f"miss {shootAI(0)}")
    print(f"hit  {shootAI(0)}")
    print(f"miss {shootAI(1)}")
    print(f"hit  {shootAI(0)}")
    print(f"hit  {shootAI(1)}")
    print(f"miss {shootAI(1)}")
    print(f"miss {shootAI(0)}")
    print(f"miss {shootAI(0)}")
    print()