import json
import urllib2

def readJson():
    #asks user for where they want to know the weather for 
    #and opens the file
    print('Where would you like to know the weather for?:'),
    userLocation = raw_input()
    url = 'https://api.apixu.com/v1/current.json?key=1de387c932054c6690f230028172304&q=' + userLocation
    jsonTxt = urllib2.urlopen(url).read()
    jsonTxt = json.loads(jsonTxt)

    return jsonTxt

def returnWeather(file):
    location = str(file['location']['name'] + ', ' + file['location']['region'])
    print('Here is the current weather for ' + location + '.') 
    sky = str(file['current']['condition']['text'])
    temp = str(file['current']['temp_f'])
    feelTemp = str(file['current']['feelslike_f'])
    
    print(sky + ' and ' + temp + ' degrees (F).')
    print('It actually feels like ' + feelTemp + '(F).') 

def main():
    returnWeather(readJson())
main()