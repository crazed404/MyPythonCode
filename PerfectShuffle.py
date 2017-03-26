def buildDeck():
    #I decided to not use any parameters for this function
    #instead I just put the rank and suit within the function, considering they never change
    rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    deck = []
    
    #for each rank adds suit each time
    for i in range(0,len(rank)):
        deck.append(rank[i] + ' of ' + suit[0])
        deck.append(rank[i] + ' of ' + suit[1])
        deck.append(rank[i] + ' of ' + suit[2])
        deck.append(rank[i] + ' of ' + suit[3])
    return deck

def shuffle(deck):
    shuffleDeck = []
    half1 = deck[:26]
    half2 = deck[26:]
   
    #algo that does the actual shuffling
    for i in range(0,26):
        if i ==  0:
            shuffleDeck.append(half1[i])
            shuffleDeck.append(half2[i])
        if i % 2 != 0:
            shuffleDeck.append(half1[i])
        if i % 2 != 0:
            shuffleDeck.append(half2[i])
        if i % 2 == 0 and i != 0:
            shuffleDeck.append(half1[i])
        if i % 2 == 0 and i != 0:
            shuffleDeck.append(half2[i])
            
    return shuffleDeck
    
def deal(deck):
    hand = []
    i = 0
    print('How many times would you like to shuffle? '),
    shuffleTimes = int(raw_input())
    
    #loop for how many times to do shuffle the deck
    while i <shuffleTimes:
        deck = shuffle(deck)
        hand = deck[:5]
        i+= 1
    print hand
    
def main():
   #uses buildDeck() as parameter because don't want shuffled when calling shuffle function
   #inside of of deal()
   deal(buildDeck())
main()