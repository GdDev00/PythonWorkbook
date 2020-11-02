#Exercise 150: Display the Tail of a File

import sys

NUM_LINES = 10

#check if there is the second argument passed by the user
if len(sys.argv)!=2:
    print("Provide file name as argument!")
    quit()

try:
    #open file
    inf = open(sys.argv[1], "r")

    lines = []
    #Read the file and save in a list 10 lines at a time
    for line in inf:
        lines.append(line.rstrip())
        #If there are more than NUM_LINES lines, i remove the oldest
        if len(lines)>NUM_LINES:
            lines.pop(0)

    #close the file
    inf.close()

    #Print the result (the old 10 line)
    for element in lines:
        print(element)

except Exception as e: 
    print("File error!")
    print(e.args)
    quit()
