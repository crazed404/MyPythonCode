import FunctionModule

verse1 = FunctionModule.userString("Enter your first verse:  ")
verse2 = FunctionModule.userString("Enter your second verse: ")
verse3 = FunctionModule.userString("Enter your third verse:  ")
verse4 = FunctionModule.userString("Enter your fourth verse: ")
chorus = FunctionModule.userString("Enter your chours:       ") 
repeat = FunctionModule.userInt("Chorus repeat?:          ")
chorusRepeat = (chorus + " ") * repeat

verse1 = verse1 + chorusRepeat 
verse2 =  verse2 + chorusRepeat 
verse3 = verse3 + chorusRepeat 
verse4 = verse4 + chorusRepeat 

verse1 = verse1.split(chorusRepeat)
verse2 = verse2.split(chorusRepeat)
verse3 = verse3.split(chorusRepeat)
verse4 = verse4.split(chorusRepeat)

verse1.insert(1,chorusRepeat)
del verse1[2]
verse2.insert(1,chorusRepeat)
del verse2[2]
verse3.insert(1,chorusRepeat)
del verse3[2]
verse4.insert(1,chorusRepeat + chorus)
del verse4[2]

#I originally did this without a for loop because I couldn't get the list to work
#but I messed around for a while with the list and got it too work
songList = verse1 + verse2 + verse3 + verse4

print songList

print ''
for element in [0]:
    print songList[0]
    print songList[1]
    print songList[2]
    print songList[3]
    print songList[4]
    print songList[5]
    print songList[6]
    print songList[7]
    
print '...one more time...'

for element in [0]:
    print songList[0]
    print songList[1]
    print songList[2]
    print songList[3]
    print songList[4]
    print songList[5]
    print songList[6]
    print songList[7]