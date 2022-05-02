import random

# def __init__(self):
#     posibleHand = ["rock", "paper", "scissors"]
#     self.currentHand = random.choice(posibleHand)

def getHand():
    posibleHand = ["rock", "paper", "scissors"]
    currentHand = random.choice(posibleHand)
    return currentHand
