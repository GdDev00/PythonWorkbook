#Ex. 172 Spelling with element symbol
import os

def spelling(word_to_spell, symbol_list):
    if len(word_to_spell) == 0:
        return ""

    else:
        result = ""

        if word_to_spell[0:2] in symbol_list:
            result += word_to_spell[0:2] + " "
            result += spelling(word_to_spell[2:],symbol_list)

        elif word_to_spell[0:3] in symbol_list:
            result += word_to_spell[0:3] + " "
            result += spelling(word_to_spell[3:],symbol_list)
        else:
            result = ""
    
    if len(result.replace(" ",""))==len(word_to_spell):
        return result
    else:
        return ""


def main():
    element_dict = {}

    file_path = os.path.join(os.path.dirname(__file__),"elements.txt")

    with open(file_path) as f:
        for line in f:
            line = line.lower()
            line = line.replace("\n","")
            key, symbol, element = line.split(",")
            element_dict[symbol] = element

    for element in element_dict.values():
        result = spelling(element,element_dict)
        if result != "":
            print(result)


main()