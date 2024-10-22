import random
from operator import add, sub

notSunk = 0                     #case vars
prevMiss = 0
cluster = 0
rows = 0

class ShotLines():
    def __init__(self):      
        self.lines = []
        
    def addLine(self,sink, hits):               #bool, list
        length = len(hits)
        directional, trash = tuple(map(sub,hits[0],hits[1]))
        self.lines.append([sink, hits, length, directional]) #sunk?, list of hits in line, length of the line, direction(0 is horizontal)

shotLines = ShotLines()
sinkSeries = list()             #if i start tracking def. lengths
hitShots = set()                #list of shots that hit
recentHits = list()              #list of shots since the last sink
recentShots = list()            #list of recent shots that hit (order important)
targetShots = set()             #squares to target after getting a hit
directionS = set()              #directionally important coords
freeSquares = set()             #generate possible squares, to keep track of shots
for x in range(10):
    for y in range(10):
        freeSquares.add((x,y))   
        
def undefinedAiming():
    return aiShoot(freeSquares)
    
def parallelFish(response):
    return undefinedAiming()
    if rows==0:
        baseLine = len(shotLines.lines)         #select which line of shots is the base
        rows = shotLines.lines[baseLine][2]     #the total number of rows it'll have
        targetShots.clear
        for x in range(-1,1,2):
            [each for each in shotLines.lines[baseLine][2]]

        
    if response == 2:
        pass
    
    

def aiAim(response):     #input is whether the last shot missed(0), hit(1) or sunk(2) 
    global notSunk
    global targetShots
    global prevMiss
    global cluster
    
    if(response == 2 and cluster == 0):              #if enemy sinks
        notSunk = 0                 #well... it sunk
        recentHits.append(pickedSquare)
        shotLines.addLine(1, recentHits)      #add sunk boat
        recentHits.clear()            #clear past shots
        return aiShoot(freeSquares)
    
    elif(response == 1 and notSunk == 0):                   #last shot a hit
        notSunk = 1                                         #block this line
        prevMiss = 0                                        #reset notSunk
        recentHits.append(pickedSquare)
        recentShots.append(pickedSquare)
        for hits in recentShots:
            targetShots.add(tuple(map(add, hits, (0,-1))))
            targetShots.add(tuple(map(add, hits, (1,0))))
            targetShots.add(tuple(map(add, hits, (0,1))))
            targetShots.add(tuple(map(add, hits, (-1,0))))  #add all surrounding squares
        return aiShoot(targetShots)
    
    elif(cluster == 1):
        return parallelFish(response)
    
    elif(notSunk == 1):
        if (response == 1):                                 #if hit, go that, or the other way
            recentHits.append(pickedSquare)
            recentShots.append(pickedSquare)
            directionX, directionY=tuple(map(sub, recentShots[-2], recentShots[-1]))                   #calculate direction
            targetShots.clear()
            directionS = set(((directionX,directionY),(-directionX,-directionY)))                        #tuple in set
            print("line62", targetShots, directionS)
            for each in directionS:
                for thing in recentHits:                                              #check ends of straight line, 
                    targetShots.add(tuple(map(add, each, thing)))
            if set(targetShots) & freeSquares == set():                              #if empty
                shotLines.addLine(0,recentHits)
                recentHits.clear
                cluster = 1
                return parallelFish(response)
            return aiShoot(targetShots)
            
        else:                                               #if miss try other direction
            if(prevMiss == 0):
                prevMiss = 1
                
                return undefinedAiming()
            else:
                shotLines.addLine(0,recentHits)
                recentHits.clear
                cluster = 1
                return parallelFish(response)
            
    else:
        return aiShoot(freeSquares)
    

def aiShoot(aim):
    global pickedSquare                              
    targetSquares = freeSquares & set(aim)         #remove previous shots/oob
    pickedSquare = random.choice(list(targetSquares))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY       #returns aim coordinates
    

    
'''
    
#DEBUG    
shotLines.addLine(1,{{5,7},{4,7},{6,7},{7,7}})
print(shotLines.lines[0][1]*2)
exit'''

print(f"miss {aiAim(0)}")
print(f"hit {aiAim(0)}")
print("recent1", recentHits)
exit

print(f"sink {aiAim(1)}")
print(recentHits)
print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
print(f"miss {aiAim(2)}")
print(recentHits)
print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
print(f"hit {aiAim(0)}")
print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
print(f"hit {aiAim(1)}")
print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
print(f"hit {aiAim(1)}")
print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
print(f"miss {aiAim(1)}")
print(f"Not Sunk {notSunk} prevMiss {prevMiss}")
print()