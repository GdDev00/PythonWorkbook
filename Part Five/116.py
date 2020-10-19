#Ex. 116 Perfect Numbers

def calculateProperDivisors(number):
    properDivisors = []
    
    tNum = number

    while tNum > 1:
        tNum = tNum - 1
        if number % tNum == 0: #is a proper divisor
            properDivisors.append(tNum)
    
    return properDivisors

def isPerfectNumber(integer):
    divisors = calculateProperDivisors(integer)

    numberSum=sum(divisors)

    #A number is perfect when the sum of all of the proper divisors of n is equal to n.
    if numberSum == integer:
        return True  #it's a perfect number
    else:
        return False #it isn't a perfect number


def main():
    print("Ecco i numeri perfetti da 1 a 10.000:")
    print("")
    for i in range(1,10000):
        if(isPerfectNumber(i)):
            print(i)

main()