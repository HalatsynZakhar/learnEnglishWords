import random

class Word:

    def __init__(self, currentLvl, currentStepInLvl, stepLvl, status, english, russian, type):
        self.currentLvl = currentLvl
        self.currentStepInLvl = currentStepInLvl
        self.stepLvl = stepLvl
        self.status = status
        self.english = english.lower()
        self.all_level = len(english)
        self.russian = russian.lower()
        self.type = type

    def getStatus(self):
        return self.status
    def addStatus(self, status):
        if status in ["не изучено", "на изучении", "изучено"]:
            self.status = status

    def addStep(self):
        self.addStatus("на изучении")
        if self.currentStepInLvl < self.stepLvl:
            self.currentStepInLvl += 1
        if self.currentStepInLvl == self.stepLvl:
            self.addLvl()

    def addLvl(self):
        if self.currentLvl < self.all_level:
            self.currentStepInLvl = 0
            self.currentLvl += 1
        elif self.currentLvl == self.all_level:
            self.addStatus("изучено")
            print("изучено")

    def getAllLevel(self):
        return self.all_level

    def getEnglish(self):
        return self.english

    def getEnglishTraining(self):
        if self.status == "изучено":
            return "?"

        if self.currentLvl == 0:
            return self.getEnglish()

        res = ""
        index = random.sample(range(self.all_level), self.currentLvl)
        for i in range(self.all_level):
            if i in index:
                res += "_"
            else:
                res += self.getEnglish()[i]
        return res

    def setEnglish(self, english):
        self.english = english

    def getRussian(self):
        return self.russian

    def setRussian(self, russian):
        self.russian = russian

    def getCurrentLvl(self):
        return self.currentLvl

    def setCurrentLvl(self, currentLvl):
        self.currentLvl = currentLvl

    def getCurrentStepInLvl(self):
        return self.currentStepInLvl

    def setCurrentStepInLvl(self, currentStepInLvl):
        self.currentStepInLvl = currentStepInLvl

    def getStepLvl(self):
        return self.stepLvl

    def setStepLvl(self, stepLvl):
        self.stepLvl = stepLvl
