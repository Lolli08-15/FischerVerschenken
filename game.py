from place import place
from shoot import shoot


class Player:
    def __init__(self):
        self.fishes = []
        self.shotList = []
        
    def addFish(self, fish):
        self.fishes.append(fish)
        
    def removeFish(self,posXY):
        for fish in self.fishes:
            #print(fish.occupied)
            if posXY in fish.occupied:
                length = fish.length
                self.fishes.remove(fish)
                return length
        return 0
                
    
    def addShot(self,posXY,what):
        self.shotList.append([posXY,what])
    
    def showOff(self):
        """A test function: prints every placed fish and it's occupied spaces"""
        for fish in self.fishes:
            print(f"Fisch on: ({fish.posX}|{fish.posY}) spannig: {fish.length} fields in direction: {fish.direction}")
            print(fish.occupied)

 


class Game:
    def __init__(self):
        self.player1 = Player()
        self.ai = Player()
    

    def getPlayerFish(self, player):
        """returns the FishObjekts of the prompted 
        Player(Huaman or Ai) as an Array of Pointers"""
        if player == "player1":
            return self.player1.fishes
        elif player == "ai":
            return self.player1.fishes
        return False
    

    def placeFish(self,posXY,direction,length):
        return place(self.player1,posXY,direction,length)


    def placeAiFish(self, posXY, direction, length):
        possible = place(self.ai,posXY,direction,length)
        if possible == False: return False
    

    def removeFish(self, posXY):
        return self.player1.removeFish(posXY)

    

"""_____________________Test Start_____________________"""
if __name__ == "__main__":
    game = Game()
    trash = game.player1.removeFish((1,0))
    print(trash)
    game.player1.showOff()
    game.placeFish((0, 0), 1, 4)

    print(shoot(game.player1, (0, 0)))
"""_____________________Test End______________________"""

"""
    0 1 2 3 4 5 6 7 8 9

0   # # # 0 0 0 0 0 0 0
1   # # # # 0 0 0 0 0 0
2   0 0 0 0 0 0 0 # # # #
3   0 0 0 0 0 0 0 0 0 0
4   0 0 0 0 0 0 0 0 0 0
5   0 # 0 0 0 # 0 0 0 0
6   0 # 0 0 0 # 0 0 0 0
7   0 # 0 0 0 0 0 0 0 0
8   0 # 0 0 0 0 0 0 0 0
9   0 # 0 0 0 0 0 0 0 0

"""
        