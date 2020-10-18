
#Controlla se il numero inserito sotto forma di stringa è un intero valido
#@parameter s, stringa da controllare
#
#@return True se la stringa è un intero valido
#@return False se la stringa NON è un intero valido

def isInteger(s):
    #rimuovo tutti gli spazi all'inizio e alla fine della stringa
    s = s.strip()

    if(len(s)>1):
        if((s[0] == '+' or '-') and s[1:].isdigit()==True):
            return True
        else:
            return False
    else:
        return False



def main():
    line = input("Inserisci stringa: ")
    if isInteger(line) == True:
        print("La stringa rappresenta un intero valido")
    else:
        print("La stringa NON rappresenta un intero valido")

if __name__ == "__main__": 
    main()