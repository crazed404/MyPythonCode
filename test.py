def buildDeck():
    rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    deck = []
    for i in range(0,13):
        deck.append(rank[i])
    print deck
buildDeck()