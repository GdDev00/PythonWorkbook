#Exercise 151: Concatenate Multiple Files

import sys

if len(sys.argv)<2:
    print("At least one argument is required!")
    quit()

try:
    for i in range(1, len(sys.argv)):     
        inf = open(sys.argv[i])
        for line in inf:
            print(line, end="")

        inf.close()

except Exception as e:
    print("File errror!")
    print(e.args)
