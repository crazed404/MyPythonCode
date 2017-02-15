def countBirds(file):
    d = {}
    for line in (open(file)):
        temp = line.split(",")
        birdName = temp[0].strip()
        sightings = temp[1].strip()
        d[birdName] = sightings
    return d

def askUser():
    d = countBirds('Birds.txt')
    print('What bird would you like to know about?: '),
    bird = raw_input()
    print ('There has been %s sighting(s) of this bird.' % d[bird])
    
def main():
    countBirds('Birds.txt')
    askUser()   
    
main()