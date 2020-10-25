#Ex. 129 Tokenizing a String

#converting a string into a list of substrings, known as tokens
#@params stringExpression -> string to convert
#@return -> converted token list
def tokenize(stringExpression):
    text = stringExpression
    tokens=[]
    i=0
    while i < len(text):
        if(text[i] == "*" or text[i] == "/" or text[i] == "^" or\
            text[i] == "-" or text[i] == "+"):
            #ho trovato il primo operatore
            tokens.append(text[i])
            i+=1

        elif text[i].isnumeric():
            num=""
            while i<len(text) and text[i].isnumeric():
                num = num+text[i]
                i+=1
            tokens.append(num)
        elif text[i] == " ":
            i+=1
        else:
            #la stringa inserita contiene caratteri non validi!
            tokens.clear()
            tokens.append(0)

    return(tokens)
             


def main():
    expression = input("Inserisci un'espressione matematica: ")
    tokens = tokenize(expression)
    print("I token sono:", tokens)

if __name__ == "__main__":
    main()