#returns list from file
def readTemps():
    list = []
    file = open('temps.txt', 'r') 
    for item in file:
        item = item.strip()
        list.append(float(item)) # turn the string to a float!
    return list    
        
def calculateAve(temps, start, stop):
    total = 0.0 # we need the total to calculate the average
    for i in range(start, stop): # we need a loop for the values
        total = total + temps[i] # now we do the summation
    return total/(stop-start) # and finally we do the division
         There is a chat window on the ri

 
 