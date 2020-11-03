#Exercise 159: Two Word Random Password
import random

RANDOM_FILE_NAME =  "words.txt"

def main():
    inp = input("Please enter a key to generate a simple password: ")

    try:
        inf = open(RANDOM_FILE_NAME, "r")
    except Exception as ex:
        print("File error!")
        print(ex.args)

    words=[]
    #read all word in the file and save only the word with lenght
    #between 3 and 7 char
    for line in inf:
        line = line.rstrip()
        line = line.lower()
        for word in line.split():
            if len(word)>=3 and len(word)<=7:
                words.append(word)
    inf.close()

    #choose casually a word in the list
    word_index = random.randint(0,len(words))
    first_psw = words[word_index]
    first_psw = first_psw.capitalize()

    #remove from the list the word selected
    words.pop(word_index)

    password = first_psw
    #choose casually the second word in the list
    #to generate a password with lenght between 8 and 10 char
    while len(password)<8 or len(password)>10:
        second_psw = words[random.randint(0,len(word))]
        second_psw = second_psw.capitalize()
        password = first_psw + second_psw

    print("The generate password is: %s"%password)
    
main()