#Ex. 137 Two Dice Simulation
import random

#This function 
def rolls_two_dice():
    roll_a = random.randint(1,6)
    roll_b = random.randint(1,6)

    return roll_a + roll_b

def main():
    #In the value is initialized to the probability that each key will occur
    #when two 6-sided dice are rolled
    expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, \
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, \
    11: 2/36, 12: 1/36}

    result_dict = dict()

    for i in range(0,1000):
        #roll the dice
        roll_result = rolls_two_dice()

        if result_dict.get(roll_result,0) == 0: 
            #the key for this value is inesistent
            result_dict[roll_result] = 1
        else:
            #the key for this value already exists, I increment its counter
            result_dict[roll_result] += 1

    #I print the result
    print("Total Simulated Expected")
    print(" Percent Percent")    
    for c in sorted(result_dict.keys()):
        print("%5d %11.2f %8.2f" % (c, result_dict[c] / 1000 * 100, expected[c] * 100))
        
main()
