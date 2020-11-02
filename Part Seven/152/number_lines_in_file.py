#Exercise 152: Number the Lines in a File
import os.path

print("Number the lines in a file")

fileName = input("Please, enter the file name: \n")
#check if the file exist
while os.path.exists(fileName) == False:
    print("File not found!")
    fileName = input("Please, enter the correct file name: \n")

#name of file output
newFileName = input("Please, enter the desired name for the new file: \n")

inf = open(fileName,"r")
newFile = open(newFileName,"w")

count = 1
for line in inf:
    newLine = "%d: %s" %(count,line)
    newFile.write(newLine)
    count+=1

inf.close()
newFile.close()