#Exercise 167: Spell Checker
import sys
import string


CORRECT_WORDS_F_NAME = "words.txt"

#remove punctuation marks at the beginning and end of string
#@return a list of words
def onlyWords(s):
    t = s.split()
    returnList=[]
    for word in t:
        word = word.lower()
        for char in string.punctuation:
            if (word[0]) == char:
                word = word[1:]
            if (word[-1]) == char:
                word = word[:(len(word)-1)]
        returnList.append(word)

    return returnList


#check if a list of string is containing in the second argument dict
#@returns a dictionary with all the words not present
def check_string(words_list,known_words_dict):
    spelling_mistakes_dict=dict()

    for word in words_list:
        if word not in known_words_dict:
            spelling_mistakes_dict[word]=0

    return spelling_mistakes_dict

def main():
    if len(sys.argv)!=2:
        print("Provide file name as argument!")
        quit()

    spelling_mistakes_dict = dict()
    #open file
    try:
        inf = open(sys.argv[1], "r")
    except Exception as ex:
        print("Error!")
        print(ex.args)

    #load correct words file
    correct_words_dict = dict()
    f_correct_words = open(CORRECT_WORDS_F_NAME,"r")
    for line in f_correct_words:
        line = line.rstrip()
        for word in line.split():
            correct_words_dict[word.lower()] =  0

    for line in inf:
        line.rstrip()
        line = onlyWords(line)
        spelling_mistakes_dict.update(check_string(line,correct_words_dict))

    inf.close()
    
    if len(spelling_mistakes_dict)>0:
        print("These are the spelling mistakes: ")
        for word in spelling_mistakes_dict.keys():
            print(word)

main()



