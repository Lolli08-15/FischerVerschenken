import random

freeSquares = []            #generate possible squares, to keep track of shots
for i in range(10):
    for j in range(10):
        freeSquares.append([i,j])   


def ai_shoot(response):     #input is whether the last shot missed(0), hit(1) or sunk(2) 
    
    pickedSquare = random.choice(freeSquares)
    aimX, aimY = pickedSquare
    freeSquares.remove(pickedSquare)
    return aimX, aimY       #returns aim coordinates 
