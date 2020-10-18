def checkNumberPrime(number):
    if(number<1):
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def main():
    number = int(input("Inserisci un numero: "))
    result = checkNumberPrime(number)

    if(result==True):
        print("Il numero è primo!")
    else:
        print("Il numero non è primo!")

if(__name__ == "__main__"):
    main()