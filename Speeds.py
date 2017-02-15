
def readData(file):
    list = []
    file = open(file, 'r') 
    for item in file:
        item = item.strip()
        list.append(int(item))
    return list    
    
notRush = readData('data-not-rush.txt')
rush = readData('data-rush.txt')

def getAverage(file):
    average = sum(file) / float(len(file))
    return average
    
avgNotRush = getAverage(notRush)
avgRush = getAverage(rush)


def countSpeeders(file):
    fine = 0
    speeders = 0
    for i in range(0,len(file)):
        if file[i] > 69:
            if file == rush:
             fine = 150 + fine
             speeders = fine / 150
            if file == notRush:
             fine = 100 + fine
             speeders = fine / 100
             #took a while to figure out how not to use
             #two functions for this
    return speeders, fine


speedersNotRush =countSpeeders(notRush)
speedersRush= countSpeeders(rush)


def main():
    print('The average speed during non rush hour is %.2f.') % avgNotRush
    print('The average speed during rush hour is %.2f.') % avgRush
    print('There were %s speeders during non rush hour fined for $%s' %speedersNotRush)
    print('There were %s speeders during rush hour fined for $%s' % speedersRush) 

main()
