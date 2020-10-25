#Ex. 125 Shuffling a Deck of Cards

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


def main():
    deckOfCards = createDeck()
    for element in deckOfCards:
        print(element)

    print("")
    print("Mischio le carte....")
    print("")

    shuffledCards = shuffle(deckOfCards)
    for card in shuffledCards:
        print(card)


main()