#Ex. 132 Evaluate Postfix

from unaryAndBinaryOperators import tokenize, checkUnaryOperators

def convertPostfixToInfix(expression):
    value = []
    for element in expression:
        if element.isnumeric():
            value.append(float(element))     
        elif element.find("u") != -1: #l'operatore è unario
            oldElement = value.pop()
            oldElement = oldElement*-1
            value.append(oldElement)
        else: #l'operatore è binario
            right = value.pop()
            left = value.pop()
            if element == "*":
                value.append(left*right)
            elif element == "/":
                value.append(left / right)
            elif element == "^":
                value.append (left ** right)
            elif element == "+":
                value.append (left + right)
            elif element == "-":
                element.append (left - right)

    return value[0]
    

def main():
    line = input("Inserisci un'espressione in notazione postfissa: ")
    tokens = checkUnaryOperators(tokenize(line))
    result = convertPostfixToInfix(tokens)
    print(result)

if __name__ == "__main__":
    main()
