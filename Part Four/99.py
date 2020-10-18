from numberConverter import hex2int, int2hex

def convertDecToN(num, newBase):
    result=""
    n = num
    r = n%newBase
    result = int2hex(r)+ result
    n=n//newBase

    while n>0:
        r = n%newBase
        result = int2hex(r)+result
        n=n//newBase

    return result

def convertNtoDec(num, oldBase):
    dec = 0

    for i in range(len(num)):
        dec = dec * oldBase
        dec = dec + hex2int(num[i])

    return dec


def main():
    fromBase = int(input("Inserisci la base inziale: "))
    fromNum = input("Inserisci una sequenza di numeri: ")
    dec = convertNtoDec(fromNum,fromBase)
    print("In base 10: %d" %dec)

    toBase = int(input("Inserisci la base su cui eseguire la conversione: "))
    toNum = convertDecToN(dec, toBase)
    print("%s in base %d" % (toNum, toBase))    

main()