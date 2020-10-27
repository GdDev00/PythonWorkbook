#Ex. 148 - Play Bingo

from bingo_card import create_bingo_card, show_bingo_card
from check_winning_card import check_winning_card

import random
import copy

#generate a bingo extration list
#@return -> extration list
def generate_bingo_calls():
    numbers = []
    numerb_range_min = 1

    #generate a list with all bingo calls
    for char in "BINGO":
        for i in range(numerb_range_min,numerb_range_min+15):
            numbers.append(char + str(i))

        numerb_range_min += 15
    
    #randomize number order
    random.shuffle(numbers)

    return numbers


def main():
    print("Bingo!")

    input("Press any key to generate one bingo card...")
    original_card = create_bingo_card()
    print()

    print("Your card is this:")
    show_bingo_card(original_card)
    print()

    input("Press any key to simulate 1000 games with your cards...")

    N_OF_GAMES = 1000
    min_call = N_OF_GAMES
    max_call = 0
    totalCall= 0
    count = 0

    for i in range(N_OF_GAMES):   
        count = 0

        #copy the original cards in another variable
        card = copy.deepcopy(original_card)

        calls = generate_bingo_calls()

        #check the extration number
        for val in calls:
            #countator for stats
            count +=1

            for key,card_line_numbers in card.items():
                if int(val[1:]) in card_line_numbers:
                    ind = card_line_numbers.index(int(val[1:]))
                    card[key][ind]=0

            if check_winning_card(card)==True:
                if count < min_call:
                    min_call=count
                if count > max_call:
                    max_call= count
                
                totalCall += count
                break
        
    print("Here are the stats -->")
    print("The minimum number of calls before the card result winning are: %d" %min_call)
    print("The max number of calls before the card result winning are: %d" %max_call)
    print("The average of number calls is: %0.2f" %(totalCall/N_OF_GAMES))


main()