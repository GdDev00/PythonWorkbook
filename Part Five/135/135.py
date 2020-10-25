#Ex. 135 The Sieve of Eratosthenes

def calculatePrimeNumber(limit):
    numbers=[]
    for n in range(0,limit+1):
        numbers.append(n)
    
    numbers[1]=0
    p = 2
    while p <limit:
        #change to 0 all the multiple of p
        for i in range (p*2, limit+1, p):
            numbers[i] = 0
        
        p = p + 1
        while p < limit and numbers[p] == 0:
                p+=1
            
    for i in range(len(numbers)):
        if 0 in numbers:
            numbers.remove(0)

    return numbers

