#Ex. 126 Dealing Hands of Cards

import random

NUMBER_OF_CARDS = 52
SEEDS = ["s","h","d","c"]

#return a complete list of 52 standard play cards
def createDeck():
    deck=[]
    for seed in SEEDS:
        deck.append("A"+seed)

        for i in range(2,10):
            deck.append((str(i)+seed))

        deck.append("T"+seed)
        deck.append("J"+seed)
        deck.append("Q"+seed)
        deck.append("K"+seed)

    return deck

#return a shuffled deck of cards
#params deck -> list of number(cards) to shuffle
def shuffle(deck):
    for i in range (52):
        #scelgo radom una carta
        newIndexCard = random.randint(0,51)

        #memorizzo il vecchio valore 
        oldValue = deck[i]

        #scambio le carte
        deck[i]= deck[newIndexCard]
        deck[newIndexCard] = oldValue

    return deck

#generate hands of cards
#return -> a list of the hands, the original deck is edit
def deal(nOfHands, nOfCardsForHand, deckOfCards):
    hands = []
    for i in range(nOfHands):
        cards = []
        for n in range(nOfCardsForHand):
            x = random.randint(0, (len(deckOfCards)-1))
            cards.append(deckOfCards.pop(x))
        
        hands.append(cards)
    return hands

deck = createDeck()
deck = shuffle(deck)
print("Hands: ")
print(deal(4,5,deck))
print("Deck: ")
print(deck)
    



