from place import place
class Player:
    def __init__(self):
        self.fishes = []
        
    def addFish(self, fish):
        self.fishes.append(fish)
    
    def showOff(self):
        for fish in self.fishes:
            print(f"Fisch on: ({fish.posX}|{fish.posY}) spannig: {fish.length} fields in direction: {fish.direction}")

class Fish:
    def __init__(self, posX, posY, direction, length):
        self.posX = posX
        self.posY = posY
        self.direction = direction
        self.length = length
        self.hits = 0
 
if __name__ == "__main__":
    player1 = Player()
    ki = Player()
    goal = [[0,0,1,3],[7,2,1,4],[1,9,0,5],[5,5,2,2],[9,9,3,3],[5,9,0,4]]
    for aim in goal:
        possible = place(player1,aim[0],aim[1],aim[2],aim[3])
        if possible == False:
            print("Fish not placable")
        else:
            print("Fish placed")
    player1.showOff()



"""
    0 1 2 3 4 5 6 7 8 9

0   # # # 0 0 0 0 0 0 0
1   0 0 0 0 0 0 0 0 0 0
2   0 0 0 0 0 0 0 # # # #
3   0 0 0 0 0 0 0 0 0 0
4   0 0 0 0 0 0 0 0 0 0
5   0 # 0 0 0 # 0 0 0 0
6   0 # 0 0 0 # 0 0 0 0
7   0 # 0 0 0 0 0 0 0 0
8   0 # 0 0 0 0 0 0 0 0
9   0 # 0 0 0 0 0 0 0 0

"""
        