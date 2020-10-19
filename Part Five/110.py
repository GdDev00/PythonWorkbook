#Ex. 110 Sorted Order

line = input("Inserisci un numero intero (0 per uscire:): ")

t=[]

while line!="0":
    number = int(line)
    t.append(number)
    line = input("Inserisci un numero intero (0 per uscire:): ")

t.sort()

print("I numeri inseriti (ordinati in ordine crescente) sono: ")
for num in t:
    print(num)
