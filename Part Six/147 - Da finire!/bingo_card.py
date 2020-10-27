#Ex. 146 Create a bingo card
import random

def create_bingo_card():
    card_dict = dict()
    numerb_range_min = 1

    for char in "BINGO":
        #i will generate 5 number for letter
        for i in range(5):
            if char in card_dict:
                newNumber =  random.randint(numerb_range_min,numerb_range_min+15)
                while newNumber in card_dict[char]:
                    newNumber =  random.randint(numerb_range_min,numerb_range_min+15)

                card_dict[char].append(newNumber)
            else:
                card_dict[char] = [random.randint(numerb_range_min,numerb_range_min+15)]

        numerb_range_min += 15

    return card_dict

def show_bingo_card(card):

    #create the card

    #show the card
    print(" B  I  N  G  O ")
    for i in range(5):
        for char in "BINGO":
            print("%2d " % card[char][i], end="")
        print()


def main():
    line = input("Premi qualsiasi tasto per generare la tua cartella del bingo: ")

    card = create_bingo_card()
    show_bingo_card(card)

if __name__ == "__main__":
    main()