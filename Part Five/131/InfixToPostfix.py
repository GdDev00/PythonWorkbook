#Ex 131: Infix to Postfix

from tokenizeExpression import tokenize

def precedence(operator):
    if operator == "+" or operator == "-":
        return 1
    if operator == "*" or operator == "/":
        return 2
    if operator == "u+" or operator == "u-":
        return 3
    if operator == "^":
        return 4

def convertInfixToPostfix(infixExpressionTokenList):
    operators = []
    postfix = []

    for token in infixExpressionTokenList:
        if (str(token)).isnumeric() == True:
            postfix.append(token)
        if token == "*" or token == "/" or token == "+" or token == "-" or token == "^":
            while len(operators)>0 and operators[-1] != "(" and operators[-1] != "[" \
                and operators[-1] != "{"  and precedence(token)<precedence(operators[-1]):
                postfix.append(operators.pop())
            operators.append(token)
        if token == "(" or token == "[" or token=="{":
            operators.append(token)
        if token == ")" or token == "]" or token=="}":
            while operators[-1] != "(" and operators[-1] != "[" and operators[-1] != "{":
                postfix.append(operators.pop())
            operators.remove("(")
            operators.remove("[")
            operators.remove("{")

    while len(operators)>0:
        postfix.append(operators.pop())

    return postfix


def main():
    line = input("Inserisci un'espressione in notazione infissa: ")
    tokens = tokenize(line)
    result = convertInfixToPostfix(tokens)
    print(result)

if __name__ == "__main__":
    main()
