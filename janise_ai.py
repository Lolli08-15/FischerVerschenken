import random
from operator import add, sub


found = 0

recentHits = list()              #list of shots since the last sink
targetShots = set()             #squares to target after getting a hit
freeSquares = set()             #generate possible squares, to keep track of shots
for x in range(10):
    for y in range(10):
        freeSquares.add((x,y))   
        
        
        
def aiAim(response):
    global found
    if response == 1 and found == 0 or found > 3:
        found = 0
        return aiShoot(freeSquares)
    elif response == 1 or found > 0:               #if 
        found += 1
        recentHits.append(pickedSquare)
        for hits in recentHits:
            targetShots.add(tuple(map(add, hits, (0,-1))))
            targetShots.add(tuple(map(add, hits, (1,0))))
            targetShots.add(tuple(map(add, hits, (0,1))))
            targetShots.add(tuple(map(add, hits, (-1,0))))  #add all surrounding squares
        return aiShoot(targetShots)
    else:
        return aiShoot(freeSquares)

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
    print(f"miss {aiAim(0)}")
    print(f"miss {aiAim(0)}")
    print(f"miss {aiAim(0)}")
    print(f"hit {aiAim(0)}")
    print(f"miss {aiAim(1)}")
    print()