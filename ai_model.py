import random


free_squares = []
shots = []
recent_hits = []

attacking_direction = -1
attacking_steps = 0


for x in range(10):
    for y in range(10):
        free_squares.append((x,y))



ai_state = "idle"
last_shot = ()

def resetAI():
    global free_squares, shots, recent_hits
    global attacking_direction, attacking_steps, ai_state, last_shot

    free_squares = []
    shots = []
    recent_hits = []

    attacking_direction = -1
    attacking_steps = 0


    for x in range(10):
        for y in range(10):
            free_squares.append((x,y))



    ai_state = "idle"
    last_shot = ()


def shootAI(response):
    global free_squares, shots, recent_hits
    global attacking_direction, attacking_steps, ai_state, last_shot

    if response > 0:
        recent_hits.append(last_shot)
    
    if len(recent_hits) > 0:
        ai_state = "attack"
    if len(recent_hits) == 0:
        ai_state = "idle"
    
    if response == 2:
        recent_hits = []
        ai_state = "idle"
    
    if ai_state == "attack":
        if response == 0:
            attacking_steps = 0
            attacking_direction += 1
        ispossible = False
        while not ispossible:
            if attacking_direction == 4:
                attacking_direction = 0
                attacking_steps = 0
                recent_hits.pop(0)

                if len(recent_hits) == 0:
                    ai_state = "idle"
                    ispossible = True
            if not ispossible:

                attacking_steps += 1
                
                x_pos = recent_hits[0][0]
                y_pos = recent_hits[0][1]
                if attacking_direction == 0:
                    x_pos -= attacking_steps
                if attacking_direction == 1:
                    x_pos += attacking_steps
                if attacking_direction == 2:
                    y_pos -= attacking_steps
                if attacking_direction == 3:
                    y_pos += attacking_steps
                if (x_pos >= 0 and y_pos >= 0 and
                    x_pos < 10 and y_pos < 10):
                    position = (x_pos, y_pos)
                    if free_squares.count(position) > 0:
                        last_shot = position
                        free_squares.remove(last_shot)
                        shots.append(last_shot)
                        ispossible = True

                        return last_shot
                    else:
                        attacking_steps = 0
                        attacking_direction += 1
                else:
                    attacking_steps = 0
                    attacking_direction += 1

    
    if ai_state == "idle":
        attacking_direction = 0
        attacking_steps = 0

        last_shot = random.choice(free_squares)
        free_squares.remove(last_shot)
        shots.append(last_shot)

        return last_shot