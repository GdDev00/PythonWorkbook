#Exercise 158: Remove Comments
import os

#remove Python comment from text line
def remove_comments_from_line(s):
    result_string = s

    #find if in the string there is a '#'
    index = s.find('#')
    if index != -1:
        result_string = result_string[:index]
        #if the string isn't empty
        #i add the \n ad end of line
        if len(result_string)>0:
            result_string += "\n"
        return result_string
    else:
        return result_string


def main():
    input_file_name = input("Please, enter the file name to open: ")
    while os.path.isfile(input_file_name) == False:
        print("File name isn't valid!")
        input_file_name = input("Please, enter the file name to open: ")

    output_file_name = input("Please, enter the output file name: ")

    try:
        input_file = open(input_file_name,"r")
    except Exception as e:
        print("Error!")
        print(e.args)

    try:
        output_file = open(output_file_name, "w")

        for line in input_file:
            output_file.write(remove_comments_from_line(line))

        output_file.close()
        input_file.close()
    except Exception as e:
        print("An error was encourend while processing the file")
        print(e.args)
        print("Quitting")

main()