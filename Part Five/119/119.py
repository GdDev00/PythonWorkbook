#Ex. 119 Below and Above Average

line = input("Inserisci un numero intero: ")
t=[]

while line !="0":
    num = float(line)
    t.append(num)
    line = input("Inserisci un numero intero: ")

average = sum(t) / len(t)

belowAverageValues=[]
for number in t:
    if number < average:
        belowAverageValues.append(number)
print("I numeri al di sotto della media sono: ")
print(belowAverageValues)

print("La media dei numeri inseriti è: %.2f" %average)

aboveAverageValues = []
for number in t:
    if number > average:
        aboveAverageValues.append(number)
print("I numeri al di sopra della media sono: ")
print(aboveAverageValues)
