#Ex. 147 Checking for a Winning Card

from bingo_card import show_bingo_card, create_bingo_card

#A card wins when contains a list of 5 zeros (vertical, horizontal or diagonal)
#@params card -> the card to check
#@return -> True if is win, False if no win
def check_winning_card(card):
    #check horizontal line
    for i in range(5):
        signed_num_sum = 0

        for char in "BINGO":
            signed_num_sum += card[char][i]
        
        #card is winning
        if signed_num_sum == 0:
            return True

    #check vertical line
    for char in "BINGO":
        signed_num_sum = 0
        for i in range(5):
            signed_num_sum += card[char][i]

        if signed_num_sum == 0:
            return True

    #check diagonal line
    i=0
    for char in "BINGO":
        signed_num_sum = card[char][i]
        i+=1

    if signed_num_sum == 0:
        return True

    for char in "OGNIB":
        signed_num_sum = card[char][i]
        i+=1
    if signed_num_sum == 0:
        return True


    #the card not win
    return False

def main():
    print("Cartella originale:")
    card_original = create_bingo_card()
    show_bingo_card(card_original)
    print()

    #--------------------------------------------------------#
    #I demonstrate the function with a horizontal line winning
    print("Cartella vincente sulla prima linea orizzontale: ")
    card = card_original.copy()
    for char in "BINGO":
        card[char][0]=0

    show_bingo_card(card)

    result = check_winning_card(card)

    if result:
        print("La carta è vincente!")
    else:
        print("La carta è perdente!")


    # ------------------------------------------------------#
    #I demonstrate the function with a vertical line winning

    print()
    print()
    print("Cartella vincente sulla prima linea verticale: ")
    card = card_original.copy()
    for i in range(5):
        card['B'][i]=0

    show_bingo_card(card)

    result = check_winning_card(card)

    if result:
        print("La carta è vincente!")
    else:
        print("La carta è perdente!")

     # ------------------------------------------------------#
    #I demonstrate the function with a diagonal line winning

    print()
    print()
    print("Cartella vincente sulla prima linea diagonale: ")
    card = card_original.copy()
    i=0
    for char in "BINGO":
        card[char][i] = 0
        i+=1

    show_bingo_card(card)

    result = check_winning_card(card)

    if result:
        print("La carta è vincente!")
    else:
        print("La carta è perdente!")


main()
    