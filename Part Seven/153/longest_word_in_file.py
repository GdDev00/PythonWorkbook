#Exercise 153: Find the Longest Word in a File

import os.path
import string

print("Find the Longest Word in a File")

fileName = input("Please, enter the file name: \n")
#check if the file exist
while os.path.exists(fileName) == False:
    print("File not found!")
    fileName = input("Please, enter the correct file name: \n")

try:
    text = open(fileName, "r")

except Exception as e:
    print("File errror!")
    print(e.args)
    quit()

isto = dict()

lines = text.readlines()

#for each line in the file
for line in lines:
    #create a list of words in the line
    words = line.rstrip()
    #for each word in the list of words
    for word in words.split():
        word = word.lower()
        #add the word in the histogram as key and its lenght
        isto[word] = len(word)

all_isto_values = isto.values()
longest_word = max(all_isto_values)
text.close()
print("The longest word is formed by %d char" %longest_word)

print("These are the longest words:->")
for key,value in isto.items():
    if value == longest_word:
        print(key)