
line= input("Inserisci stringa: ")
words=[]

while line != "":
    if line not in words:
        words.append(line)

    line= input("Inserisci stringa: ")

for word in words:
    print(word)
