#Exercise 183: Element Sequences
import os

def find_next_element(last_word, element_list):
    last_char = last_word[-1]
    for i in range(len(element_list)):
        if element_list[i][0] == last_char:
            new_element = element_list.pop(i)
            result = new_element + ", "
            return result + find_next_element(str(new_element), element_list)
    
    return ""
        

def main():
    #load element list
    element_list = []
    file_path = os.path.join(os.path.dirname(__file__),"elements.txt")

    with open(file_path) as f:
        for line in f:
            line = line.lower()
            line = line.replace("\n","")
            key, symbol, element = line.split(",")
            element_list.append(element)

    print("Element Sequence Game!")
    word = input("Please enter a chimical element: ")
    word = word.lower()

    if word in element_list:
        result = find_next_element(word, element_list)
        print("The word sequence is %s" %result)
    else:
        print("Please, enter a valide chimical element!")

main()