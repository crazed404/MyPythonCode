def openFile(file):
    d = {}
    for line in (open(file)):
        temp = line.split(",")
        name = temp[0].strip()
        time = temp[1].strip()
        d[name] = time
    return d

def getTime():
    d = openFile('timings.txt')

    #finds how fast you are    
    print('Cube head (0 - 9.99):')
    for k in d.keys():
      if float(d[k]) <= 9.99:
         print k 
    print('\nSquare Master (10 - 19.99):')
    for k in d.keys():
       if float(d[k]) <= 19.99 and float(d[k]) > 9.99:
            print k
    print('\nAdvanced Twister (20 - 29.99):')
    for k in d.keys():         
        if float(d[k]) <= 29.99 and float(d[k]) > 19.99:
            print k
    print('\nIntermediate Turner (30 - 39.99):')
    for k in d.keys(): 
        if float(d[k]) <= 39.99 and float(d[k]) > 29.99:
            print k
    print('\nAverage Mover (40 - 59.99):')
    for k in d.keys():  
        if float(d[k]) <= 59.99 and float(d[k]) > 39.99:
            print k
    print('\nPathetic (60 and beyond):')
    for k in d.keys():   
        if float(d[k]) >=60:
           print k
    #had to use too many loops because couldn't figure out 
    #how to get it to not print the heading each time
            
def main():
    print(getTime())
main()