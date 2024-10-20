from place import place
from shoot import shoot
from aiPlace import aiPlace
from ai import aiAim



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
                
    def addShot(self, posXY, what):
        self.shotList.append([posXY, what])

    def getSunkenFish(self):
        count = 0
        for shot in self.shotList:
            if "sunk" in shot:
                count += 1
        return count
    
    def showOff(self):
        """A test function: prints every placed fish and it's occupied spaces"""
        for fish in self.fishes:
            print(f"Fisch on: ({fish.posX}|{fish.posY}) spannig: {fish.length} fields in direction: {fish.direction}")
            print(fish.occupied)

 


class Game:
    def __init__(self):
        self.player1 = Player()
        self.ai = Player()
        self.ai_last_shot = 0
    

    def getPlayerFish(self, player):
        """returns the FishObjekts of the prompted 
        Player(Huaman or Ai) as an Array of Pointers"""
        if player == "player1":
            return self.player1.fishes
        elif player == "ai":
            return self.ai.fishes
        return False
    

    def placeFish(self,posXY,direction,length):
        return place(self.player1,posXY,direction,length)


    def placeAiFish(self):
        # TO DO
        aiPlace(self.ai)
        #place(self.ai, (0, 0), 1, 2)
        #place(self.ai, (0, 1), 1, 3)
        #place(self.ai, (0, 2), 1, 3)
        #place(self.ai, (0, 3), 1, 4)
        #place(self.ai, (0, 4), 1, 5)
    

    def removeFish(self, posXY):
        return self.player1.removeFish(posXY)
    

    def getSunkenFish(self, player):
        if player == "player1":
            return self.player1.getSunkenFish()
        elif player == "ai":
            return self.ai.getSunkenFish()
        return False


    def reset(self):
        self.player1 = Player()
        self.ai = Player()
        self.ai_last_shot = 0

    
    def playerShoot(self, posXY):
        return shoot(self.player1, self.ai, posXY)
    

    def aiShoot(self):
        coords = aiAim(self.ai_last_shot)
        response = shoot(self.ai, self.player1, coords)

        if response == "hit": self.ai_last_shot = 1
        elif response == "sunk": self.ai_last_shot = 2
        else: self.ai_last_shot = 0
    

    def getSunkenFish(self, player):
        if player == "player1":
            return self.player1.getSunkenFish()
        elif player == "ai":
            return self.ai.getSunkenFish()
        return False
    

    def getShotList(self, player):
        if player == "player1":
            return self.player1.shotList
        elif player == "ai":
            return self.ai.shotList
        return False


    def reset(self):
        self.player1 = Player()
        self.ai = Player()

    

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
        