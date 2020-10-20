#Ex. 120 Formatting a list

def formatList(listString):
    if len(listString)==0:
        return "String is empty!"

    if len(listString)==1:
        return listString[0]

    result=""
    for i in range (0, len(listString)-2):
        result += listString[i] + ", "

    result += listString[-2] + " and "
    result += listString[-1]

    return result


line = input("Inserisci un elemento: ")
t = []
while line!="":
    t.append(line)
    line = input("Inserisci un elemento: ")

formattedList = formatList(t)
print(formattedList)
