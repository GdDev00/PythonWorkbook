


def riduciLista(valuesList, nOfElement):

    newList = sorted(valuesList)

    for i in range(nOfElement):
        newList.pop()

    for c in range(nOfElement):
        newList.pop(0)

    return newList



def main():
    s = input("Insersci un valore intero (premi spazio per uscire): ")
    values=[]
    
    while s != "":
        num = int(s)
        values.append(num)
        s = input("Insersci un valore intero (premi spazio per uscire): ")

    if(len(values) <4):
        print("Devi inserire almeno 4 numeri!")
    else:
        print("I valori inseriti sono: ", values)
        print("La stringa ridotta è", riduciLista(values,2))


main()