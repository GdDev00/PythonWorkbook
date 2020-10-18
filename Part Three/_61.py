
counter = 0
sum = 0

num = None

while num!=0:
    num = int(input(("Inserisci numero decimale: ")))
    if(num!=0):
        counter +=1
        sum +=num


print("La media dei numeri inseriti è: {0}".format(sum/counter))

