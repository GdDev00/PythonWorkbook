#Ex. 112 - Remove Outliers


# Remove the outliers from a list of values
#@param t = the list of element to analys
#@param nElementToRemove = the number of elements to remove at the extremes of the list
#
#@return = return a new list without the desideraded extremes

def reduceList(t,nElementToRemove):
    #order the list
    newList.sort()

    #remove n element at the beginning
    newList = t[nElementToRemove:]

    #remove n element at the end
    newList = newList[:(len(newList)-nElementToRemove)]
    
    return newList

def main():
    line = input("Inserisci un numero (0 per uscire): ")
    t =[]
    while line!="0":
        number = int(line)
        t.append(number)
        line = input("Inserisci un numero (0 per uscire): ")

    if(len(t)<4):
        print("Devi inserire almeno 4 caratteri!")
    else:
        reducedList = reduceList(t, 2)
        
        print("La lista inserita è: ")
        print(t)
        print("La lista ridotta è: ")
        print(reducedList)

main()