import json

class Stats:

    def __init__(self):
        self.shotStat = 0
        self.hitStat = 0
        self.sunkStat = 0
        self.winStat = 0
        self.gameStat = 0
        """self.aiWinStat = {
            "dumAi" = 0,
            "chadGPTAi" = 0,
            "" = 0,
            "AIQ" = 0,

        }"""
        self.fishSunkStat = [0, 0, 0, 0, 0, 0]
        self.progressStat = 0.0
        self.loadStats()

    #lade json
    def loadStats():
        pass



    # speicher in json
    def saveStats(self):
        json.dumps(self.stats)

    # setzte alle stats zurück
    def resetAllStat(self):
        self.shotStat = 0
        self.hitStat = 0
        self.sunkStat = 0
        self.winStat = 0
        self.gameStat = 0
        self.aiWinStat = []
        self.fishSunkStat = []
        self.progressStat = 0.0
        # speicher den reset
        self.saveStats()

    # shot stat
    def addShotStat(self):
        self.shotStat += 1

    def getShotStat(self):
        return self.shotStat

    # hit stat
    def addHitStat(self):
        self.hitStat += 1

    def getHitStat(self):
        return self.hitStat

    # sunk stat
    def addSunkStat(self):
        self.sunkStat += 1

    def getSunkStat(self):
        return self.unkStat

    # win stat
    def addWinStat(self):
        self.winStat += 1

    def getWinStat(self):
        return self.winStat

    # game stat
    def addGameStat(self):
        self.gameStat += 1

    def getGameStat(self):
        return self.gameStat

    # ai win stat
    def addAiWinStat(self, aiNumber):
        if aiNumber < len(self.aiWinStat) and aiNumber >= 0:
            self.aiWinStat[aiNumber] += 1

    def getAiWinStat(self, aiNumber):
        if aiNumber < len(self.aiWinStat) and aiNumber >= 0:
            return self.aiWinStat[aiNumber]
        return None



stats = Stats()

stats.resetAllStat()

stats.addHitStat()

print("current hits: ", stats.getHitStat)