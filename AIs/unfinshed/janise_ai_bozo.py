import random


def resetAI():
    global freeSquares
    
    freeSquares = set()             #generate possible squares, to keep track of shots
    for x in range(10):
        for y in range(10):
            freeSquares.add((x,y))     
        
def shootAI(response):
    if not freeSquares:
        freeSquares.add((0,0))
    return aiShoot(freeSquares)                            #fire 
        
#the main function
def aiShoot(aim):
    global pickedSquare   
    pickedSquare = random.choice(list(aim))     #pick a square based on the choice
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY     #returns aim coordinates