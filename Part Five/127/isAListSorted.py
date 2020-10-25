#Ex. 127 Is a list already in sorted order?

def isSorted(t):
    sorted=True
    for i in range(len(t)-1):
        result = t[i] < t[i+1]

        if result ==True:
            sorted=True
        else:
            sorted=False
            break

    if sorted == False:
        for i in range(len(t)-1):
            result = t[i]> t[i+1]

            if result ==True:
                sorted=True
            else:
                sorted=False
    
    return sorted
    


t=[1,2,3,7,4,5,6]
#line = input("inserisci un numero: ")
#while line !="":
#    t.append(int(line))
 #   line = input("inserisci un numero: ")

result = isSorted(t)
if(result):
    print("La sequenza è ordinata")
else:
    print("La sequenza non è ordinata")



