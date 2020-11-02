## Exercise 149: Display the Head of a File

import sys

#check if there is the second argument passed by the user
if len(sys.argv)!=2:
    print("Provide file name as argument!")
    quit()

try:
    #open file
    inf = open(sys.argv[1], "r")

    #print the first 10 line
    line = inf.readline()
    count = 0
    while count < 10:
        line = line.rstrip()
        print(line)
        count+=1
        line = inf.readline()

    inf.close()

except Exception as e: 
    print("File error!")
    print(e.args)
    quit()

