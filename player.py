
playerHand = ''
posibleHand = ["rock", "paper", "scissors","exit"]

def setHand(self, inputData):
    self.playerHand = inputData


def getHand(self):
    if self.playerHand not in posibleHand:
        return 'error'
    else :
        return self.playerHand
