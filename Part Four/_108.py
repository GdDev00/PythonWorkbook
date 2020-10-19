
positivi=[]
negativi=[]
zeri=[]

line = float(input("Inserisci un numero intero: "))

while line != "":
    if line <0:
        negativi.append(line)
    elif line == 0:
        zeri.append(line)
    elif line > 0:
        positivi.append(line)
    
    line = float(input("Inserisci un numero intero: "))

print("I numeri negativi sono:", end=" ")
for number in negativi:
    print(number, end =" ")
print("")


print("Gli zeri sono:", end=" ")
for number in zeri:
    print(number, end =" ")
print("")

print("I numeri positivi sono:", end=" ")
for number in positivi:
    print(number, end =" ")
print("")