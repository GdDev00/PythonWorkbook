
def calculateParityBits(bits):
    n_of_zero = bits.count('0')
    n_of_one = bits.count('1')
    
    if((n_of_one % 2) == 0):
        return 0
    else:
        return 1


bits = input("Inserisci 8 bits:")

while bits!="":
    if(bits.count('0')+bits.count('1')==8):
        #stringa valida, sono 8 bits
        print("Il bit di parità è:" + str(calculateParityBits(bits)))
    else:
        print("Attenzione!!! Il testo inserito non sono 8 bits")

    bits = input("Inserisci 8 bits:")

#fino a quando non inserisco uno spazio
