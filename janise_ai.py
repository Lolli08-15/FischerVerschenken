import random
from operator import add


def reset():
    global hit, recentHits, targetShots, freeSquares
    
    
    hit     = 0     #resolving hits
    recentHits = list()              #list of shots since the last sink
    freeSquares = set()             #generate possible squares, to keep track of shots
    for x in range(10):
        for y in range(10):
            freeSquares.add((x,y))   
    targetShots = freeSquares             #squares to target after getting a hit
        
        
        
def aiAim(response):
    global hit
    if response == 0 and hit == 0:      #misses
        return aiShoot(freeSquares)
    elif response == 1 or hit == 1:    #1st hit
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
            hit=0
            recentHits.clear
            return aiShoot(freeSquares)
        return aiShoot(targetShots)                                 #fire
        
        
#the main function
def aiShoot(aim):
    global pickedSquare   
    pickedSquare = random.choice(list(aim))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY     #returns aim coordinates
    

   
#DEBUG  
 
if __name__ == "__main__":
    '''
        
    shotLines.addLine(1,{{5,7},{4,7},{6,7},{7,7}})
    print(shotLines.lines[0][1]*2)
    exit'''
    reset()
    print(f"miss {aiAim(0)}")
    print(f"hit  {aiAim(0)}")
    print(f"miss {aiAim(1)}")
    print(f"hit  {aiAim(0)}")
    print(f"hit  {aiAim(1)}")
    print(f"miss {aiAim(1)}")
    print(f"miss {aiAim(0)}")
    print(f"miss {aiAim(0)}")
    print()