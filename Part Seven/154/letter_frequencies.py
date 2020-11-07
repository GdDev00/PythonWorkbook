#Ex. 154: Letter Frequencies

import sys
import string

#check if there is the second argument passed by the user
if len(sys.argv)!=2:
    print("Provide file name as argument!")
    quit()

try:
    inf = open(sys.argv[1],"r")
except Exception as e:
    print("File error!")
    print(e.args)

frequency_dict = dict()

for line in inf:
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

inf.close()
print("These are the letter frequencies for this file->")
for key,value in frequency_dict.items():
    print("%s:-> %d" %(key,value))
