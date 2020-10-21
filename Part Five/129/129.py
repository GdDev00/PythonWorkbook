OPERATORS = ["*","/","^","-","+"]


def tokenize(stringExpression):
    text = stringExpression.replace(" ","")
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