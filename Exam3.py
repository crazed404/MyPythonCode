import random

def playGame():
    choices = ['bird', 'dog','snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck','crab']
    r = random.randrange(0,8)
    choices.append(choices[r])
    random.shuffle(choices)
    global count
    count = 1
    
    while True:
      print('Pick the first card to turn over (0 - 9)'),
      card1 = int(raw_input())
      while card1 < 0 or card1 > 9:
        print('Please enter a number between 0 and 9'),
        card1 = int(raw_input())
      
      print('Pick the second card to turn over (0 - 9)'),
      card2 = int(raw_input())
      while card2 < 0 or card2 > 9 or card1 == card2:
         print('Please enter a number between 0 and 9 or a different card than the first'),
         card2 = int(raw_input())
      print('Card %s is a %s' % (card1, choices[card1])) 
      print('Card %s is a %s' % (card2, choices[card2])) 
      
      count += 1
      if choices[card1] == choices[card2]:
        break

def printOut():
    print('\nCongrats you picked the matching cards!!!!!!!!!!!!!!!!!11!!!!!!!!!')
    print('It took you %s tries to match them' % count)
    
def main():
    playGame()
    printOut()
main()