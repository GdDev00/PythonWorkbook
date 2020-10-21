#Ex. 127 Is a list already in sorted order?

def isSorted(t):
    sorted=True
    for i in range(len(t)-1):
        a = t[i]
        print(a)
        b = t[i+1]
        print(b)

        print (a<b)
        result = t[i] < t[i+1]
        print(result)

        if result ==True:
            sorted=True
        else:
            sorted=False
            break
    return sorted


t=[]
line = input("inserisci un numero: ")
while line !="":
    t.append(int(line))
    line = input("inserisci un numero: ")

result = isSorted(t)
if(result):
    print("La sequenza è ordinata")
else:
    print("La sequenza non è ordinata")



