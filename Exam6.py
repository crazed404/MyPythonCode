#two functions for getting lists
def getSuspects():
    suspects = ['Miss Scarlett', 'Col Mustard', 'Mr Green']
    return suspects
    
def getWeapons():
      weapons = ['Candlestick', 'Wrench', 'Pipe']
      return weapons
      
def eliminateChoices(suspects, weapons):
    possibilities = len(suspects) * len(weapons)
    print (str(possibilities) + ' possibilities left')
    
    #eliminates what the user enters
    while possibilities != 1:
        print('Is the clue about a weapon or suspect (w or s) '),
        userInput = raw_input()
        
        if userInput == 's':
            print('Enter the weapon that was not used ' + str(suspects)),
            userSuspect = raw_input()
            userSuspect = userSuspect.lower()
            suspects = [i.lower() for i in suspects]
            suspects.remove(userSuspect)
            possibilities = len(suspects) * len(weapons)
            print (str(possibilities) + ' possibilities left')
        
        if userInput == 'w':
            print('Enter the weapon that was not used ' + str(weapons)),
            userWeapon = raw_input()
            userWeapon = userWeapon.lower()
            weapons = [i.lower() for i in weapons]
            weapons.remove(userWeapon)
            possibilities = len(suspects) * len(weapons)
            print (str(possibilities) + ' possibilities left')
    
    print('It must be ' + str(suspects) +' with the' + str(weapons) + '.')

def main():
    eliminateChoices(getSuspects(), getWeapons())
main()