import json

def openJson():
    #opens JSON file and converts it to txt and back to 
    #usable python
    jsonTxt = ""
    file = open('Pets.json')
    for line in file:
        line = line.strip()
        jsonTxt = jsonTxt + line
    pets = json.loads(jsonTxt)
    return pets
    
def getPets():
    jsonTxt = openJson()
    print('Please enter a pet name'),
    name = raw_input()
    for i in jsonTxt:
        if i["Name"] == name:
            print i["Color"]
            for breed in i["Breed"]:
                print breed
    
def main():
    getPets()
main()