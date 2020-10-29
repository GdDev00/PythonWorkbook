#Ex. 175 Recursive Decimal To Binary

def decimal_to_binary(number, binary):
    #base case
    if number == 0:
        return binary

    #recursive case
    else:
        binary = str(number%2) + binary
        return decimal_to_binary(number//2,binary)

print(decimal_to_binary(150,""))