import bot
import player



def showHowToPlay():
    print(' enter start to play game\n enter exit to exit program\n enter stat to see stat')

def startGame():
    userHandInput = input("Enter only rock or paper or scissors : ")
    player.setHand(player, userHandInput)
    playerHand = player.getHand(player)
    botHand = bot.getHand()
    compareBotAndPlayerHand(botHand, playerHand)


def compareBotAndPlayerHand(botHand, playerHand):
    if(botHand == playerHand):
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Draw')
    elif(botHand == 'paper' and playerHand == 'rock'):
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('bot won')
    elif (playerHand == 'paper' and botHand == 'rock'):
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('player won')
    elif (playerHand == 'paper' and botHand == 'scissors'):
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('bot won')
    elif (botHand == 'paper' and playerHand == 'scissors'):
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('player won')
    elif (playerHand == 'scissors' and botHand == 'rock'):
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('bot won')
    elif (playerHand == 'rock' and botHand == 'scissors'):
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('player won')
    elif (playerHand == 'exit'):
        showHowToPlay()
    else:
        print('error')


def showStat():
    print('test')



showHowToPlay()
while True:
    userChoice = input('Enter start to start the game : ')
    if userChoice == 'start':
        startGame()
    if userChoice == 'stat':
        showStat()
    if userChoice == 'exit':
        break

