#Ex. 174 Greatest common divisor

def greatest_commond_divisor(a,b):
    if b == 0:
        return a
    else:
        c = a%b
        return greatest_commond_divisor(b,c)

def main():
    print("Greatest Common Divisor of two numbers!")
    number1 = int(input("Please, insertr the first number: "))
    number2 = int(input("Plase, insert the second number:"))
    print("The greatest commond divisor is %d" %greatest_commond_divisor(number1,number2))

main()