#Exercise 171: Consistent Line Lengths
import os


def main():
    #get terminal width
    terminal_widht = os.get_terminal_size()[0]

    file_name = input("Please, enter the file name to open: ")
    while os.path.isfile(file_name) == False:
        print("File name isn't valid!")
        file_name = input("Please, enter the file name to open: ")
    try:
        inf = open(file_name,"r")
        text = []

        #copy text in a list
        for line in inf:
            line = line.rstrip()
            for word in line.split():
                text.append(word)   


        word_len_count = 0
        for word in text:
            word_len_count += len(word) +1 #+1 is the space char
            if word_len_count>terminal_widht:
                print("")
                word_len_count=0
            else:
                print(word, end=" ")
    inf.close()

    except Exception as ex:
        print("Error!")
        print(ex.args)
 

main()