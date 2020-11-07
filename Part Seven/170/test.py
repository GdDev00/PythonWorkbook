#Exercise 169: Redacting Text in a File
import os
import string

def redact_text(words_list,sensitive_words_dict):
    for key,value in enumerate(words_list):
        if value.lower() in sensitive_words_dict:
            words_list[key]=words_list[key].replace(value,"***")

    return words_list



def main():
    sensitive_word_file_path = input("Please, input the sensitive word file name: ")
    while not os.path.isfile(sensitive_word_file_path):
        print("File not valid!")
        sensitive_word_file_path = input("Please, input the sensitive word file name: ")

    word_file_path = input("Please, input the word file name: ")
    while not os.path.isfile(word_file_path):
        print("File not valid!")
        word_file_path = input("Please, input the word file name: ")

    #load all sensitve words in a dict
    sensitive_word_dict = dict()
    sensitive_word_file = open(sensitive_word_file_path,"r")
    for word in sensitive_word_file:
        sensitive_word_dict[word.rstrip()] = 0

    sensitive_word_file.close()


    newFile = open("new_file.txt","w")


    word_file = open(word_file_path,"r")
    for line in word_file:
        line = line.strip(string.punctuation)
        words = line.split()
        words = redact_text(words, sensitive_word_dict)
        new_file_line = ' '.join(map(str, words))
        new_file_line += "\n"
        newFile.write(new_file_line)

    word_file.close()
    newFile.close()

main()