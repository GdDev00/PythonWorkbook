
def calculateDivisors(integer):
    divisors=[]
    i=integer-1
    while i>0:
        if integer % i == 0: #il numero divide perffettamente quel numero
            divisors.append(i)
        i=i-1

    return divisors

def isPerfectNumber(integer):
    divisors = calculateDivisors(integer)
    sum=0
    for num in divisors:
        sum += num

    if sum == integer:
        return True  #è un numero perfetto
    else:
        return False #NON è un numero perfetto


def main():
    print("Ecco i numeri perfetti da 1 a 10.000:")
    print("")
    for i in range(0,10000):
        if(isPerfectNumber(i)):
            print(i)


main()