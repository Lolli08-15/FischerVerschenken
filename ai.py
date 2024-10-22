import random
from operator import add, sub

notSunk = 0                     #case vars
prevMiss = 0

hitShots = set()                #list of shots that hit
recentShots = list()            #list of recent shots that hit (order important)
targetShots = set()             #squares to target after getting a hit
directionS = set()              #directionally important coords
freeSquares = set()             #generate possible squares, to keep track of shots
for x in range(10):
    for y in range(10):
        freeSquares.add((x,y))   
        


def aiAim(response):     #input is whether the last shot missed(0), hit(1) or sunk(2) 
    global notSunk
    global targetShots
    global prevMiss
    
    if(response == 2):              #if enemy sinks
        notSunk = 0                 #well... it sunk
        hitShots.clear()            #no more shots needed
        return aiShoot(freeSquares)
    
    elif(response == 1 and notSunk == 0):                   #last shot a hit
        notSunk = 1                                         #block this line
        prevMiss = 0                                        #reset notSunk
        hitShots.add(pickedSquare)
        recentShots.append(pickedSquare)
        for hits in recentShots:
            targetShots.add(tuple(map(add, hits, (0,-1))))
            targetShots.add(tuple(map(add, hits, (1,0))))
            targetShots.add(tuple(map(add, hits, (0,1))))
            targetShots.add(tuple(map(add, hits, (-1,0))))  #add all surrounding squares
        return aiShoot(targetShots)
    
    elif(notSunk == 1):
        if (response == 1):                                 #if hit, go that, or the other way
            hitShots.add(pickedSquare)
            recentShots.append(pickedSquare)
            directionX, directionY=tuple(map(sub, recentShots[0], recentShots[-1]))                   #calculate direction
            targetShots.clear()
            '''targetShots.add(tuple(map(add, recentShots[-1], (directionX, directionY))))
            targetShots.add(tuple(map(add, recentShots[0], (-directionX, -directionY))))'''
            directionS = set((directionX,directionY),(-directionX,-directionY))
            for each in directionS:
                while True:
                    #check up and down     if alredy miss??
                    if('''ende'''):
                        break
            aiShoot(targetShots)
            
        else:                                               #if miss try other direction
            if(prevMiss == 0):
                prevMiss = 1
            else:
                eeeeyup = len(recentShots)                  #RENAME  KEEPS TRACK OF SUNK SHIP SIZE
                pass#
            
    else:
        return aiShoot(freeSquares)

def aiShoot(aim):
    global pickedSquare                             
    targetSquares = freeSquares & list(aim)         #remove previous shots/oob
    pickedSquare = random.choice(targetSquares)     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY       #returns aim coordinates
    
if __name__ == "__main__":
    print(f"miss {aiAim(0)}")
    print(f"miss {aiAim(0)}")
    print(f"miss {aiAim(0)}")
    print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
    print(f"hit {aiAim(0)}")
    print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
    print(f"hit {aiAim(1)}")
    print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
    print(f"egal {aiAim(1)}")
    print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
    print(f"miss {aiAim(0)}")
    print(f"Not Sunk {notSunk} prevMiss {prevMiss}")