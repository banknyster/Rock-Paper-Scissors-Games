import random

def getHand():
    posibleHand = ["rock", "paper", "scissors"]
    currentHand = random.choice(posibleHand)
    return currentHand
