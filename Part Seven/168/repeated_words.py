#Exercise 168: Repeated Words
import sys
import string


def main():
    if len(sys.argv)!=2:
        print("Provide file name as argument!")
        quit()

    #open file
    try:
        inf = open(sys.argv[1], "r")
    except Exception as ex:
        print("Error!")
        print(ex.args)


    repeated_words = []
    file_lines = inf.readlines()

    last_line_word = ""

    #for each line in the file
    for i in range(len(file_lines)):
        file_lines[i] = file_lines[i].rstrip()
        file_lines[i] = file_lines[i].lower()

        line_words = file_lines[i].split()
        
        if line_words[0] == last_line_word:
            repeated_words.append((word,(str(i)+"," +str(i+1))))

        previous_word = ""
        for word in line_words:
            if word == previous_word:
                repeated_words.append((word,i+1))
            previous_word = word
        last_line_word = line_words[-1]

    inf.close()
    
    for element in repeated_words:
        print(element)
        

main()

        
