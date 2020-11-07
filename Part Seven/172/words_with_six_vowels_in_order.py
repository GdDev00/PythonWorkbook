#Exercise 172:Words with Six Vowels in Order
import os


 #load a file into a words list
 #@params 'fileName' -> name of the file to open
 #@return -> a list with all the words contains in the file
def load_file(fileName):
    word_list=[]
    try:
        inf = open(fileName,"r")
        for line in inf:
            line= line.rstrip()
            word_list.append(line)

    except Exception as ex:
        print("Error!")
        print(ex.args)
        quit()

    inf.close()
    return word_list

#chek words with order vowel 
#@parmas words_list -> a list with all word to check
#@return -> a list with all word with six vowels in order
def check_words_with_order_vowel(words_list):
    ordered_word = []

    for word in words_list:
        word = word.lower()
        is_ordered = True

        last_vowel_index = -1

        #check if the word contains all vowel in order "aeiou"
        for char in "aeiou":
            if is_ordered == True:
                #check if the vowel exist and get its index
                vowel_index = word.find(char)

                #if the word contains
                if  vowel_index == -1:
                    is_ordered = False
                elif vowel_index > last_vowel_index:
                    last_vowel_index = vowel_index
                else:
                    is_ordered=False

        if is_ordered==True:
            ordered_word.append(word)

        is_ordered = False

    return ordered_word



    
def main():
    file_name = input("Please, enter the file name: ")
    words_list = load_file(file_name)
    ordered_words = check_words_with_order_vowel(words_list)
    for word in ordered_words:
        print(word)

        
main()