#Ex. 175 Recursive Decimal To Binary

def decimal_to_binary(number, binary=""):
    #base case
    if number == 0:
        return binary

    #recursive case
    else:
        binary = str(number%2) + binary
        return decimal_to_binary(number//2,binary)

def main():
    print("Recursive Decimal to Binary converter")
    num = int(input("Please, insert a non negative number-->\n"))
    if num>0:
        print("The binary number is: "+  decimal_to_binary(num))
    else:
        print("The number must be a non negative integer!")

main()