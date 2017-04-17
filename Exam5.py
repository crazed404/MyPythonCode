import json

def openJSON():
    #opens file
    jsonTxt = ""
    file = open('PetStore.json')
    for line in file:
        line = line.strip()
        jsonTxt = jsonTxt + line
    pets = json.loads(jsonTxt)
    return pets

def searchJSON(file):
    print('Search by category(c) or keyword (k): '),
    userIn = raw_input()
    
    #seaches for what user entered 
    if userIn == 'c':
        print('Enter a category: '),
        category = raw_input()
        category = category.lower()
        index = 0
    
        for i in file:
            jsonString = str(file[index]['Category'])
            jsonString = jsonString.lower()
            if  jsonString == category:
                print ('%s - $%s') % (file[index]['Product'], file[index]['Price'])
            index = index + 1
            
    if userIn == 'k':
        print('Enter a keyword: '),
        keyword = raw_input()
        keyword =  keyword.lower()
        index = 0
        for i in file:
            jsonString = str(file[index]['Product'])
            jsonString = jsonString.lower()
            if keyword in jsonString:
                print ('%s - $%s') % (file[index]['Product'], file[index]['Price'])
            index = index + 1
def main():
    searchJSON(openJSON())
main()