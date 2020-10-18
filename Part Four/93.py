from prime import checkNumberPrime

def searchNextPrimeNumber(num):
    while (checkNumberPrime(num)==False):
        num+=1
    return num

number = int(input("Inserisci un numero: "))
nextPrime = searchNextPrimeNumber(number)
print("Il prossimo numero primo è: %d" %nextPrime)
