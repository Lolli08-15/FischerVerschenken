from place import place
from shoot import shoot
from aiPlace import aiPlace
from detectWin import detectWin

import random

import dum_ai
import gpt_ai
import janise_ai
import janise_ai_dirty
import kilian_ai
import aiShootQ
import kilian_ai_hard
import impossible_ai



class Player:
    def __init__(self):
        self.fishes = []
        self.shotList = []
        self.sunkenFish = 0
        
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
        self.blockList = []
    

    def getPlayerFish(self, player):
        """returns the FishObjekts of the prompted 
        Player(Huaman or Ai) as an Array of Pointers"""
        if player == "player1":
            return self.player1.fishes
        elif player == "ai":
            return self.ai.fishes
        return False
    

    def placeFish(self, posXY, direction, length):
        return place(self.player1, posXY, direction, length, self.blockList)


    def placeAiFish(self, preset):
        aiPlace(self.ai, preset, self.blockList)
    

    def removeFish(self, posXY):
        return self.player1.removeFish(posXY)
    

    def getSunkenFish(self, player):
        if player == "player1":
            return self.player1.sunkenFish
        elif player == "ai":
            return self.ai.sunkenFish
        return False


    def reset(self,preset):
        self.player1 = Player()
        self.ai = Player()
        self.ai_last_shot = 0
        self.blockList = self.setBlocklist(preset)
        self.player1.shotList += self.blockList
        self.ai.shotList += self.blockList

        if self.selected_ai == 0:
            dum_ai.resetAI()
        if self.selected_ai == 1:
            gpt_ai.resetAI()
        if self.selected_ai == 2:
            kilian_ai.resetAI()
        if self.selected_ai == 3:
            aiShootQ.resetAI()
        if self.selected_ai == 4:
            kilian_ai_hard.resetAI()
        if self.selected_ai == 5:
            impossible_ai.resetAI()
        if self.selected_ai == 6:
            janise_ai.resetAI()
        if self.selected_ai == 7:
            janise_ai_dirty.resetAI()

    
    def playerShoot(self, posXY):
        return shoot(self.player1, self.ai, posXY)
    

    def aiShoot(self):
        coords = (0, 0)
        
        if self.selected_ai == 0:
            coords = dum_ai.shootAI(self.ai_last_shot)
        if self.selected_ai == 1:
            coords = gpt_ai.shootAI(self.ai_last_shot)
        if self.selected_ai == 2:
            coords = kilian_ai.shootAI(self.ai_last_shot)
        if self.selected_ai == 3:
            coords = aiShootQ.shootAI(self.ai_last_shot)
        if self.selected_ai == 4:
            coords = kilian_ai_hard.shootAI(self.ai_last_shot)
        if self.selected_ai == 5:
            coords = impossible_ai.shootAI(self.player1)
        if self.selected_ai == 6:
            coords = janise_ai.shootAI(self.ai_last_shot)
        if self.selected_ai == 7:
            coords = janise_ai_dirty.shootAI(self.ai_last_shot)
            
        if not coords in self.blockList:
            response = shoot(self.ai, self.player1, coords)

            if response == "hit": self.ai_last_shot = 1
            elif response == "sunk": self.ai_last_shot = 2
            else: self.ai_last_shot = 0
            return self.ai_last_shot
        else:
            self.ai_last_shot = 0
            print("it Works...")
            self.aiShoot()
    

    def aiModelReset(self, ai):
        if ai == 0:
            dum_ai.resetAI()
        if ai == 1:
            gpt_ai.resetAI()
        if ai == 2:
            kilian_ai.resetAI()
        if ai == 3:
            aiShootQ.resetAI()
        if ai == 4:
            kilian_ai_hard.resetAI()
        if ai == 5:
            impossible_ai.resetAI()
        if ai == 6:
            janise_ai.resetAI()
        if ai == 7:
            janise_ai_dirty.resetAI()
    
    def aiModelShoot(self, ai, ai_last_shot):
        coords = (0, 0)

        if ai == 0:
            coords = dum_ai.shootAI(ai_last_shot)
        if ai == 1:
            coords = gpt_ai.shootAI(ai_last_shot)
        if ai == 2:
            coords = kilian_ai.shootAI(ai_last_shot)
        if ai == 3:
            coords = aiShootQ.shootAI(ai_last_shot)
        if ai == 4:
            coords = kilian_ai_hard.shootAI(ai_last_shot)
        if ai == 5:
            coords = impossible_ai.shootAI(self.player1)
        if ai == 6:
            coords = janise_ai.shootAI(ai_last_shot)
        if ai == 7:
            coords = janise_ai_dirty.shootAI(ai_last_shot)
        
        return coords
    

    def getSunkenFish(self, player):
        if player == "player1":
            return self.player1.sunkenFish
        elif player == "ai":
            return self.ai.sunkenFish
        return False
    

    def getShotList(self, player):
        if player == "player1":
            return self.player1.shotList
        elif player == "ai":
            return self.ai.shotList
        return False
    

    def detectWin(self):
        aiWin = detectWin(self.player1)
        playerWin = detectWin(self.ai)
        if playerWin:
            return "player"
        if aiWin:
            return "ai"
        return False
    

    def setAI(self, AI):
        self.selected_ai = AI
    
    def setBlocklist(self,preset):
        if preset == 1:
            blockNr = random.randint(0,5)
        elif preset == 2:
            blockNr = random.randint(3,8)
        elif preset == 3:
            blockNr = random.randint(8,18)
        elif preset == 4:
            blockNr = random.randint(4,10)
        elif preset == 5:
            blockNr = random.randint(3,15)
        elif preset == 6:
            blockNr = random.randint(2,12)
        else:
            blockNr = 0
        bList=[]
        for i in range(blockNr):
            xCord = random.randint(0,9)
            yCord = random.randint(0,9)
            pos =(xCord,yCord)
            bList.append([pos,"block"])
        return(bList)


    

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
