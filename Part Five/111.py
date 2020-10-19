#Ex. 111 Reverse Order

line = input("Inserisci un numero intero (0 per uscire:): ")

t=[]

while line!="0":
    number = int(line)
    t.append(number)
    line = input("Inserisci un numero intero (0 per uscire:): ")

t.sort(reverse=True)

print("I numeri inseriti (ordinati in ordine decrescente) sono: ")
for num in t:
    print(num)