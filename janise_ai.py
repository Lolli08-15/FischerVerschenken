import random
from operator import add, sub

hit     = 0     #resolving hits
found   = 0     #direction found
capped  = 0     #line capped off

recentHits = list()              #list of shots since the last sink
targetShots = set()             #squares to target after getting a hit
freeSquares = set()             #generate possible squares, to keep track of shots
for x in range(10):
    for y in range(10):
        freeSquares.add((x,y))   
        
        
        
def aiAim(response):
    global hit
    global found
    global capped
    
    
    if response == 0 and hit == 0:      #misses
        return aiShoot(freeSquares)
    elif response == 1 and hit == 0:    #1st hit
        hit = 1
        recentHits.append(pickedSquare)
        for each in [(0,-1),(1,0),(0,1),(-1,0)]:   #up, right, left, down
            targetShots.add(tuple(map(add, recentHits[0], each)))   #add adjacents as targets
        return aiShoot(targetShots)                                 #fire
    elif response == 0 and hit == 1 and found == 0:
        return aiShoot(targetShots)                                 #fire again
    elif response == 1 and hit == 1 and found == 0:    #direction found
        found = 1
        recentHits.append(pickedSquare)
        ax, ay = recentHits[-1]
        bx, by = recentHits[-2]
        direction = abs(ax-bx)   #find direction of line 1=horizontal
        for each in recentHits:
            continue
            
        
        



#the main function
def aiShoot(aim):
    global pickedSquare                              
    targetSquares = freeSquares & set(aim)         #remove previous shots/oob
    pickedSquare = random.choice(list(targetSquares))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY       #returns aim coordinates
    

   
#DEBUG  
 
if __name__ == "__main__":
    '''
        
    shotLines.addLine(1,{{5,7},{4,7},{6,7},{7,7}})
    print(shotLines.lines[0][1]*2)
    exit'''

    print(f"miss {aiAim(0)}")
    print(f"hit {aiAim(0)}")
    print(f"miss {aiAim(1)}")
    print(f"hit {aiAim(0)}")
    print(f"miss {aiAim(1)}")
    print(f"miss {aiAim(0)}")
    print(f"hit {aiAim(0)}")
    print(f"miss {aiAim(1)}")
    print()