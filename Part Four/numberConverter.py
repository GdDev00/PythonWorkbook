def hex2int(n):
    n = int(n, 16)
    return n
    
def int2hex(n):
    n = hex(n)
    return n

def main():  
    print("Premi 1 per il convertitore Hex-> Int ")
    print("Premi 2 per il convertitore Int-> Hex ")
    print("Premi 0 per uscire")

    choice = int(input(">>>"))
    
    if choice == 1:
        n = input("Inserisci un numero esadecimale: ")
        print(hex2int(n))
        
    elif choice == 2:
        n = int(input("Inserisci un intero: "))
        print(int2hex(n))
   
    elif choice == 0:
        print("Ciao ;)")
   
    else:
        print("Non è un'opzione valida!")

if __name__ == "__main__":
    main()
