import bot
import player

# index 0 = rock, index 1 = paper, index2 = scissors
playerStat = [0, 0, 0]
botStat = [0, 0, 0]

playerWinCount = 0
botWinCount = 0
drawCount = 0


def showHowToPlay():
    print(' enter start to play game\n enter exit to exit program\n enter stat to see stat')


def startGame():
    userHandInput = input("Enter only rock or paper or scissors : ")
    player.setHand(player, userHandInput)
    playerHand = player.getHand(player)
    botHand = bot.getHand()
    compareBotAndPlayerHand(botHand, playerHand)


def compareBotAndPlayerHand(botHand, playerHand):
    global botWinCount, playerWinCount, drawCount

    if(botHand == playerHand):
        if(botHand == 'rock'):
            botStat[0] += 1
            playerStat[0] += 1
        elif(botHand == 'paper'):
            botStat[1] += 1
            playerStat[1] += 1
        elif(botHand == 'scissors'):
            botStat[2] += 1
            playerStat[2] += 1
        drawCount += 1
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Draw')
    elif(botHand == 'paper' and playerHand == 'rock'):
        botStat[1] += 1
        playerStat[0] += 1
        botWinCount += 1
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Bot won')
    elif (playerHand == 'paper' and botHand == 'rock'):
        botStat[0] += 1
        playerStat[1] += 1
        playerWinCount += 1
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Player won')
    elif (playerHand == 'paper' and botHand == 'scissors'):
        botStat[2] += 1
        playerStat[1] += 1
        botWinCount += 1
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Bot won')
    elif (botHand == 'paper' and playerHand == 'scissors'):
        botStat[1] += 1
        playerStat[2] += 1
        playerWinCount += 1
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Player won')
    elif (playerHand == 'scissors' and botHand == 'rock'):
        botStat[0] += 1
        playerStat[2] += 1
        botWinCount += 1
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Bot won')
    elif (playerHand == 'rock' and botHand == 'scissors'):
        botStat[2] += 1
        playerStat[0] += 1
        playerWinCount += 1
        print('Player hand = ' + playerHand)
        print('Bot hand = ' + botHand)
        print('Player won')
    elif (playerHand == 'exit'):
        showHowToPlay()
    elif (playerHand == 'stat'):
        showStat()
    else:
        print('error')


def showStat():
    print('Player Won ', playerWinCount, ' times')
    print('Player choose Rock ', playerStat[0], ' times')
    print('Player choose Paper ', playerStat[1], ' times')
    print('Player choose Scissors ', playerStat[2], ' times\n')
    print('Bot Won ', botWinCount, ' times')
    print('Bot choose Rock ', botStat[0], ' times')
    print('Bot choose Paper ', botStat[1], ' times')
    print('Bot choose Scissors ', botStat[2], ' times\n')
    print('Drawn ', drawCount, ' times')


showHowToPlay()
while True:
    userChoice = input('Enter option : ')
    if userChoice == 'start':
        startGame()
    if userChoice == 'stat':
        showStat()
    if userChoice == 'exit':
        break
