import random
import time
    
def getFrankNumbers():
    #list so I can add up hotdogs eaten
    hotDogsEaten = [0, 0, 0]
    while hotDogsEaten[0] < 50 and hotDogsEaten[1] < 50 and hotDogsEaten[2] < 50:
        #makes random ints to add up
        tomDogs = random.randrange(1, 6)
        sallyDogs = random.randrange(1, 6)
        fredDogs = random.randrange(1, 6)
        #adds up hotdogs eaten each turn
        hotDogsEaten[0] = hotDogsEaten[0] + tomDogs
        hotDogsEaten[1] = hotDogsEaten[1] + sallyDogs
        hotDogsEaten[2] = hotDogsEaten[2] + fredDogs
        print('Tom has eaten %s franks.' % hotDogsEaten[0])
        print('Sally has eaten %s franks.' % hotDogsEaten[1])
        print('Fred has eaten %s franks.' % hotDogsEaten[2])
        print('\nChomp chomp chompity\n')
        time.sleep(1)
    #compares the index of hotdogs eaten to find the max
    #so I can return it to another function that decides the winner
    global winner
    winner = hotDogsEaten.index(max(hotDogsEaten))
    if winner == 0:
        winner = 'Tom'
    elif winner == 1:
        winner = 'Sally'
    elif winner == 2:
        winner = 'Fred'
    
def getWinner():
    print('Who do you think will be the first to eat 50 franks?!? (Tom, Sally, Fred)'),
    userGuess = raw_input() 
    print('\nRead...Set...Go!')
    print
    getFrankNumbers()
    if userGuess == winner:
        print('Congrats, you guessed correctly!\n')
    else:
        print('Perhaps hot dog betting is not your thing.\n')

def main():
    while True:
        getWinner()
        print('Would you like to play again (Type anything to continue, or type "No")'),
        keepPlaying = raw_input()
        print
        if keepPlaying == 'No'or keepPlaying == 'NO' or keepPlaying == 'no':
            break
#I spent a decent amount of time on this...
#God knows if I did this right
main()
    