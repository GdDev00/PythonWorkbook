n = int(input("Inserisci un numero intero (2 o maggiore): "))

factor = 2
while factor <= n:
    if n%factor == 0:
        print(factor)
        n= n/factor
    else:
        factor +=1