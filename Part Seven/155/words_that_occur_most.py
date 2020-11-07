#Ex. 155 Words that Occur Most

import os.path
import string

def main():
    fileName = input("Please, enter the file name: \n")

    #check if the file exist
    while os.path.exists(fileName) == False:
        print("File not found!")
        fileName = input("Please, enter the correct file name: \n")

    try:
        inf = open(fileName, "r")

    except Exception as e:
        print("File errror!")
        print(e.args)
        quit()

    frequency_dict = dict()
    
    for line in inf:
        #print word frequency in dictionary
        for word in line.split():
            word = word.lower()

            #remove any leading punctuation marks
            word = word.lstrip(string.punctuation + string.whitespace)

            #remove any tail punctuation marks
            word = word.rstrip(string.punctuation + string.whitespace)

            frequency_dict[word] = frequency_dict.get(word, 0) + 1

    inf.close()
    
    #print result
    print("The most frequency words is:")
    max_frequency = max(frequency_dict.values())
    for key,value in frequency_dict.items():
        if value==max_frequency:
            print("'%s'" %key)
    
    print("They are repeated %d time" %max_frequency)
        
main()