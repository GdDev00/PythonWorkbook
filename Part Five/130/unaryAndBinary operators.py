#Ex. 130  Unary and Binary operators

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

#check the unary operators + and -
#@parmas listOfToken -> the list of token where find + - unary operators
#@return list of token, when the operator is unary, it is signed with u
#        ex: 2*-3 -> return [2,*,u-,3]
def checkUnaryOperators(listOfToken):
    nextIsUnary=False
    for i in range(len(listOfToken)):
        if listOfToken[i] == "*" or listOfToken[i] == "/" or listOfToken[i]=="(" or\
            listOfToken[i] == "[" or listOfToken[i] == "{":
            nextIsUnary = True
        elif listOfToken[i] =="+" or listOfToken[i]=="-":

            #the operator it's the first element
            if i == 0:
                listOfToken[i] = "u"+listOfToken[i]

            elif nextIsUnary==True:
                listOfToken[i] = "u"+listOfToken[i]
                nextIsUnary=False           

    return listOfToken


def main():
    line = input("Inserisci un'espressione matematica: ")
    result = checkUnaryOperators(tokenize(line))
    for element in result:
        print(element)

if __name__ == "__main__":
    main()

            
