def greatesCommonDivisor(intA, intB):
    d=0

    d=min(intA,intB)

    while intA%d !=0 and intB%d!=0:
        d = d-1

    return d

def reduceFractions(num,den):
    if(num==0):
        return (0,1)

    d = greatesCommonDivisor(num,den)
    return (num//d, den//d)

def main():
    num = int(input("Inserisci numeratore: "))
    den = int(input("Inserisci denominatore: "))
    (n,d) = reduceFractions(num,den)

    print("La frazione è stata ridotta in: %d / %d " %(n,d))


main()