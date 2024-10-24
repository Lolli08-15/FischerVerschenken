import random
freeFields = []
meShootHere = ()

for y in range(10):
        for x in range(10):
            freeFields.append((x, y))

def resetAI():
    global freeFields, meShootHere

    freeFields = []
    meShootHere = ()
    x = 0
    y = 0

    for y in range(10):
        for x in range(10):
            freeFields.append((x, y))


def shootAI(theWhat):
    global freeFields, meShootHere

    dontCare = theWhat

    meShootHere = freeFields[0]
    freeFields.pop(0)

    return meShootHere