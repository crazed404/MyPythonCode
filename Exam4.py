#couldn't figure out how to do the os thing
def openFiles():
    #reads files in and properly formats them
    breadList = []
    file0 = open('bread.txt', 'r') 
    for item in file0:
        item = item.upper()
        item = item.strip()
        item = item.split()
        breadList.append(item)
        
    firstAidList = []
    file1 = open('firstAid.txt', 'r') 
    for item in file1:
        item = item.upper()
        item = item.strip()
        item = item.split()
        firstAidList.append(item)
        
    recipesList = []
    file2 = open('recipes.txt', 'r') 
    for item in file2:
        item = item.upper()
        item = item.strip()
        item = item.split()
        recipesList.append(item)
    
    triviaList = []
    file3 = open('trivia.txt', 'r') 
    for item in file3:
        item = item.upper()
        item = item.strip()
        item = item.split()
        triviaList.append(item)
    
    global userWord
    print('Please enter a word to search for: '),
    userWord = raw_input().upper()
    global count
    count = 0
    
    for i in range (0, len(breadList)):
        if userWord in breadList[i]:
            print ('bread.txt ' + str(breadList[i]))
            count = count + 1
    
    for i in range (0, len(firstAidList)):
        if userWord in firstAidList[i]:
            print ('firstAid.txt ' + str(firstAidList[i]))
            count = count + 1
            
    for i in range (0, len(recipesList)):
        if userWord in recipesList[i]:
            print ('recipes.txt ' + str(recipesList[i]))
            count = count + 1
            
    for i in range (0, len(triviaList)):
        if userWord in triviaList[i]:
            print ('trivia.txt ' + str(triviaList[i]))
            count = count + 1
    
def getCount():
    print('There are %s instances of %s in the files.' % (count, userWord))
    
def main():
    openFiles()
    getCount()
main()