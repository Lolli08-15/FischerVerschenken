import random

meShootHere = ()

dMode = random.choice([True, False, False, False])

if dMode:
    freeFields = [(5,1),(6,2),(6,3),(6,4),(6,5),(7,5),(8,6),(8,7),(7,8),(6,8),(5,7),(4,7),(3,8),(2,8),(1,7),(1,6),(2,5),(3,5),(3,4),(3,3),(3,2),(4,1)]
else:
    freeFields = []



for y in range(10):
    for x in range(10):
        freeFields.append((x, y))


def resetAI():
    global freeFields, meShootHere

    dMode = random.choice([True, False, False, False])

    if dMode:
        freeFields = [(5,1),(6,2),(6,3),(6,4),(6,5),(7,5),(8,6),(8,7),(7,8),(6,8),(5,7),(4,7),(3,8),(2,8),(1,7),(1,6),(2,5),(3,5),(3,4),(3,3),(3,2),(4,1)]
    else:
        freeFields = []

    meShootHere = ()
    x = 0
    y = 0

    for y in range(10):
        for x in range(10):
            tryXY = (x, y)
            if tryXY not in freeFields:
                freeFields.append((x, y))
    
    random.choice([True, False, False, False])


def shootAI(shotInformation):
    global freeFields, meShootHere

    dontCare = shotInformation

    meShootHere = freeFields[0]
    freeFields.pop(0)

    return meShootHere