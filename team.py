class Team:
    def __init__(self, name, score, outcome):
        self.name = str(name)
        self.score = float(score)
        self.outcome = float(outcome)

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def getOutcome(self):
        # this will be 1, 0, or 0.5
        return self.outcome

    def gameOutcomeAsString(self):
        if(self.outcome == 1):
            return "won"
        elif(self.outcome == 0):
            return "lost"
        else:
            return "tied"

    def printInfo(self):
        print(f"{self.name} scored {self.score} and {self.gameOutcomeAsString()}")




