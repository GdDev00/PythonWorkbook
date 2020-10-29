#Exercise 178: Recursive Palindrome

def is_palindrome(string):
    #base case
    if len(string)==1 or string == "":
        return True
    
    #recursive case
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False


def main():
    print("Check if a string is palindrome using recursive function!")
    string = input("Please, write a string-->\n")
    if(is_palindrome(string)):
        print("The string is PALINDROME")
    else:
        print("The string is NOT PALINDROME!")

main()