import json

class Stats:

    def __init__(self):
        """
        self.stats["shotStat = 0
        self.stats["hitStat = 0
        self.stats["sunkStat = 0
        self.stats["winStat = 0
        self.stats["gameStat = 0
        self.stats["aiWinStat = {
            "dumAi" : 0,
            "chadGPTAi" : 0,
            "*empty String*" : 0,
            "AIQ" : 0, }
        
        self.stats["fishSunkStat = [0, 0, 0, 0, 0, 0]
        self.stats["progressStat = 0.0
        """
        self.loadStats()

    #lade json
    def loadStats(self):
        file = open('stats.json')
        self.stats = json.load(file)



    # speicher in json
    def saveStats(self):
        json.dumps(self.stats)

    # setzte alle stats zurück
    def resetAllStat(self):
        self.stats["shotStat"] = 0
        self.stats["hitStat"] = 0
        self.stats["sunkStat"] = 0
        self.stats["winStat"] = 0
        self.stats["gameStat"] = 0
        self.stats["aiWinStat"] = []
        self.stats["fishSunkStat"] = []
        self.stats["progressStat"] = 0.0
        # speicher den reset
        self.saveStats()

    # shot stat
    def addShotStat(self):
        self.stats["shotStat"] += 1
        self.saveStats()

    def getShotStat(self):
        return self.stats["shotStat"]

    # hit stat
    def addHitStat(self):
        self.stats["hitStat"] += 1
        self.saveStats()

    def getHitStat(self):
        return self.stats["hitStat"]

    # sunk stat
    def addSunkStat(self):
        self.stats["sunkStat"] += 1
        self.saveStats()

    def getSunkStat(self):
        return self.stats["sunkStat"]

    # win stat
    def addWinStat(self):
        self.stats["winStat"] += 1
        self.saveStats()

    def getWinStat(self):
        return self.stats["winStat"]

    # game stat
    def addGameStat(self):
        self.stats["gameStat"] += 1
        self.saveStats()

    def getGameStat(self):
        return self.stats["gameStat"]

    # ai win stat
    def addAiWinStat(self, aiNumber):
        if aiNumber < len(self.stats["aiWinStat"]) and aiNumber >= 0:
            self.stats["aiWinStat"][aiNumber] += 1
            self.saveStats()

    def getAiWinStat(self, aiNumber):
        if aiNumber < len(self.stats["aiWinStat"]) and aiNumber >= 0:
            return self.stats["aiWinStat"][aiNumber]
        return None
    
    def setProgress(notMe, newNum):
        notMe.stats["progressStat"]=newNum
        notMe.saveStats()
    
    def getProgress(notMe):
        return notMe.stats["progressStat"]
    
    def selfTest(self):
        print("_______________________Stats Test_______________________")
        savestate=self.stats
        
        print(self.stats)
        print("resetAllStats")
        self.resetAllStat()
        print(self.stats)
        
        print("loadStats")
        self.loadStats()
        print(self.stats)
        
        print("addShotStat / getShotStat")
        self.addShotStat()
        print(self.getShotStat())
        
        print("addSunkStat / getSunkStat")
        self.addSunkStat()
        print(self.getSunkStat())
        
        print("addHitkStat / getHitStat")
        self.addHitStat()
        print(self.getHitStat())
        
        print("addWinStat / getWinStat")
        self.addWinStat()
        print(self.getWinStat())
        
        print("addAiWinStat / getAiWinStat (0)")
        self.addAiWinStat(0)
        print(self.getAiWinStat(0))
        
        print("addGameStat / getGameStat")
        self.addGameStat()
        print(self.getGameStat())
        
        print("reset to before Testing")
        self.stats = savestate
        self.saveStats()
        print("_______________________Testing Finsh_______________________")
