#Ex. 177 Roman Numerals

roman_numbers_dict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}

def convert_roman_number_to_int(number):
    #base case
    if number == "":
        return 0

    #recursive case
    else:
        if len(number)>1:
            if roman_numbers_dict[number[0]] < roman_numbers_dict[number[1]]:
                return -roman_numbers_dict[number[0]] + convert_roman_number_to_int(number[1:])

            return roman_numbers_dict[number[0]] + convert_roman_number_to_int(number[1:])
        
        return roman_numbers_dict[number[0]]


def main():
    print("Roman Number to Integer Number")
    roman_number = input("Please insert a roman number: \n").upper()
    print(convert_roman_number_to_int(roman_number))

main()