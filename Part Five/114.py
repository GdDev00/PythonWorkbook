#Ex. 114 Negatives, Zeros and Positives

negativeNumbers=[]
zeroNumbers=[]
positiveNumbers=[]

line = input("Inserisci un numero intero: ")
while(line!=""):

    number = int(line)

    if number < 0:
        negativeNumbers.append(number)
    elif number == 0:
        zeroNumbers.append(number)
    elif number > 0:
        positiveNumbers.append(number)

    line = input("Inserisci un numero intero: ")

print("I numeri negativi inseriti sono: ")
for negatives in negativeNumbers:
    print(negatives, end=" ")
print("")

for zero in zeroNumbers:
    print(zero, end=" ")
print("")

print("I numeri positivi inseriti sono: ")
for positives in positiveNumbers:
    print(positives, end=" ")
