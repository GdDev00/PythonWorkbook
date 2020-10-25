#Ex. 133 Does a List Contain a Sublist

def isSublist(larger, smaller):
    #la lista è vuota
    if len(smaller) == 0:
        return True
    
    index = larger.index(smaller[0])
    for c in range(len(smaller)):
        if larger[index] == smaller[c]:
            index += 1
        else:
            return False
        
    return True

def test():
    larg = [1,2,3,4,5,6,7,8,9,10]
    small = [5,6,7]
    result = isSublist(larg,small)
    if result == True:
        print ("La lista inserita è una sottolista!")
    else:
        print("La lista inserita non è una sottolista")

test()