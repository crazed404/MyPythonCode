#anomaly = 1951 - 1980

import TempFunctions

#turns from strings to floats
#read the temps into myTemps
myTemps = TempFunctions.readTemps();
# cal the average for values from 0 to 80
ave1 = TempFunctions.calculateAve(myTemps, 0, 81) 
count1 = TempFunctions.countTemps(myTemps, 0, 81)
print 'During the first 81 years the deviation from the anomaly was %f'% ave1
print 'During the first 81 %s had a positive temperature anomaly '% count1


ave2 = TempFunctions.calculateAve(myTemps, 81, 116)
count2 = TempFunctions.countTemps(myTemps, 81, 116)
print 'During the last 35 years the deviation from the anomaly was %f'%ave2
print 'During the last 35 %s had a positive temperature anomaly '% count2





