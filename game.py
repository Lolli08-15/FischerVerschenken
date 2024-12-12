from place import place
from shoot import shoot
from aiPlace import aiPlace
from detectWinFile import detectWin as detectWin_extern

import random

import statistics_file

import AIs.dum_ai
import AIs.gpt_ai
import AIs.janise_ai
import AIs.janise_ai_dirty
import AIs.kilian_ai
import AIs.aiShootQ
import AIs.kilian_ai_hard
import AIs.impossible_ai



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
        self.statBlock = statistics_file.Stats()
        self.aiMode = False
    

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
            AIs.dum_ai.resetAI() # Dummheit persönlich
        if self.selected_ai == 1:
            AIs.gpt_ai.resetAI() # Chad GPT
        if self.selected_ai == 2:
            AIs.kilian_ai.resetAI() # Medium
        if self.selected_ai == 3:
            AIs.aiShootQ.resetAI() # Hai AIQ
        if self.selected_ai == 4:
            AIs.kilian_ai_hard.resetAI() # Hard wie Hartmut
        if self.selected_ai == 5:
            AIs.impossible_ai.resetAI() # Impossible
        if self.selected_ai == 6:
            AIs.janise_ai.resetAI() # Mr. Chunky
        if self.selected_ai == 7:
            AIs.janise_ai_dirty.resetAI() # Dirty Dan

    
    def playerShoot(self, posXY):
        self.statBlock.addShotStat()
        answer = shoot(self.player1, self.ai, posXY)
        if answer == "hit":
            self.statBlock.addHitStat()
        if answer == "sunk":
            self.statBlock.addHitStat()
            self.statBlock.addSunkStat()
        return answer
    

    def aiShoot(self):
        coords = (0, 0)
        
        if self.selected_ai == 0:
            coords = AIs.dum_ai.shootAI(self.ai_last_shot) # Dummheit persönlich
        if self.selected_ai == 1:
            coords = AIs.gpt_ai.shootAI(self.ai_last_shot) # Chad GPT
        if self.selected_ai == 2:
            coords = AIs.kilian_ai.shootAI(self.ai_last_shot) # Medium
        if self.selected_ai == 3:
            coords = AIs.aiShootQ.shootAI(self.ai_last_shot) # Hai AIQ
        if self.selected_ai == 4:
            coords = AIs.kilian_ai_hard.shootAI(self.ai_last_shot) # Hard wie Hartmut
        if self.selected_ai == 5:
            coords = AIs.impossible_ai.shootAI(self.player1) # Impossible
        if self.selected_ai == 6:
            coords = AIs.janise_ai.shootAI(self.ai_last_shot) # Mr. Chunky
        if self.selected_ai == 7:
            coords = AIs.janise_ai_dirty.shootAI(self.ai_last_shot) # Dirty Dan
            
        if not coords in self.blockList:
            response = shoot(self.ai, self.player1, coords)

            if response == "hit":
                self.ai_last_shot = 1
            elif response == "sunk": self.ai_last_shot = 2
            else: self.ai_last_shot = 0
            return (self.ai_last_shot, coords)
        else:
            self.ai_last_shot = 0
            self.aiShoot()
    

    def aiModelReset(self, ai):
        if ai == 0:
            AIs.dum_ai.resetAI() # Dummheit persönlich
        if ai == 1:
            AIs.gpt_ai.resetAI() # Chad GPT
        if ai == 2:
            AIs.kilian_ai.resetAI() # Medium
        if ai == 3:
            AIs.aiShootQ.resetAI() # Hai AIQ
        if ai == 4:
            AIs.kilian_ai_hard.resetAI() # Hard wie Hartmut
        if ai == 5:
            AIs.impossible_ai.resetAI() # Impossible
        if ai == 6:
            AIs.janise_ai.resetAI() # Mr. Chunky
        if ai == 7:
            AIs.janise_ai_dirty.resetAI() # Dirty Dan
    
    def aiModelShoot(self, ai, ai_last_shot):
        coords = (0, 0)

        if ai == 0:
            coords = AIs.dum_ai.shootAI(ai_last_shot) # Dummheit persönlich
        if ai == 1:
            coords = AIs.gpt_ai.shootAI(ai_last_shot) # Chad GPT
        if ai == 2:
            coords = AIs.kilian_ai.shootAI(ai_last_shot) # Medium
        if ai == 3:
            coords = AIs.aiShootQ.shootAI(ai_last_shot) # Hai AIQ
        if ai == 4:
            coords = AIs.kilian_ai_hard.shootAI(ai_last_shot) # Hard wie Hartmut
        if ai == 5:
            coords = AIs.impossible_ai.shootAI(self.ai) # Impossible
        if ai == 6:
            coords = AIs.janise_ai.shootAI(ai_last_shot) # Mr. Chunky
        if ai == 7:
            coords = AIs.janise_ai_dirty.shootAI(ai_last_shot) # Dirty Dan
        if not coords in self.blockList:
            return coords
        else:
            self.aiModelShoot(ai,0)
    

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
        aiWin = detectWin_extern(self.player1)
        playerWin = detectWin_extern(self.ai)
        if aiWin:
            if not self.aiMode:
                self.statBlock.addGameStat()
            return "ai"
        if playerWin:
            if not self.aiMode:
                self.statBlock.addGameStat()
                self.statBlock.addWinStat()
                self.statBlock.addAiWinStat(self.selected_ai)
                self.progression()
            return "player"
        return False
    
    def progression(self):
        if self.statBlock.stats["progressStat"] < 3:
            if self.selected_ai == 1 or self.selected_ai == 2:
                if not self.statBlock.stats["progressStat"] > 1:
                    self.statBlock.setProgress(1)
            elif self.selected_ai == 6 or self.selected_ai == 4:
                if not self.statBlock.stats["progressStat"] > 2:
                    self.statBlock.setProgress(2)
            elif self.selected_ai == 3 or self.selected_ai == 7:
                    self.statBlock.setProgress(3)
                    

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
            blockNr = 7
        elif preset == 6:
            blockNr = random.randint(2,12)
        else:
            blockNr = 0
        bList=[]
        for i in range(blockNr):
            xCord = random.randint(0,9)
            yCord = random.randint(0,9)
            pos =(xCord,yCord)
            if not [pos,"block"] in bList:
                bList.append([pos,"block"])
        return(bList)
    


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
