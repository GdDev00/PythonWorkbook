import random

def lanciaMoneta():
    #genero un numero casuale tra 0 e 1 
    #0 simulerà la TESTA (H)
    #1 simulerà la CROCE (T)
    result = random.randint(0,1)

    #TESTA
    if(result==0):
        return "H"
    else:
        return "T"



line = input("Premi invio per lanciare la moneta. q per uscire ")


for i in range(0,10):
    print("")
    n_of_head = 0
    n_of_tails = 0
    previousResult=""
    previousResultCount = 0
    attemps = 0

    while previousResultCount <3:
        attemps +=1
        result = lanciaMoneta()
        print(result, end=" ")

        if(result == "H"):
            n_of_head +=1
            if previousResult == "H":
                previousResultCount +=1
            else:
                previousResultCount = 1
                previousResult = "H"
        else:
            n_of_tails +=1
            if previousResult == "T":
                previousResultCount +=1
            else:
                previousResultCount = 1
                previousResult = "T"
    print("Sono stati necessari %.d tentativi" %attemps)
    print("La media è di %.2f" %(attemps/2))
    