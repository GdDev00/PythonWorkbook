#Ex. 113 : Avoiding Duplicates

line = input("Inserisci parola: ")

t=[]
while line !="":
    if line not in t:
        t.append(line)
    line = input("Inserisci parola: ")

for word in t:
    print(word)