def precedence(string):
    if (string == "+" or string == "-"):
        return 1
    elif string == "*" or string == "/":
        return 2
    elif string == "^":
        return 3
    else:
        return -1

def main():
    string = input("Inserisci un operatore: ")    
    
    precedence(string)
    
    if precedence(string) > 0:
        print(string, "è un operatore:",precedence(string))
    elif precedence(string) < 0:
        print(string, "non è un operatore:",precedence(string))

if __name__ == "__main__":
    main()