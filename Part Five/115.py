#Ex. 115 List of Proper Divisors

def calculateProperDivisors(number):
    properDivisors = []
    
    tNum = number

    while tNum > 1:
        tNum = tNum - 1
        if number % tNum == 0: #is a proper divisor
            properDivisors.append(tNum)
    
    return properDivisors


def main():
    number = int(input("Inserisci un numero intero: "))
    print("I divisori propri di questo numero sono: ")
    print(calculateProperDivisors(number))


if __name__ == "__main__":
    main()
        
